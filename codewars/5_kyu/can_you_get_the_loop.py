"""
You are given a node that is the beginning of a linked list.
This list contains a dangling piece and a loop.
Your objective is to determine the length of the loop.
"""
import codewars_test as test
from data_structures.linked_list.linked_list import Node

def loop_size(node):
    nodes = []
    while node not in nodes:
        nodes.append(node)
        node = node.next
    return len(nodes) - max(0, nodes.index(node))

@test('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        test.assert_equals(loop_size(node1), 3, 'Loop size of 3 expected')
