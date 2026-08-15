# Docker Compose - Flask & Redis App

This project demonstrates a multi-container environment using **Docker Compose**. 
The system consists of a Flask web application that communicates with a Redis cache server to manage a page view counter.

## 📂 Project Structure
* `app.py` - The Python/Flask application code that connects to the Redis server.
* `Dockerfile` - The build instructions for the Flask container (including dependencies).
* `docker-compose.yml` - The orchestration file that runs both the Web and Redis containers and links them together.

## 🚀 How to Run the Project

1. Ensure Docker Desktop is running on your machine.
2. Open the terminal in the project directory and run the following command:
   ```bash
   docker compose up --build
