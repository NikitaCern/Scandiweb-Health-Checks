import sys
from termcolor import colored

LINE_LEN = 73

def print_header():
    print(bold(color(middle(" Scandiweb "), 'red')))
    print(bold(color(
"""                                                                         
 **  ╔══╦══╗      ╔═╗╔═╗        ╔═╗          ╔═╗╔═╗     ╔═╗      ╔═╗   **
 **  ║  ║  ╠══╦══╦╣ ╚╣ ╚╦═╗╔═╦╗ ║ ╚╦══╦══╗╔═╗║ ╚╣ ╚╗ ╔══╣ ╚╦══╦══╣ ╠╗  **
 **  ║ ║║║ ║ ║║ ║║║ ╔╣ ║║ ╚╣ ║║ ║ ║║ ╩╣ ╬╚╣ ╚╣ ╔╣ ║║ ║ ═╣ ║║ ╩╣ ═╣ ═╣  **
 **  ╚═╩═╩═╩══╩═╩═╩══╩═╩╩══╬═╗║ ╚═╩╩══╩═══╩══╩══╩═╩╝ ╚══╩═╩╩══╩══╩═╩╝  **
 **                        ╚══╝                                        **
""", 'cyan')))

    print(bold(color(middle("="), 'red')))

    print("""
    How to use:
    1. Find the url of the website
    2. Paste url
    3. When web browser opens feel free to click around, or not
    4. Wait for results!
    """)

def middle(text):
    line_length = (LINE_LEN - len(text)) // 2
    return "="*line_length + text + "="*line_length

def category(text):
    string = "\n"
    string += "="*LINE_LEN + "\n"
    string += f"  {text}:" + "\n"
    string += "="*LINE_LEN
    return string

def bold(text):
    return colored(text, attrs=['bold'])

def dark(text):
    return colored(text, attrs=['dark'])

def color(text, color_name):
    return colored(text, color_name)

def show_error():
    print(color(f"Error: {sys.exc_info()}", "red"))
