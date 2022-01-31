
import enum
import json
import sys
from print_helper import category, color_green, color_red, color_text, color_yellow


def check_application(url, console_output, networking):
    print(category("Checking application:"))
    uptime()
    magento_error_log()
    cache_enabled()
    console_errors(console_output)
    networking_404(networking)

def uptime():
    print(color_text("\tUptime:","grey"))
    pass

def magento_error_log():
    print(color_text("\tMagento error log:","grey"))
    pass

def cache_enabled():
    print(color_text("\tMagento cache enabled:","grey"))
    pass

def console_errors(console_output):
    print("\tConsole errors:", end="")

    try:
        if not console_output:
            print(color_green("No console errors found!"))

        print(color_yellow(" Console errors found!"))
        map = {}
        for output in console_output:
            key = ""
            if output['level'] == "WARNING" or output['level'] == "SEVERE":
                key =  f"{color_red(output['level'])} :: {output['message'][:60]}..."
            else:
                key = f"{color_yellow(output['level'])} :: {output['message'][:60]}..."

            if key not in map.keys():
                map[key] = []

            map[key].append(f" {output['message']}")
            
        ordered_output = {}
        for key, value in map.items():
            if len(value) not in ordered_output.keys():
                ordered_output[len(value)] = []
            ordered_output[len(value)].append(
                { 
                    "key": key,
                    "values": value
                }
                )

        outputs = list(reversed(sorted(ordered_output.keys())))
        print_count = 0
        for value in outputs:
            for item in ordered_output[value]:      
                print(f"\t {value}x {item['key']}")

                for i in range(min(3,len(item['values']))): 
                    print(f"\t  {item['values'][i][:200]}")
                print_count+=1
                print()
                if print_count >=5:
                    return
    except:
        print(color_red(f"Error: {sys.exc_info()[0]}"))

def networking_404(networking):
    print("\tNetworking 404: ", end="")

    missing = []
    try:
        for x, entry in enumerate(networking):
            log = json.loads(entry["message"])["message"]
            if log["method"].find("Network") > 0:
                if log["params"]["statusCode"] >= 300:
                    missing.append({
                        "code": log["params"]["statusCode"],
                        "log": log
                        })

        if missing:
            print(missing)
            return
        
        print(color_green(f"No networking errors found!"))
    except:
        print(color_red(f"Error: {sys.exc_info()[0]}"))
# 'Network.requestWillBeSent': '',
# 'Network.requestWillBeSentExtraInfo': '',
# 'Network.responseReceivedExtraInfo': '',
# 'Network.responseReceived': '',
# 'Network.dataReceived': '',
# 'Network.loadingFinished': '',
# 'Network.requestServedFromCache': '',
# 'Network.resourceChangedPriority': '',