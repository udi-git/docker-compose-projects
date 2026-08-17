# Dockerized Clock & Button Microservices

This project demonstrates a multi-container architecture using Docker Compose, Flask, and internal container networking. It consists of two separate Python web services communicating with each other.

## Project Architecture

The project is built with two microservices:

1. **Clock App (`clock_app` - Port 5001):**
   * A Flask-based web application that displays a specific timestamp, initialized at server startup using the Israel timezone (UTC+3).
   * Exposes a REST API endpoint (`POST /update_time`) that subtracts 1 minute from the current displayed time.
   * **UX Feature:** The HTML frontend includes a `<meta http-equiv="refresh" content="2">` tag, creating an automatic 2-second refresh loop. This allows the user to see the time changes in real-time without needing to manually refresh the page.

2. **Button App (`button_app` - Port 5002):**
   * A separate Flask web application serving a simple UI with a single button.
   * When clicked, the backend uses the Python `requests` library to send a POST request to the Clock App's API.
   * Utilizes Docker's internal DNS routing to communicate directly with the Clock App via `http://clock_app:5001/update_time`.

## Project Structure

```text
.
├── docker-compose.yml
├── clock_app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       └── index.html
└── button_app/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    └── templates/
        └── index.html

How to Run
Make sure you have Docker and Docker Compose installed.

Clone this repository and navigate to the root folder.

Build and start the containers using the following command:

Bash
docker compose up --build
Open your web browser:

Clock Interface: http://localhost:5001

Controller Interface: http://localhost:5002

How to Use
Place the two browser tabs side by side.

Click the "Subtract 1 Minute" button in the Button App (Port 5002).

Watch the Clock App (Port 5001) automatically update its displayed time without requiring a manual page reload, thanks to the HTML auto-refresh implementation.

Technical Highlights
Layer Caching: Optimized Dockerfile design by separating requirements.txt from source code to leverage Docker layer caching and reduce build times.

Timezone Handling: Managed datetime timezone settings within the Python logic to bypass the missing tzdata package in the python:3.9-slim image.

Internal Networking: Showcases Docker Compose's ability to resolve service names (e.g., clock_app) to internal IP addresses.
