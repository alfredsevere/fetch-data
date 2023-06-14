import asyncio
import random

async def fetch_data(id):
    wait_time = random.randint(1, 5)  # Simulate random server response times
    await asyncio.sleep(wait_time)
    print(f"Task {id} finished fetching data after {wait_time}s")

async def main():
    tasks = [fetch_data(i) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
