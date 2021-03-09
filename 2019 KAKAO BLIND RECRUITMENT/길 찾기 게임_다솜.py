import sys

sys.setrecursionlimit(10 ** 6)


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


pre, post = [], []


def preorder(node, nodeinfo):
    pre.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)


def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)
    if node.right:
        postorder(node.right, nodeinfo)
    post.append(nodeinfo.index(node.data) + 1)


def solution(nodeinfo):
    answer = []
    sort_node = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    root = None
    for node in sort_node:
        if not root:
            root = Tree(node)
        else:
            cur = root
            while 1:
                if node[0] < cur.data[0]:
                    if cur.left:
                        cur = cur.left
                        continue
                    else:
                        cur.left = Tree(node)
                        break
                if node[0] > cur.data[0]:
                    if cur.right:
                        cur = cur.right
                        continue
                    else:
                        cur.right = Tree(node)
                        break
                break
    preorder(root, nodeinfo)
    postorder(root, nodeinfo)
    answer.append(pre)
    answer.append(post)
    return answer
