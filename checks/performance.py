from urllib.parse import quote
from print_helper import category, color

def check_performance(url, backend_performance):
    print(category("Checking performance:"))
    TTFB(url, backend_performance)
    page_insight(url)

def TTFB(url, backend_performance):
    print("\tTTFB:", end = "")
    print(color(f" {backend_performance} ms", "yellow"))

def page_insight(url):
    print("\tPage Insight: ", end = "")
    url = quote(url, safe ='')
    page_insight_url = f"https://pagespeed.web.dev/report?url={url}"
    print(page_insight_url)
