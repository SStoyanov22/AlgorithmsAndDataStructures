

import codewars_test as test

def is_zero(element):
    return element==0
def move_zeros(lst):
    return sorted(lst, key=is_zero)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        test.assert_equals(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        test.assert_equals(move_zeros([0, 0]), [0, 0])
        test.assert_equals(move_zeros([0]), [0])
        test.assert_equals(move_zeros([]), [])