# Page Counter App - Flask & MySQL with Docker Compose

## Overview
This project is a containerized web application built with Python (Flask) and a MySQL database. It acts as a page counter, dynamically tracking and displaying the number of times the main page has been visited. The infrastructure is entirely orchestrated using Docker Compose.

## Project Structure
* `main.py` - The core Flask web application.
* `templates/index.html` - The HTML front-end template rendered by Flask.
* `requirements.txt` - Lists the Python dependencies required for the app (Flask, mysql-connector-python).
* `Dockerfile` - Builds the lightweight Python image and installs dependencies.
* `docker-compose.yml` - Defines and orchestrates the web and database services, network, and storage volumes.
* `init.sql` - Database initialization script that executes automatically on the first run to create the schema.

## Technical Highlights & Problem Solving
* **Automated Database Initialization:** Leverages the MySQL `docker-entrypoint-initdb.d` mechanism to seamlessly execute `init.sql` upon initial deployment. This automatically creates the `page_counter` table with an `AUTO_INCREMENT` primary key, aligning perfectly with the Flask application's logic.
* **Race Condition Mitigation:** Implements a `restart: on-failure` policy for the Flask service in the Compose file. This ensures that if the web container starts before the MySQL database is fully initialized and ready to accept connections (a common microservices race condition), it will gracefully restart and successfully connect once the database is up.
* **Data Persistence:** Utilizes a named Docker Volume (`mysql_data`) mapped to `/var/lib/mysql` to ensure that the page count data is saved persistently and survives container restarts or rebuilds.

## Prerequisites
* Docker
* Docker Compose

## How to Run
1. Clone this repository to your local machine.
2. Open a terminal in the project directory.
3. Build the images and start the containers:
   ```bash
   docker compose up -d --build
