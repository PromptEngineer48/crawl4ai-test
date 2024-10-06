import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.example.com")
        print(result.markdown[:500])  # Print first 500 characters


if __name__ == "__main__":
    asyncio.run(main())
