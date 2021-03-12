import time, datetime
import os


#Display time in seconds
print(f"Time in seconds:  {int(time.time())}" )

#Create a time
current_time = datetime.time(hour = 9, minute = 13)

print("Current time: ")
print(current_time.strftime("%X"))

#System time in string representation
print("System time in string representation:")
print(time.ctime())
print(time.asctime())

#Construct a date 
date_obj = datetime.date(1999, 3, 12)

print("date_obj: ")
print(date_obj.ctime())

#Displaying time in different timezones

os.environ['TZ'] = 'US/Eastern'
time.tzset()
print("Current time in US/Eastern: ")
print(time.ctime())


#Change timezone to Japan/Tokyo
os.environ['TZ'] = 'Japan/Tokyo'
time.tzset()
print("Current time in Japan/Tokyo timezone: ")
print(time.ctime())

#Construct time 
time_obj = datetime.time(9, 26, 0, 600)
print("Constructed time_obj: ")
print(time_obj.strftime("%H:%M:%S"))

