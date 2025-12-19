import datetime

moscow_tz = datetime.timezone(datetime.timedelta(hours=3))
current_moscow_time = datetime.datetime.now(tz=moscow_tz)