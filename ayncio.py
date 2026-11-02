import asyncio 
import time


async def heat_water():
    print(f'heating the water....❄️💧')
    await asyncio.sleep(10)
    print(f'Water is heated.....🔥💧')

async def cookies():
    print("Getting the cookies")
    await asyncio.sleep(5)
    print(f'Got the cookies🍪')

async def main():
    start_time=time.time()
    await asyncio.gather(heat_water(),cookies())
    end_time=time.time()
    print(f'Total time:{end_time-start_time}')


asyncio.run(main())