import re
import colorama
from check import check_health
from print_helper import bold, color, print_header, dark

if __name__ == '__main__':
    colorama.init()
    print_header()
    print(bold("Enter the url ("), end="")
    print(dark("https://www.example.com/"), end="")
    print(bold(") of the project you want to check: "), end="")

    pattern = re.compile('^http["s"]?:\/\/www[.]([^\/]*)[.]([^\/]*)\/$')
    url = input().strip()

    while pattern.fullmatch(url) is None:
        print(f"Make sure the URL is similar to this: {color('https://www.example.com/ : ', 'red')}", end="")
        url = input().strip()

    check_health(url)
