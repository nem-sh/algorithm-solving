def check(play, adv, adv_logs):
    if play == adv:
        return 0
    for i in range(1,len(adv_logs)):
        adv_logs[i] += adv_logs[i-1]

    for i in range(1,len(adv_logs)):
        adv_logs[i] += adv_logs[i-1]

    mostview, maxtime = 0, 0
    for i in range(adv,play):
        if mostview < adv_logs[i] - adv_logs[i-adv]:
            mostview = adv_logs[i] - adv_logs[i-adv]
            maxtime = i - adv + 1

    # 이게 멀까...
    if mostview <= adv_logs[adv-1]:
        maxtime = 0

    return maxtime

def solution(play_time, adv_time, logs):
    play_h, play_m, play_s = play_time.split(':')
    adv_h, adv_m, adv_s = adv_time.split(':')

    play_time = int(play_h) * 3600 + int(play_m) * 60 + int(play_s)
    adv_time = int(adv_h)*3600 + int(adv_m)*60 + int(adv_s)

    adv_logs = [0 for _ in range(play_time+1)]

    for i in range(len(logs)):
        st, ed = logs[i].split('-')
        st_h, st_m, st_s = st.split(':')
        ed_h, ed_m, ed_s = ed.split(':')

        st = int(st_h)*3600 + int(st_m)*60 + int(st_s)
        ed = int(ed_h)*3600 + int(ed_m)*60 + int(ed_s)

        logs[i] = (st,ed)
        adv_logs[st] += 1
        adv_logs[ed] -= 1

    time = check(play_time, adv_time, adv_logs)

    time_h = str(int(time / 3600))
    time_m = str(int(time % 3600 / 60))
    time_s = str(int(time % 60))

    if len(time_h) == 1:
        time_h = '0' + time_h
    if len(time_m) == 1:
        time_m = '0' + time_m
    if len(time_s) == 1:
        time_s = '0' + time_s
    time = time_h + ':' + time_m + ':' + time_s

    return time

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))