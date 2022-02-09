import re
import colorama
from check import check_health
from print_helper import bold, color, print_header, dark

if __name__ == '__main__':
    colorama.init()
    print_header()
    print(bold("Enter the FE url ("), end="")
    print(dark("https://www.example.com/"), end="")
    print(bold(") of the project you want to check: "), end="")

    pattern = re.compile('^http["s"]?:\/\/www[.]([^\/]*)[.]([^\/]*)\/$')
    FE_url = input().strip()

    while pattern.fullmatch(FE_url) is None:
        print(f"Make sure the URL is similar to this: {color('https://www.example.com/ : ', 'red')}", end="")
        FE_url = input().strip()

    print(bold("Enter the BE url (if its the same, or you dont care about it, press enter) "), end="")

    BE_url = input().strip()
    if BE_url:
        while pattern.fullmatch(BE_url) is None:
            print(f"Make sure the URL is similar to this: {color('https://www.example.com/ : ', 'red')}", end="")
            BE_url = input().strip()

    check_health(FE_url, BE_url)
