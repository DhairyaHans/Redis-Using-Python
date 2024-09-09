from fastapi import FastAPI
from model import RequestBody
import json
import redis

app = FastAPI()
client = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.post("/submit")
def submitSolution(body: RequestBody):
    try:
        print(body)
        data = {
            "problemId": body.problemId,
            "userId": body.userId,
            "code": body.code,
            "language": body.language
        }
        print(json.dumps(data))
        client.lpush("submissions", json.dumps(data))
        return "Submission Received!"
    except Exception as e:
        raise e
    

