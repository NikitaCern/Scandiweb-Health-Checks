import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from checks.server import check_server
from checks.application import check_application
from checks.performance import check_performance
from checks.security import check_security
from checks.eCommerce import check_eCommerce
from print_helper import color, show_error

TIME_TO_WAIT = 10

def check_health(FE_url, BE_url):
    try:
        page_source, console_output, networking, backend_performance= page_load(FE_url)
    except:
        print(color("Cannot connect to website", "red"))
        show_error()
        return

    FE_url = FE_url[:-1]
    BE_url = BE_url[:-1]
    check_server()
    check_application(console_output, networking)
    check_performance(FE_url, backend_performance)
    check_security(FE_url, BE_url)
    check_eCommerce(FE_url, page_source)
        
def page_load(url):

    page_source = ""
    console_output = ""
    networking = ""
    backend_performance = -1

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--incognito")
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = { 'browser':'ALL'}
    capabilities['goog:loggingPrefs'] = { "performance":"ALL" }

    driver = webdriver.Chrome(
        executable_path=f"{os.getcwd()}/chromedriver",
        chrome_options=options,
        desired_capabilities=capabilities
    )

    driver.get(url)
    time.sleep(TIME_TO_WAIT)

    page_source = BeautifulSoup(driver.page_source, 'html.parser')

    console_output = driver.get_log('browser')
    networking = driver.get_log("performance")

    requestStart = driver.execute_script("return window.performance.timing.requestStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")

    backend_performance = responseStart - requestStart

    driver.close()

    return page_source, console_output, networking, backend_performance
