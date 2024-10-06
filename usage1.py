## basic usage
import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # We'll add our crawling code here
        pass


if __name__ == "__main__":
    asyncio.run(main())
