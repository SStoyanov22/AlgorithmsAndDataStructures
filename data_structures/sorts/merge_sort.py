"""
This is a pure Python implementation of the merge sort algorithm.
For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""


def merge_sort(collection: list) -> list:
    """
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> merge_sort([54,26,93,17,77,31,44,55,20])
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    if len(collection) > 1:
        mid = len(collection) // 2
        left = collection[:mid]
        right = collection[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                collection[k] = left[i]
                i += 1
            else:
                collection[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            collection[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            collection[k] = right[j]
            j += 1
            k += 1

    return collection


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
