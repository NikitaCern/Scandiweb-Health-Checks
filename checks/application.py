import json
from print_helper import category, color, dark, show_error

def check_application(console_output, networking):
    print(category("Checking application:"))
    uptime()
    magento_error_log()
    cache_enabled()
    console_errors(console_output)
    networking_404(networking)

def uptime():
    print(dark("\tUptime:"))

def magento_error_log():
    print(dark("\tMagento error log:"))

def cache_enabled():
    print(dark("\tMagento cache enabled:"))

def console_errors(console_output):
    print("\tConsole errors:", end="")

    try:
        if not console_output:
            print(color("No console errors found!","green"))

        print(color(" Console errors found!","yellow"))
        map = {}
        for output in console_output:
            key = ""
            if output['level'] == "WARNING" or output['level'] == "SEVERE":
                key =  f"{color(output['level'], 'red')} :: {output['message'][:60]}..."
            else:
                key = f"{color(output['level'],'yellow')} :: {output['message'][:60]}..."

            if key not in map.keys():
                map[key] = []

            map[key].append(f" {output['message']}")

        ordered_output = {}
        for key, value in map.items():
            if len(value) not in ordered_output.keys():
                ordered_output[len(value)] = []
            ordered_output[len(value)].append({
                    "key": key,
                    "values": value
                })

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
        show_error()

def networking_404(networking):
    print("\tNetworking 404: ", end="")

    missing = []
    try:
        for entry in networking:
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

        print(color(
            "No networking errors found!",
            "green"))
    except:
        show_error()
