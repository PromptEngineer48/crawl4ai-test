from crawl4ai import WebCrawler

# Create the WebCrawler instance
crawler = WebCrawler()
crawler.warmup()

# Run the crawler with a CSS selector to extract only H2 tags
result = crawler.run(url="https://www.nbcnews.com/business", css_selector="h2")


print("Extracted H2 tags:", result.extracted_content)
