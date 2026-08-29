import asyncio
import time
from fastapi import FastAPI

app = FastAPI()

# Task 1:
# Create GET /sync-delay (plain def) that time.sleep(3) then returns {"type": "sync", "done": True}
# Create GET /async-delay (async def) that await asyncio.sleep(3) then returns {"type": "async", "done": True}


@app.get("/sync-delay")
def sync_delay():
    time.sleep(3)
    return {"type": "sync", "done": True}


@app.get("/async-delay")
async def async_delay():
    await asyncio.sleep(3)
    return {"type": "async", "done": True}


# Task 2:
# Before testing: predict — if you open two browser tabs and hit /sync-delay in both at nearly the same time, do they finish at the same time or one after another? Same question for /async-delay.
# Test it for real: open two tabs, hit /sync-delay in both simultaneously, time it. Repeat for /async-delay.

# Prediction:
# Both /sync-delay and /async-delay will actually finish at the same time (~3 seconds).
#
# Why? Even though time.sleep(3) is blocking, FastAPI automatically offloads plain `def`
# functions to a background thread pool. So it blocks that individual thread, not the main loop.
# /async-delay relies on non-blocking await, so it yields control back to the event loop.
#
# (Note: If testing in browser tabs, add dummy query params like ?1 and ?2 so the browser
# doesn't queue identical GET requests itself!)


# Task 3:
# Report real timing: did /sync-delay tabs both take ~3s, or did the second wait for the first (~6s total)? Same for /async-delay.

# Real Timing Report:
# - /sync-delay: Both tabs complete in ~3s simultaneously. FastAPI handles standard def routes in separate thread pool threads.
# - /async-delay: Both tabs complete in ~3s simultaneously. Asyncio pauses the coroutine and allows the loop to serve the other tab concurrently.