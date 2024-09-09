# import redis
import time
import redis.asyncio as redis
import asyncio

client = redis.Redis(host="localhost", port=6379, decode_responses=True)

async def main():
    while True:
        response = await client.brpop("submissions", 0)
        print(response)
        # HERE ACTUALLY RUN THE USER's WORKER CODE LOGIC
        await asyncio.sleep(1)
        # SEND THE RESPONSE TO PUB-SUB
        print("Processed User's Submission")

asyncio.run(main())