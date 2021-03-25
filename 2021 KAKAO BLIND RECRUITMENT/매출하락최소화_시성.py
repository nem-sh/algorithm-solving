def dfs_search(team_leader, is_attend, dp, teams, sales):
    if dp[team_leader][is_attend] != -1:
        return dp[team_leader][is_attend]

    total_sales = 0
    if team_leader in teams:

        team = teams[team_leader]
    else:
        team = []
    if is_attend:
        total_sales += sales[team_leader-1]

        for team_member in team:
            total_sales += min(dfs_search(team_member, True, dp, teams, sales),
                               dfs_search(team_member, False, dp, teams, sales))

        dp[team_leader][is_attend] = total_sales
    else:
        attend_flag = False
        if len(team) == 0:
            attend_min_sales = 0
        else:
            attend_min_sales = float("inf")
        for team_member in team:
            attend_yes = dfs_search(team_member, True, dp, teams, sales)
            attend_no = dfs_search(team_member, False, dp, teams, sales)
            if attend_yes <= attend_no:
                attend_flag = True
            else:
                attend_min_sales = min(attend_min_sales, attend_yes-attend_no)
            total_sales += min(attend_yes, attend_no)

        if not attend_flag:
            total_sales += attend_min_sales

        dp[team_leader][is_attend] = total_sales

    return total_sales


def solution(sales, links):
    answer = 0
    teams = {}
    dp = [[-1 for _ in range(2)] for _ in range(len(sales)+1)]
    for link in links:
        team_leader, team_member = link
        if not team_leader in teams:
            teams[team_leader] = []
        teams[team_leader].append(team_member)

    answer = min(dfs_search(1, True, dp, teams, sales),
                 dfs_search(1, False, dp, teams, sales))
    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9],
                                                          [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
