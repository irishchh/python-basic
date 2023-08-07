import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now()



now = current_time.strftime("%H,%M,%S")

print(current_date, now)