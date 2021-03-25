def solution(play_time, adv_time, logs):
    answer = ''

    H, M, S = play_time.split(':')
    play_second = int(H) * 60 * 60 + int(M) * 60 + int(S)

    H, M, S = adv_time.split(':')
    adv_second = int(H) * 60 * 60 + int(M) * 60 + int(S)

    play_list = [0] * (play_second + 1)

    for log in logs:
        start, end = log.split('-')

        H, M, S = start.split(':')
        start = int(H) * 60 * 60 + int(M) * 60 + int(S)

        H, M, S = end.split(':')
        end = int(H) * 60 * 60 + int(M) * 60 + int(S)

        play_list[start] += 1
        play_list[end] -= 1

    for second in range(1, play_second+1):
        play_list[second] += play_list[second - 1]

    value = 0
    for second in range(adv_second):
        value += play_list[second]

    max_value = value
    max_second = 0

    for second in range(play_second - adv_second):
        value -= play_list[second]
        value += play_list[second + adv_second]
        if value > max_value:
            max_value = value
            max_second = second + 1

    H = str(max_second // 3600)
    M = str((max_second % 3600) // 60)
    S = str((max_second % 3600) % 60)
    answer = H.zfill(2)+":"+M.zfill(2)+":"+S.zfill(2)
    return answer
