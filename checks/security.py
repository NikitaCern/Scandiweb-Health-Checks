import sys
import requests
import datetime
import json
import ssl, socket
from print_helper import category, color, show_error, dark

def check_security(url):
    print(category("Checking security:"))
    magento_admin_url(url)
    sensitive_urls(url)
    SSL_expiration(url)
    admin_users()
    non_commited_changes()

def get_urls_to_check(filename):
    urls = []
    try:
        with open(f"urls/{filename}", "r") as file:
            lines = file.readlines()
        for line in lines:
            urls.append(line.replace("\n", ""))
    except:
        show_error()
    return urls

def magento_admin_url(url):
    print("\tMagento admin url:")

    filepath = 'admin_urls.txt'

    danger_list = get_urls_to_check(filepath)
    if len(danger_list) < 0:
        print(color(
            f"{filepath} is empty!",
            "red"))
        return

    for item in danger_list:
        temp_url = url + item
        try:
            request = requests.get(temp_url)
            if request.status_code == 200:
                print(f"\t {color(request, 'red')} {request.url}")
        except:
            show_error()

def sensitive_urls(url):
    print("\tSensitive urls:")

    filepath = 'sensitive_urls.txt'

    danger_list = get_urls_to_check(filepath)
    if len(danger_list) < 0:
        print(color(
            f"{filepath} is empty!",
            "red"))
        return

    for item in danger_list:
        temp_url = url + item
        try:
            r = requests.get(temp_url)
            if r.status_code == 200:
                print(f"\t {color(r, 'red')} {r.url}")
            else:
                print(f"\t {color(r, 'green')} {r.url}")
        except:
            show_error()


def SSL_expiration(url):
    print("\tSSL expiration: ", end="")

    hostname = url[12:]
    port = '443'

    try:
        socket.getaddrinfo('127.0.0.1', 8080)
        context = ssl.create_default_context()

        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname = hostname) as ssock:
                certificate = ssock.getpeercert()

        cert_expires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
        months_to_expiration = round((cert_expires - datetime.datetime.now()).days/30)

        text_color = "green"

        if months_to_expiration <= 5:
            text_color="cyan"
        if months_to_expiration <= 3:
            text_color="yellow"
        if months_to_expiration <= 2:
            text_color="red"

        print(color(
                f"Good for ~{months_to_expiration} months [{cert_expires.strftime('%d %b %Y')}]",
                text_color))

    except:
        show_error()

def admin_users():
    print(dark("\tAdmin users:"))

def non_commited_changes():
    print(dark("\tNon-commited changes:"))
