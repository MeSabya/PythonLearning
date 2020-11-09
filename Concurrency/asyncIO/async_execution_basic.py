'''
Question : What are the ways we can start a co-routine ?
Does the below code is the example of co-operative multi tasking ?

'''

import asyncio

async def example(message):
    print("start of example():", message)
    await asyncio.sleep(1)
    print("end of example():", message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable =  asyncio.create_task(example("First call"))              #example("First call")
    second_awaitable = asyncio.create_task(example("Second call"))              #example("Second call")
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)
results = loop.run_until_complete(main())
loop.close()