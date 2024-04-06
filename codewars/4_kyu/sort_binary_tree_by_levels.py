"""
You are given a binary tree
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.
"""
import codewars_test as test
from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def tree_by_levels(node):
    if node is None:
        return []
    visited = list()
    queue = deque([node])
    visited.append(node)
    while queue:
        current = queue.popleft()
        if current.left and current.left not in visited:
            visited.append(current.left)
            queue.append(current.left)
        if current.right and current.right not in visited:
            visited.append(current.right)
            queue.append(current.right)
    return [n.value for n in visited]


@test.describe('Find the unknown digit')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
        test.assert_equals(tree_by_levels(None), [])