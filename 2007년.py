import calendar

m,d = map(int, input().split())
weekdy = {0 : 'MON', 1 : 'TUE', 2 : 'WED', 3 : 'THU', 4 : 'FRI', 5 : 'SAT', 6 : 'SUN'}
print(weekdy[calendar.weekday(2007,m,d)])