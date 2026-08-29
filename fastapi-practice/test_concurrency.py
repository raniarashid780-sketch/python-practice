import time
import requests
from concurrent.futures import ThreadPoolExecutor

def call(url):
    start = time.time()
    requests.get(url)
    return time.time() - start

urls = [
    "http://127.0.0.1:8000/broken-async-delay?a=1",
    "http://127.0.0.1:8000/broken-async-delay?a=2",
]

overall_start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(call, urls))

print("Individual call durations:", results)
print("Total wall-clock time:", time.time() - overall_start)