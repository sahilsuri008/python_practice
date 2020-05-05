#!/usr/bin/python

from time import localtime, strftime, mktime

start_time=localtime()
print ("Timer started at %s" % strftime("%X",start_time))

#wait for user input
raw_input("Press enter to continue")

stop_time=localtime()

difference = mktime(stop_time) - mktime(start_time)

print ("Timer stopped at %s" % strftime("%X",stop_time))
print ("Time difference is %s" % difference)
