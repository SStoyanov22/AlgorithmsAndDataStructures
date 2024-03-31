def array_diff(arrA: list[int], arrB: list[int]) -> list[int]:
	"""
	    Your goal in this kata is to implement a difference function,
	     which subtracts one list from another and returns the result.

		It should remove all values from list a, which are present in list b keeping their order.
	    :param arrA: array of values
	           arrB: array of values
	    :return: array of values
	    Examples:
	    >>> array_diff([1,2],[1])
	    [2]
	    >>> array_diff([1,2,2,2,3],[2])
	    [1, 3]

	"""
	for b in arrB:
		arrA = [a for a in arrA if a!=b]
	return arrA

if __name__ == "__main__":
    import doctest

    doctest.testmod()