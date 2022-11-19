"""
This is pure Python implementation of counting sort algorithm
For doctests run following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py
For manual testing run:
python counting_sort.py
"""


def counting_sort(collection):
    """Pure implementation of counting sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> counting_sort([5, 4, 3, 2, 1, 5, -1, -1])
    [-1, -1, 1, 2, 3, 4, 5, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # if the collection is empty, returns empty
    if not collection:
        return []
    coll_len = len(collection)
    coll_max = max(collection)
    coll_min = min(collection)

    # create the counting array
    count_arr_length = coll_max - coll_min + 1  # e.g. [5, 4, 3, 2, 1, 5, -1, -1] -> total pf 5 + 1 - (-2) = 8 elements
    count_arr = [0] * count_arr_length

    # count how much each element appears in the collection
    for number in collection:
        count_arr[number - coll_min] += 1

    # sum each position with its predecessor
    for i in range(1, count_arr_length):
        count_arr[i] = count_arr[i - 1] + count_arr[i]

    # create the output collection
    ordered = [0] * coll_len

    # place the elements in the output, respecting the original order
    for i in range(0, coll_len):
        index = collection[i] - coll_min
        ordered[count_arr[index] - 1] = collection[i]
        count_arr[index] -= 1

    return ordered


def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisthestring")
    'eghhiiinrsssttt'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


if __name__ == "__main__":
    # Test string sort
    assert "eghhiiinrsssttt" == counting_sort_string("thisisthestring")

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(counting_sort(unsorted))
