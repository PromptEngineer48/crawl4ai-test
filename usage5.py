## going over commit pages

import json
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

import asyncio


async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        url = "https://github.com/microsoft/TypeScript/commits/main"
        session_id = "typescript_commits_session"
        all_commits = []

        js_next_page = """
        const button = document.querySelector('a[data-testid="pagination-next-button"]');
        if (button) button.click();
        """

        wait_for = """() => {
            const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
            if (commits.length === 0) return false;
            const firstCommit = commits[0].textContent.trim();
            return firstCommit !== window.lastCommit;
        }"""

        schema = {
            "name": "Commit Extractor",
            "baseSelector": "li.Box-sc-g0xbh4-0",
            "fields": [
                {
                    "name": "title",
                    "selector": "h4.markdown-title",
                    "type": "text",
                    "transform": "strip",
                },
            ],
        }
        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

        for page in range(3):  # Crawl 3 pages
            result = await crawler.arun(
                url=url,
                session_id=session_id,
                css_selector="li.Box-sc-g0xbh4-0",
                extraction_strategy=extraction_strategy,
                js_code=js_next_page if page > 0 else None,
                wait_for=wait_for if page > 0 else None,
                js_only=page > 0,
                bypass_cache=True,
                headless=False,
            )

            assert result.success, f"Failed to crawl page {page + 1}"

            commits = json.loads(result.extracted_content)
            all_commits.extend(commits)

            print(f"Page {page + 1}: Found {len(commits)} commits")

        await crawler.crawler_strategy.kill_session(session_id)
        print(f"Successfully crawled {len(all_commits)} commits across 3 pages")


asyncio.run(main())
