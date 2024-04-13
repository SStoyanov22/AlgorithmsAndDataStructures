"""
From wikipedia https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition.

For example, 4 can be partitioned in five distinct ways:

4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1.

We can write:

enum(4) -> [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]] and

enum(5) -> [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]].

The number of parts in a partition grows very fast. For n = 50 number of parts is 204226, for 80 it is 15,796,476 It would be too long to tests answers with arrays of such size. So our task is the following:

1 - n being given (n integer, 1 <= n <= 50) calculate enum(n) ie the partition of n. We will obtain something like that:
enum(n) -> [[n],[n-1,1],[n-2,2],...,[1,1,...,1]] (order of array and sub-arrays doesn't matter). This part is not tested.

2 - For each sub-array of enum(n) calculate its product. If n = 5 we'll obtain after removing duplicates and sorting:

prod(5) -> [1,2,3,4,5,6]

prod(8) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18]

If n = 40 prod(n) has a length of 2699 hence the tests will not verify such arrays. Instead our task number 3 is:

3 - return the range, the average and the median of prod(n) in the following form (example for n = 5):

"Range: 5 Average: 3.50 Median: 3.50"

Range is an integer, Average and Median are float numbers rounded to two decimal places (".2f" in some languages).

Notes:
Range : difference between the highest and lowest values.

Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.

Median : The median is the number separating the higher half of a data sample from the lower half. (https://en.wikipedia.org/wiki/Median)

Hints:
Try to optimize your program to avoid timing out.

Memoization can be helpful but it is not mandatory for being successful.
"""
import codewars_test as test
from functools import reduce
import statistics
def part(n):
    # Initialize a list to store the partitions
    partition_list = [[] for _ in range(n + 1)]
    partition_list[0] = [[]]  # Base case: empty partition

    # Iterate over all integers from 1 to n
    for i in range(1, n + 1):
        # Iterate over all possible partition sizes j
        for j in range(1, i + 1):
            # Generate partitions for the current integer using previous partitions
            for partition in partition_list[i - j]:
                if not partition or j <= partition[-1]:
                    partition_list[i].append(partition + [j])
    prod = set([reduce(lambda x, y: x * y, arr) for arr in partition_list[n]])
    mx = max(prod)
    mn = min(prod)
    rng = mx-mn
    avg = "{:.2f}".format(statistics.mean(prod))
    med = "{:.2f}".format(statistics.median(prod))
    return f"Range: {rng} Average: {avg} Median: {med}"

def doTest(n, expected):
    test.assert_equals(part(n), expected)


def doBatch(title, data):
    @test.it(title)
    def _():
        for n,exp in data: doTest(n,exp)

@test.describe("Testing...")
def _():
    doBatch("Small numbers", [
        [1, "Range: 0 Average: 1.00 Median: 1.00"],
        [2, "Range: 1 Average: 1.50 Median: 1.50"],
        [3, "Range: 2 Average: 2.00 Median: 2.00"],
        [4, "Range: 3 Average: 2.50 Median: 2.50"],
        [5, "Range: 5 Average: 3.50 Median: 3.50"],
        [6, "Range: 8 Average: 4.75 Median: 4.50"],
        [7, "Range: 11 Average: 6.09 Median: 6.00"],
        [8, "Range: 17 Average: 8.29 Median: 7.50"],
        [9, "Range: 26 Average: 11.17 Median: 9.50"],
        [10, "Range: 35 Average: 15.00 Median: 14.00"],
    ])