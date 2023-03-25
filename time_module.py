"""The time.sleep() function suspends the execution of the current thread for a specified number of
 seconds. This function can be used to pause the program for a certain period of time, allowing other
  parts of the program to run, or to synchronize the execution of multiple threads. Here's an example:"""
#_______________________________________   time.sleep()  _____________________________________
import time

print(4)
time.sleep(3)
print("This is printed after 3 seconds")  # it will wait for 3 seconds then after that write the statement .



"""     ++++++++++++++++++++++++++   time.strftime()       +++++++++++++++++++++++++++++++++++++++
 
 
 
 As you can see, the function time.strftime() formats the current time (obtained using time.localtime()) 
as a string, using a specified format. The format string contains codes that represent different
parts of the time value, such as the year,the month, the day, the hour, the minute,
and the second."""


t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)

# ******************************      time.time()    ************************************
"""The time.time() function returns the current time as a floating-point number,
 representing the number of seconds since the epoch (the point in time when the time module was initialized). 
 The returned value is based on the computer's system clock and is affected by time adjustments made by the
  operating system, such as daylight saving time. Here's an example:  """


import time           # doubt 
def usingWhile():
     i = 0
     while i<500000:
       i = i +1
       print(i)
def usingFor():
     for i in range(500000):
       print(i)
init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

"""As you can see, the function returns the current time as a floating-point number, which can be used for 
various purposes, such as measuring the duration of an operation or the elapsed time since a 
certain point in time. """

