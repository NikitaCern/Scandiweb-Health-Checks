from termcolor import colored

LINE_LEN = 91

def print_header():
    
    print(bold(color_red(middle("  Scandiweb  "))), end="")
    print(bold(color_cyan(
"""
**   __  __         _   _    _        _  _          _ _   _       ___ _           _      **
**  |  \/  |___ _ _| |_| |_ | |_  _  | || |___ __ _| | |_| |_    / __| |_  ___ __| |__   **
**  | |\/| / _ \ ' \  _| ' \| | || | | __ / -_) _` | |  _| ' \  | (__| ' \/ -_) _| / /   **
**  |_|  |_\___/_||_\__|_||_|_|\_, | |_||_\___\__,_|_|\__|_||_|  \___|_||_\___\__|_\_\   **
**                             |__/                                                      **
""")), end="")
    print(bold(color_red(middle("="))), end="\n")

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

def color_green(text):
    return colored(text, 'green')

def color_yellow(text):
    return colored(text, 'yellow')

def color_red(text):
    return colored(text, 'red')

def color_cyan(text):
    return colored(text, 'cyan')

def color_text(text, color):
    return colored(text, color)

