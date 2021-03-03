def get_second(string_time):
    (H, M, S) = string_time.split(":")
    second = float(H) * 60 * 60 + float(M) * 60 + float(S)
    return second


def get_time(second):
    S = str(int(second % (60)))
    second //= 60
    M = str(int(second % 60))
    H = str(int(second // 60))
    return H.zfill(2)+":"+M.zfill(2)+":"+S.zfill(2)


def get_log_to_time(log, times):
    (str_time, end_time) = log.split("-")
    str_second = get_second(str_time)
    times.append((str_second, True))
    end_second = get_second(end_time)
    times.append((end_second, False))


def get_timeline(times, play_time):
    cur_count = 0
    cur_time = 0
    times_idx = 0
    timeline = []

    while(times_idx < len(times)):

        time, is_str = times[times_idx]

        if time != cur_time:

            timeline.append((cur_time, cur_count))
            cur_time = time

        if is_str:

            cur_count += 1

        else:

            cur_count -= 1

        times_idx += 1
    last_time = times[times_idx-1][0]
    timeline.append((last_time, cur_count))
    timeline.append((get_second(play_time)+1, cur_count))
    return timeline


def search_best_time(play_time, adv_time, timeline):
    adv_second = get_second(adv_time)
    play_second = get_second(play_time)
    best_time = 0
    max_adv_value = 0
    adv_temp_back_idx = 0
    adv_temp_total_second = 0
    adv_temp_total_value = 0
    for adv_temp_front_idx in range(len(timeline)):

        while adv_temp_back_idx < len(timeline)-1:
            adv_temp_back_idx += 1
            if(adv_temp_total_second + timeline[adv_temp_back_idx][0] - timeline[adv_temp_back_idx-1][0] < adv_second):
                adv_temp_total_second += timeline[adv_temp_back_idx][0] - \
                    timeline[adv_temp_back_idx-1][0]
                adv_temp_total_value += (timeline[adv_temp_back_idx][0] -
                                         timeline[adv_temp_back_idx-1][0]) * timeline[adv_temp_back_idx-1][1]
            else:
                if adv_temp_front_idx > 0 and adv_second-adv_temp_total_second <= timeline[adv_temp_front_idx][0]-timeline[adv_temp_front_idx-1][0] and max_adv_value < adv_temp_total_value + ((adv_second-adv_temp_total_second) * timeline[adv_temp_front_idx-1][1]):
                    max_adv_value = adv_temp_total_value + \
                        ((adv_second-adv_temp_total_second)
                         * timeline[adv_temp_front_idx-1][1])
                    best_time = timeline[adv_temp_front_idx][0] - \
                        (adv_second-adv_temp_total_second)
                if adv_second-adv_temp_total_second <= timeline[adv_temp_back_idx][0]-timeline[adv_temp_back_idx-1][0] and max_adv_value < adv_temp_total_value + ((adv_second-adv_temp_total_second) * timeline[adv_temp_back_idx-1][1]):
                    max_adv_value = adv_temp_total_value + \
                        ((adv_second-adv_temp_total_second)
                         * timeline[adv_temp_back_idx-1][1])
                    best_time = timeline[adv_temp_front_idx][0]
                adv_temp_back_idx -= 1
                break
        if len(timeline) < adv_temp_front_idx+2:
            break
        adv_temp_total_second -= (timeline[adv_temp_front_idx+1]
                                  [0]-timeline[adv_temp_front_idx][0])
        adv_temp_total_value -= (timeline[adv_temp_front_idx+1][0] -
                                 timeline[adv_temp_front_idx][0]) * timeline[adv_temp_front_idx][1]
    return get_time(best_time)


def solution(play_time, adv_time, logs):

    times = []

    for log in logs:

        get_log_to_time(log, times)

    times.sort(key=lambda time: time[0])

    timeline = get_timeline(times, play_time)

    answer = search_best_time(play_time, adv_time, timeline)
    return answer


# solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00",
#                                   "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])


# solution("99:59:59", "25:00:00", [
#          "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
print(solution("00:00:10", "00:00:09", [
    "00:00:02-00:00:10"]))
