from datetime import datetime

def get_time():
    return datetime.now()

def get_formatted_date(t=None):
    if not t:
        t = datetime.now()
    d_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水',
          'Thu': '木', 'Fri': '金', 'Sat': '土'}
    key = t.strftime('%a')
    w = d_week[key]
    d = t.strftime('%Y年%m月%d日') + f'（{w}）' #f'{now:%Y年%m月%d日}（{w}）'
    return d

print(get_formatted_date())