import time
import requests
import json
from print_helper import category, color_cyan, color_text, color_yellow
import pyperclip


def check_performance(url, backendPerformance):
    print(category("Checking performance:"))
    TTFB(url, backendPerformance)
    page_insight(url)

def TTFB(url, backendPerformance):
    print("\tTTFB:", end = "")

    print(color_yellow(f" {backendPerformance} ms"))
    pass

def page_insight(url):
    print(color_text("\tPage Insight:","grey"))
    pass
    page_insight_api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}"
