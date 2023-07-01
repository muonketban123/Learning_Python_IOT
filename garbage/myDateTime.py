

from datetime import date

'''lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("today: ", date.today())
print("day: ", date.today().day)
print("thang: ", date.today().month)
print("nam: ", date.today().year)

print(lst[date.today().weekday()])'''



from datetime import datetime

'''print(datetime.now())
print("Giờ: ", datetime.now().hour)
print("Phút: ", datetime.now().minute)'''

'''now = datetime.now()

print(now.strftime("Năm : %Y"))
print(now.strftime("Tháng: %m"))
print(now.strftime("Ngày: %d"))'''

from datetime import timedelta

print("Thông tin của 1 khoảng thời gian sau : ")
print(datetime.now() + timedelta(days = 100, hours = 1, minutes= 50))


