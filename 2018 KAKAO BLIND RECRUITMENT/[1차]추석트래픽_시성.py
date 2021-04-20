def get_time(line,str_times,end_times):

    (day, S, T)  = line.split(" ")
    (hh,mm,ss) = S.split(":")
    second = float(hh) * 60 * 60 + float(mm) * 60 + float(ss)
    str_times.append(second-float(T[:-1]))
    end_times.append(second)

def search_max_traffic(str_times, end_times):

    cur_count = 0
    max_count = 0
    end_idx = 0

    for str_idx in range(len(str_times)):

        str_time = str_times[str_idx]
        end_time = end_times[end_idx]
        cur_count += 1

        while(end_time + 0.999 <= str_time):

            end_idx +=1
            end_time = end_times[end_idx]
            cur_count -=1

        max_count = max(max_count, cur_count)

    return max_count
        

def solution(lines):

    str_times = []
    end_times = []

    for line in lines:
        get_time(line, str_times, end_times)

    str_times.sort()
    answer = search_max_traffic(str_times,end_times)

    return answer


print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution( [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))