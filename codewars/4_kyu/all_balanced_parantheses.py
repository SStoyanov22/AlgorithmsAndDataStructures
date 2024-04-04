"""
Write a function which makes a list of strings representing
 all of the ways you can balance n pairs of parentheses
"""
import codewars_test as test
def balanced_parens(n):
    result = []
    generateParenthesisRecu(result, "", n, n)
    return result

def generateParenthesisRecu(result, current, left, right):
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        generateParenthesisRecu(result, current + "(", left - 1, right)
    if left < right:
        generateParenthesisRecu(result, current + ")", left, right - 1)
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def ff():
        for n,exp in [ [0, [""]],
                       [1, ["()"]],
                       [2, ["(())","()()"]],
                       [3, ["((()))","(()())","(())()","()(())","()()()"]]]:
            actual = balanced_parens(n)
            actual.sort()
            test.assert_equals(actual, exp)