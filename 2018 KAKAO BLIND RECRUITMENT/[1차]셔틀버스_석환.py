def solution(n, t, m, timetable):
    timetable = [time.split(':') for time in timetable]
    times, bus, ans = [], [], 0

    for time in timetable:
        times.append(int(time[0]) * 60 + int(time[1]))
    times.sort()

    bus_time = 540
    for i in range(n):
        if i == 0:
            bus.append(bus_time)
        else:
            bus_time += t
            bus.append(bus_time)

    while bus:
        customers = []
        if len(bus) > 1:
            for time in times:
                if time <= bus[0] and len(customers) < m:
                    customers.append(times.index(time))
        else:
            for time in times:
                if time <= bus[0] and len(customers) < m-1:
                    customers.append(times.index(time))
                    if bus[0] > time:
                        ans = bus[0]
                    else:
                        ans = time
                elif time <= bus[0] and len(customers) == m-1:
                    ans = time-1
                    break
                else:
                    ans = bus[0]
                    break
            break
        bus.pop(0)
        for cus in customers:
            times.pop(cus)
    hour = str(int(ans/60))
    minute = str(int(ans%60))
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    ans = hour + ':' + minute

    return ans

print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))
print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,1,1,["23:59"]))
print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))