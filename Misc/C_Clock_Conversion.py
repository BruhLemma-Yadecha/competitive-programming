t = int(input())
for _ in range(t):
    time = input()
    hour = time[:2]
    AM = True
    if hour == '00':
        hour = '12'
    elif hour[0] == '0':
        pass
    elif hour[0] == '1' and (hour[1] in ['0', '1']):
        pass
    elif hour == '12':
        AM = False
    else:
        AM = False
        hour = int(hour) - 12
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
    print(hour + ':' + time[3:] + (' AM' if AM else ' PM'))