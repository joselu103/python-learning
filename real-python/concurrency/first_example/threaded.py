import time
import concurrent.futures
import requests
import threading

threading_local = threading.local()
def get_session():
    if not hasattr(threading_local, "session"):
        threading_local.session = requests.Session()
    return threading_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    for url in sites:
        download_site(url)

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