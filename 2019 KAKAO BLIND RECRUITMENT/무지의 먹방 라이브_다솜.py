import heapq


def solution(food_times, k):
    food_times = [(food, i) for i, food in enumerate(food_times, 1)]
    heapq.heapify(food_times)
    small, tmp = food_times[0][0], 0
    while (small - tmp) * len(food_times) <= k:
        k -= (small - tmp) * len(food_times)
        tmp, idx = heapq.heappop(food_times)
        if not food_times:
            return -1
        small = food_times[0][0]
    food_times = sorted(food_times, key=lambda x: x[1])
    return food_times[k % len(food_times)][1]
