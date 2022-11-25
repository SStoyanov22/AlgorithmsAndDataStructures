"""
Implement list_flatten(input_list) function – given a list nested lists as input,
write a function that returns a list after removing all the nested lists
"""


def list_flatten(input_list):
    """
    A pure Python implementation of list flatten algorithm
    :param input_list: some nested lists
    :return: flatten collection containing all the elements of the nested lists in the same order
    Examples:
    >>> list_flatten([1, 2, [3, 4, [5, 6]], 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> list_flatten([[], [[]]])
    []
    >>> list_flatten([[[1]]])
    [1]
    >>> list_flatten([[100, 99, 97],[1, 2, 3]])
    [100, 99, 97, 1, 2, 3]
    >>> list_flatten([[100,99],[1,2,3,[5,6,[8]]]])
    [100, 99, 1, 2, 3, 5, 6, 8]
    """

    def flatten(collection):
        for i in collection:
            if isinstance(i, list):
                yield from list_flatten(i)
            else:
                yield i

    return list(flatten(input_list))


if __name__ == "__main__":
    from doctest import testmod

    testmod()

print(list_flatten([1, 2, [3, 4, [5, 6]], 7]))
print(list_flatten([[], [[]]]))
print(list_flatten([[[1]]]))
print(list_flatten([[100, 99, 97], [1, 2, 3]]))
print(list_flatten([[100, 99], [1, 2, 3, [5, 6, [8]]]]))
