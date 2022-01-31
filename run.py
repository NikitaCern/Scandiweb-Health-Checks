from check import check_health
from print_helper import bold, color_text, print_header
import colorama

if __name__ == '__main__':
    colorama.init()
    print_header()
    print(bold("Enter the url ("), end="")
    print(color_text(" https://www.example.com/  ", "grey"), end="")
    print(bold(") of the project you want to check: "), end="")

    url = input()
    url = url.strip()
    check_health(url)
