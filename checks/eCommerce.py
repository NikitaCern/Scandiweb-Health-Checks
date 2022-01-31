import sys
import time
import requests
from bs4 import BeautifulSoup
from print_helper import category, color_red, color_green, color_yellow, bold

def check_eCommerce(url, page_source):
    print(category("Checking eCommerce:"))
    print(google_tag_manager(page_source))

    response, contents = robots_txt(url)
    print(response)

    print(sitemap(contents))

def google_tag_manager(page_source):
    print(bold("\tGoogle tag manager: ") , end ="")

    response = ""
    matched_lines = []

    try:
        for script in page_source.findAll('script',{"src":True}):
            if script['src'].find("googletagmanager")>0:
                matched_lines.append(script['src'])

        if not matched_lines:
            response += color_red("No Google tag manager found!")
            return response
        
        response += color_green("Google tag manager present!")

        for line in matched_lines:
            response += f" [{line}]"
        
        return response
    except:
        return(color_red(f"Error: {sys.exc_info()[0]}"))

def robots_txt(url):
    print(bold("\tRobots.txt: "), end="")
    response = ""
    try:
        url += "/robots.txt"
        temp_response, text= url_exists_not_empty(url)
        response += temp_response
        return response, text
    except:
        return(color_red(f"Error: {sys.exc_info()[0]}")), ""

def sitemap(contents):
    print(bold("\tSitemap.xml:"), end="")
    response = ""
    try:
        if contents is  None:
            response += color_red(" No sitemap found!")
            return response
        matched_lines = [line for line in contents.split('\n') if "Sitemap: " in line]
        response += color_green( f" Found {len(matched_lines)} sitemaps:\n")
        for position, line in enumerate(matched_lines):
            response += f"\t {position+1} : {url_exists_not_empty(line[9:].strip())[0]} \n"
        return response
    except:
        return(color_red(f"Error: {sys.exc_info()[0]}"))

def url_exists_not_empty(url):
    response = ""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            response += color_red("Does not exist! " + str(r))
            return response, None
        response += color_green("Exists and is ")
        if not r.text:
            response += color_red("empty ")
            return response, None
        response += color_green("not empty ")
        response += f"[{url}]"
        return response, r.text
    except:
        return(color_red(f"Error: {sys.exc_info()[0]}")), ""