import calendar
from datetime import datetime

datetime_object = datetime.now()
print(datetime_object)

week_num = calendar.weekday(2025,1,8)
week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(week_days[week_num])