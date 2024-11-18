# Running Redis using Docker Container

## STEPS ->

### 1. Run the command -> 
    docker run --name my-redis -d -p 6379:6379 redis
 It will run a container on port 6379, having redis running

    docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest

It will run a container on port 6379, having redis running,
Also a port localhost:8001, that will provide redis-stack GUI to view the data

### 2.  Go Inside the Container, running the Redis to access the Redis-cli ->
    docker exec -it <container_id> /bin/bash

### 3. Start the Redis CLI ->
    redis-cli
