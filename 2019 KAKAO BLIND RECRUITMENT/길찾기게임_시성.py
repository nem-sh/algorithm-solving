import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    nodeinfo = [(idx+1, nodeinfo[idx][0], nodeinfo[idx][1])
                for idx in range(len(nodeinfo))]
    nodeinfo.sort(key=lambda info: info[2], reverse=True)

    node_list = [[]]
    cur_idx = 0
    cur_y = nodeinfo[0][2]
    for info in nodeinfo:
        num, x, y = info
        if cur_y == y:
            node_list[cur_idx].append([info, None, None, None])
        else:
            node_list[cur_idx].sort(key=lambda info: info[0][1])
            node_list.append([[info, None, None, None]])
            cur_idx += 1
            cur_y = y
    node_list[cur_idx].sort(key=lambda info: info[0][1])

    node_list[0][0][3] = node_list[0][0][0][1]
    for i in range(len(node_list)-1):
        ii = 0
        parent_info = node_list[i][ii][0]
        grand_parent_x = node_list[i][ii][3]
        for j in range(len(node_list[i+1])):

            num, x, y = node_list[i+1][j][0]

            while 1:
                parent_x = parent_info[1]
                if x < parent_x:
                    node_list[i][ii][1] = node_list[i+1][j]
                    node_list[i+1][j][3] = parent_x
                    break
                else:
                    if ii == len(node_list[i]) - 1:
                        node_list[i][ii][2] = node_list[i+1][j]
                        node_list[i+1][j][3] = grand_parent_x
                        break

                    if grand_parent_x == None or x < grand_parent_x:
                        node_list[i][ii][2] = node_list[i+1][j]
                        node_list[i+1][j][3] = grand_parent_x
                        break
                    else:
                        ii += 1
                        parent_info = node_list[i][ii][0]
                        parent_x = parent_info[1]
                        grand_parent_x = node_list[i][ii][3]
    front = []
    back = []

    def dfs(node):
        if node == None:
            return

        front.append(node[0][0])
        dfs(node[1])
        dfs(node[2])
        back.append(node[0][0])
    dfs(node_list[0][0])
    answer = [front, back]
    return answer
