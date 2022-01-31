import sys
import requests
import datetime
import json
import ssl, socket
from print_helper import category, color_green, color_red, color_text, color_yellow


def check_security(url):
    print(category("Checking security:"))
    magento_admin_url(url)
    sensitive_urls(url)
    SSL_expiration(url)
    admin_users()
    non_commited_changes()

def magento_admin_url(url):
    print("\tMagento admin url:")
    danger_list = ['/admin', '/magento', '/magento/admin', '/backend']
    try:
        for item in danger_list:
            temp_url = url + item
            r = requests.get(temp_url)
            if r.status_code is 200:
                print(f"\t {color_red(r)} {r.url}")
    except:
        print(color_red(f"Error: {sys.exc_info()[0]}"))

def sensitive_urls(url):
    print("\tSensitive urls:")
    danger_list = ['/dev', '/.git', '/admin', '/rss', '/app/etc/local.xml', '/info.php']
    try:
        for item in danger_list:
            temp_url = url + item
            r = requests.get(temp_url)
            if r.status_code is 200:
                print(f"\t {color_red(r)} {r.url}")
            else:
                print(f"\t {color_green(r)} {r.url}")
    except:
        print(color_red(f"Error: {sys.exc_info()[0]}"))

def SSL_expiration(url):
    print("\tSSL expiration: ", end="")
    try:
        socket.getaddrinfo('127.0.0.1', 8080)
        hostname = url[12:]
        port = '443'
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname = hostname) as ssock:
                certificate = ssock.getpeercert()
        
        certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
        monthsToExpiration = round((certExpires - datetime.datetime.now()).days/30)

        color = "green"

        if monthsToExpiration <= 5: color="cyan"
        if monthsToExpiration <= 3: color="yellow"
        if monthsToExpiration <= 2: color="red"
        
        print(color_text(f"Good for ~{monthsToExpiration} months [{certExpires.strftime('%d %b %Y')}]", color))

    except:
        print(color_red(f"Error: {sys.exc_info()[0]}"))

def admin_users():
    print(color_text("\tAdmin users:","grey"))
    pass

def non_commited_changes():
    print(color_text("\tNon-commited changes:","grey"))
    pass