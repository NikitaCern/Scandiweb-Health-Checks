from print_helper import category, color, dark

def check_server():
    print(category("Checking server:"))
    error_log()
    db_backup()
    cron_health()
    disk_space()

def error_log():
    print(dark("\tError logs:"))

def db_backup():
    print(dark("\tDB backups:"))

def cron_health():
    print(dark("\tCron health:"))

def disk_space():
    print(dark("\tDisk space:"))
