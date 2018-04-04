import calendar

year = input('Year: ')
month = input('Month (num): ')

start_day = calendar.TextCalendar(calendar.SUNDAY)
# cal = calendar.month(int(year), int(month))
cal = start_day.formatmonth(int(year), int(month))
print(cal)
