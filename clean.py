# this is mine
# class Calender:
#     def __init__(self, date,time):
#         self.date = date
#         self.time = time

#     def show_date(self):
#         print(f"today is \n{self.date}\nand its \n{self.time}'O' Clock")

# class Time:
#     def __init__(self,time):
#         self.time = time

#     def show_time(self):
#         print(f"its {self.time}")

# class Date(Calender,Time):
#     def __init__(self,date,time):
#         super(). __init__(date,time)
#         self.date = date
    

# def main():
#     d1 = Date("2023/7/27","8:00")
#     d1.show_date()
    

# if __name__ == "__main__":
#     main()



#this is sir

import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now()
now = datetime.strftime("%H:%M:%S")
print(current_date, now)
