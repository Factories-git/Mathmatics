n, m = map(int, input().split())
time_percent = 24 * (((m / n) * 100) / 100)
time = int(time_percent)
minute = int((time_percent - time) * 60)
if 0 <= minute <= 9:
    minute = '0' + str(minute)
if 0 <= time <= 9:
    time = '0' + str(time)
print(f'{time}:{minute}')