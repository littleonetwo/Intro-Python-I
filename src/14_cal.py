"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

calendar.Calendar(6)



if len(sys.argv) == 1:          #if they load the file by default there will be at least 1 arguments
  currTime = str(datetime.date(datetime.now()))       #we need the whole date before getting the month
  currMonth = int(currTime[5:7])
  currYear = int(currTime[0:4])

  print(calendar.month(currYear, currMonth))

elif len(sys.argv) == 2:
  currTime = str(datetime.date(datetime.now()))
  currMonth = int(sys.argv[1])
  currYear = int(currTime[0:4])

  print(calendar.month(currYear,currMonth))

elif len(sys.argv) == 3:

  currMonth = int(sys.argv[1])
  currYear = int(sys.argv[2])

  print(calendar.month(currYear,currMonth))

else:

  print("You are not using the correct format for this program.")
  print("You can call the program without any arguments for the current month or")
  print("you may provide the month or month and year to get specific calendars.")
  print("in this format: 14_cal.py [month] [year]")
