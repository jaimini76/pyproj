#!/usr/bin/env python3
import asyncio


async def count():
    print("One")
    start = time.perf_counter()
    await asyncio.sleep(1)
    end = time.perf_counter()
    elapsed_time = end - start
    print(f"count() executed in {elapsed:0.2f} seconds.")

    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")