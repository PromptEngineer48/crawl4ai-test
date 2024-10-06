## JSS SElection

from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import json

import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    schema = {
        "name": "News Articles",
        "baseSelector": "article.tease-card",
        "fields": [
            {
                "name": "title",
                "selector": "h2",
                "type": "text",
            },
            {
                "name": "summary",
                "selector": "div.tease-card__info",
                "type": "text",
            },
        ],
    }

    async with AsyncWebCrawler(
        verbose=True,
    ) as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            extraction_strategy=JsonCssExtractionStrategy(schema, verbose=True),
        )
        extracted_data = json.loads(result.extracted_content)
        print(f"Extracted {len(extracted_data)} articles")
        for i in range(5):
            print(json.dumps(extracted_data[i], indent=2))


asyncio.run(main())
