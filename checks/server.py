
from print_helper import category, color_text


def check_server(url):
    print(category("Checking server:"))
    error_log()
    db_backup()
    cron_health()
    disk_space()
    
def error_log():
    print(color_text("\tError logs:","grey"))
    pass

def db_backup():
    print(color_text("\tDB backups:","grey"))
    pass

def cron_health():
    print(color_text("\tCron health:","grey"))
    pass

def disk_space():
    print(color_text("\tDisk space:","grey"))
    pass