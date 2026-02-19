import concurrent.futures
import time
import requests

def get_session():
    return requests.Session()

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(download_site, sites)
    print()

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    print("Starting downloads")
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")