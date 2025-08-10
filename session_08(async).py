import time

def say_hello(name):
    print(f"Hello {name} 👋")
    time.sleep(1)  # pretend to wait for something (like downloading data)
    print(f"Goodbye {name} 👋")

def main():
    say_hello("Alice")
    say_hello("Bob")

main()





# async -----------------------------------------
import asyncio

# Step 1: Define an async function
async def say_hello(name):
    print(f"Hello {name} 👋")
    await asyncio.sleep(1)  # pretend to wait for something (like downloading data)
    print(f"Goodbye {name} 👋")

# Step 2: Run async code
async def main():
    # Run two functions at the same time
    await asyncio.gather(
        say_hello("Alice"),
        say_hello("Bob")
    )

# Step 3: Start the async program
asyncio.run(main())










# advanced async : Get title of multiple site async
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_and_print_title(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        print(f"Title from {url}: {title}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_print_title(session, url) for url in urls]
        # Schedule all tasks concurrently, print results as they come
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ]
    asyncio.run(main(urls))

