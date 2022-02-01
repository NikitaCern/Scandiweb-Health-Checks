import sys
import time
import requests
from bs4 import BeautifulSoup
from print_helper import category, color, bold, show_error

def check_eCommerce(url, page_source):
    print(category("Checking eCommerce:"))
    google_tag_manager(page_source)

    contents = robots_txt(url)
    
    sitemap(contents)

def google_tag_manager(page_source):
    print(bold("\tGoogle tag manager: ") , end ="")

    response = ""
    matched_lines = []

    for script in page_source.findAll('script',{"src":True}):
        if script['src'].find("googletagmanager")>0:
            matched_lines.append(script['src'])

    if not matched_lines:
        response += color("No Google tag manager found!", "red")
        print(response)
        return
    
    response += color("Google tag manager present!", "green")

    for line in matched_lines:
        response += f" [{line}]"
    
    print(response)

def robots_txt(url):
    print(bold("\tRobots.txt: "), end="")
    contents = ""
    url += "/robots.txt"

    try:
        response, contents = url_exists_not_empty(url)
        print(response)
    except:
        show_error()
        return ""

    return contents

def sitemap(contents):
    print(bold("\tSitemap.xml:"), end="")

    if contents is  None:
        print(color(" No sitemap found!", "red"))
        return

    matched_lines = [line for line in contents.split('\n') if "Sitemap: " in line]
    text = f" Found {len(matched_lines)} sitemaps:"

    if not len(matched_lines):
        print(color(text, "red"))
        return

    print(color(text,"green"))
    for position, line in enumerate(matched_lines):
        try:
            url = line[9:].strip()
            response = f"\t {position+1} : {url_exists_not_empty(url)[0]}"
            print(response)
        except:
            show_error()

def url_exists_not_empty(url):
    response = ""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            response += color("Does not exist! " + str(r), "red")
            return response, None
        response += color("Exists and is ", "green")
        if not r.text:
            response += color("empty ", "red")
            return response, None
        response += color("not empty ", "green")
        response += f"[{url}]"
        return response, r.text
    except:
        show_error()
        return "" , ""