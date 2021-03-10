
def solution(words, queries):

    answer = []

    class Node:
        def __init__(self, character, count):
            self.character = character
            self.count = count
            self.next = dict()

    front = [Node(None, 0) for _ in range(100001)]
    back = [Node(None, 0) for _ in range(100001)]
    for word in words:
        cur_node = front[len(word)]
        for i in range(len(word)):
            character = word[i]
            cur_node.count += 1
            if not character in cur_node.next:
                cur_node.next[character] = Node(character, 0)
            cur_node = cur_node.next[character]
        cur_node = back[len(word)]
        for i in range(len(word)-1, -1, -1):
            character = word[i]
            cur_node.count += 1
            if not character in cur_node.next:
                cur_node.next[character] = Node(character, 0)
            cur_node = cur_node.next[character]

    def search(cur_node, idx, query, direction):

        while cur_node:
            if cur_node.count == 0 or (idx == 0 and direction == -1) or (idx == len(query)-1 and direction == 1) or query[idx] == "?":
                return cur_node.count
            if not query[idx] in cur_node.next:
                return 0
            cur_node = cur_node.next[query[idx]]
            idx += direction

    for query in queries:
        if query[0] == "?":
            answer.append(search(back[len(query)], len(query)-1, query, -1))
        else:

            answer.append(search(front[len(query)], 0, query, 1))

    return answer
