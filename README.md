# HOW TO USE RUN ->

## Step 1. 
Run the FastAPI App present in the python-backend folder, 
using the following command inside the python-backend folder ->
    fastapi dev /src/app.py

## Step 2.
Inside another terminal, goto the python-worker folder,
Run the worker code, using the following command ->
    python /src/main.py

## Step 3.
To push the data inside the Redis Queue, use the fastapi endpoint

## Step 4.
The Worker code will automatically pop the data from the Redis queue

## Step 5.
You can scale the workers, by running the worker code in multiple terminals
