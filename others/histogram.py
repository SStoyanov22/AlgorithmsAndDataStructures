"""
Implement histogram(input_list) function –
given a list of numbers as input write a function
that returns a dictionary with key as numbers and value as count of the numbers.
"""


def histogram(input_list):
    """
    A pure Python implementation of histogram algorithm
    :param input_list: some nested lists
    :return: map with list elements as key and their count as value
    Examples:
    >>> histogram([2, 4, 1, 2, 3, 2, 1])
    {2: 3, 4: 1, 1: 2, 3: 1}
    >>> histogram([2, 1, 3, 4, 2, 4, 3, 4])
    {2: 2, 1: 1, 3: 2, 4: 3}
    >>> histogram([1, 2, 3, 4])
    {1: 1, 2: 1, 3: 1, 4: 1}
    >>> histogram([])
    {}
    """
    output_map = dict.fromkeys(input_list)
    for i in output_map.keys():
        output_map[i] = input_list.count(i)
    return output_map


if __name__ == "__main__":
    from doctest import testmod

    testmod()

print(histogram([2, 4, 1, 2, 3, 2, 1]))
print(histogram([2, 1, 3, 4, 2, 4, 3, 4]))
print(histogram([1, 2, 3, 4]))
print(histogram([]))
