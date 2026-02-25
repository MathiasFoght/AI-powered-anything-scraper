import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

# Our Bright Data web scraper connection
SBR_WEBDRIVER = 'https://brd-customer-hl_e6cbb8f3-zone-ai_scraper:ewi0kuz05voo@brd.superproxy.io:9515'

# Main function to scrape
def scrape_website(website: str):
    print("Launching chrome browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(command_executor=sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)

        #CAPTCHA handling
        print("Waiting captcha to solve...")
        solve_result = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print("Captcha solve status:", solve_result['value']['status'])
        print("Navigated. Scraping page data...")
        html = driver.page_source
        print("Page data scraped", html)
        return html

# Extract the body content
def extract_body_content(html_content: str):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# Clean up (remove JS and CSS from scraped content)
def clean_body_content(body_content: str):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# Handle token-limit for LLM. We split the data into batches of 6k characters for processing big websites
def split_dom_content(dom_content: str, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]


