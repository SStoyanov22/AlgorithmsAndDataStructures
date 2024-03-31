"""
    Given two positive integers n and p, we want to find a positive integer k,
    if it exists, such that the sum of the digits of n raised to consecutive
    powers starting from p is equal to k * n.
    :param n:
    :param p:
    :return:
"""
import codewars_test as test
def dig_pow(n, p):

    sum = 0
    for i, c in enumerate(str(n)):
        sum += pow(int(c), p + i)
    return sum/n if sum%n==0 else -1

@test.describe("Fixed tests")
def fixed_test():
    @test.it("Samples")
    def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
        test.assert_equals(dig_pow(41, 5), 25)
        test.assert_equals(dig_pow(114, 3), 9)
        test.assert_equals(dig_pow(8, 3), 64)