"""
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incrementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
"""
import codewars_test as test

def is_incrementing(number):
    return str(number) in '1234567890'

def is_decrementing(number):
    return str(number) in '9876543210'

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_round(number):
    return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)

    for num, color in zip(range(number, number + 3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0

@test.describe("Car Mileage numbers")
def desc1():
    @test.it("Sample tests")
    def it1():
        tests = [
            {'n': 3, 'interesting': [1337, 256], 'expected': 0},
            {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
            {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
            {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
            {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
            {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
        ]
        for t in tests:
            test.assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])