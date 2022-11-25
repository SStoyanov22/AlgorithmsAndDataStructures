"""
https://www.hackerrank.com/challenges/abbr/problem
You can perform the following operation on some string, :
1. Capitalize zero or more of 's lowercase letters at some index i
   (i.e., make them uppercase).
2. Delete all of the remaining lowercase letters in .
Example:
a=daBcd and b="ABC"
daBcd -> capitalize a and c(dABCd) -> remove d (ABC)
"""


def abbreviation():
    """
       >>> abbreviation("daBcd", "ABC")
       True
       >>> abbreviation("dBcd", "ABC")
       False
       """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
