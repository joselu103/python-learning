import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

    for task in tasks:
        print(task.result())


if __name__ == '__main__':
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice"
            ] * 80

    print("Starting downloads")
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")