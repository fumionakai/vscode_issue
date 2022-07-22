from datetime import datetime

def get_time():
    return datetime.now()

def get_formatted_date(t=None):
    if not t:
        t = datetime.now()
    d = t.strftime('%Y年%m月%d日（%a）')
    return d

print(get_formatted_date())