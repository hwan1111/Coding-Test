#길 찾기 게임

import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def add_node(root, new_node):
    if new_node.x < root.x:
        if root.left is None:
            root.left = new_node
        else:
            add_node(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            add_node(root.right, new_node)

def preorder(root, result):
    if root is not None:
        result[0].append(root.num)
        preorder(root.left, result)
        preorder(root.right, result)

def postorder(root, result):
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result[1].append(root.num)
    
def solution(nodeinfo):
    nodes = [Node(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key = lambda x: (-x.y, x.x))

    root = nodes[0]
    for node in nodes[1:]:
        add_node(root, node)
    
    result = [[], []]

    preorder(root, result)
    postorder(root, result)

    return result