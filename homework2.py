import asyncio

async def average(x):
    sum = 0
    for num in x:
        sum += num
    avg = sum / len(x)
    await asyncio.sleep(2)

    return avg


async def printAvg(y):
    print("Average for " + str(y) + " is " + str(await average(y)))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(printAvg([25, 45, 18, 1005, 8]))