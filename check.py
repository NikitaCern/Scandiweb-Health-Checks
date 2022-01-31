import time
import requests
import sys
import shutil
import tempfile
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from checks.server import check_server
from checks.application import check_application
from checks.performance import check_performance
from checks.security import check_security
from checks.eCommerce import check_eCommerce
from print_helper import color_red

def check_health(url):
    try:
        page_source, console_output, networking, backendPerformance= page_load(url)
    except:
        print (color_red("Cannot connect to website"))
        print(color_red(f"Error: {sys.exc_info()}"))
        return  

    url = url[:-1]
    check_server(url)
    check_application(url, console_output, networking)
    check_performance(url, backendPerformance)
    check_security(url)
    check_eCommerce(url, page_source)
        
def page_load(url):

    page_source = ""
    console_output = ""
    networking = ""
    backendPerformance = -1

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--incognito")
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = { 'browser':'ALL'}
    capabilities['goog:loggingPrefs'] = { "performance":"ALL" }

    driver = webdriver.Chrome(executable_path='/home/scandiweb/github/Scandiweb-Health-Checks/chromedriver', chrome_options=options, desired_capabilities=capabilities)
    driver.get(url)
    time.sleep(10)
    
    page_source = BeautifulSoup(driver.page_source, 'html.parser')

    console_output = driver.get_log('browser')
    networking = driver.get_log("performance")

    requestStart = driver.execute_script("return window.performance.timing.requestStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")

    backendPerformance = responseStart - requestStart

    driver.close()
       
    return page_source, console_output, networking, backendPerformance