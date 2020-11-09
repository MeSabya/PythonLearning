import asyncio
# Bounded semaphore is used to restrict N number of concurrent task/coroutines at a time

async def do_work(sem, n):
    async with sem:
        print("Start work fir work", n)
        await asyncio.sleep(1)
        print("End of work for", n)

async def main():
    tasks = []
    semaphore = asyncio.BoundedSemaphore(5)
    for i in range(10):
        tasks.append(asyncio.create_task(do_work(semaphore, i)))
    await asyncio.gather(*tasks)

if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.run_until_complete(main())
