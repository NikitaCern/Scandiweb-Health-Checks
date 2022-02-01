from urllib.parse import quote
from print_helper import category, color, dark

def check_performance(url, backendPerformance):
    print(category("Checking performance:"))
    TTFB(url, backendPerformance)
    page_insight(url)

def TTFB(url, backendPerformance):
    print("\tTTFB:", end = "")

    print(color(f" {backendPerformance} ms", "yellow"))
    pass

def page_insight(url):
    print("\tPage Insight: ", end = "")

    url = quote(url, safe ='')

    page_insight_url = f"https://pagespeed.web.dev/report?url={url}"
    print(page_insight_url)




