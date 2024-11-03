# Docker Demo Project: Flask App with Redis
The project serves as a learning exercise to understand how to containerize a web application and use environment variables to configure the Redis connection.
The project consists of a Flask application that displays a custom message to repeat visitors. The application uses Redis as a cache to keep track of the number of visits. If the Redis connection fails, the application will retry the connection a specified number of times before raising an error.

Docker Compose
The project includes a docker-compose.yml file to define a Docker Compose service for the Flask application and Redis. The service uses the Docker image built from the Dockerfile and sets environment variables for the Redis connection.

Running the App with Docker

Build the Docker image: docker build -t dockerized-hit .

Run the Docker container: docker run -p 5000:5000 -e REDIS_HOST=redis -e REDIS_PORT=6379 hit-counter-app

Open a web browser and navigate to http://localhost:8000
