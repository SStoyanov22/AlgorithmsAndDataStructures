"""
To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest.
Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system,
and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators,
 but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-),
 and multiplication (*), so those are the only ones that will appear. Each number will be in the range
  from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
  If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator,
   and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one
    of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0,
    therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works,
 give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his
  runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a
 paramater repressenting the expression and will return an int value representing the unknown rune or -1
 if no such rune exists.
"""
import codewars_test as test
import re
def solve_runes(runes):
    used_digits = set(re.findall(r'\d', runes))
    tokenized_equation =  tokenize_equation(runes)
    for i in range(0,10):
        if i ==0 and ((tokenized_equation[0][0]=='?'and len(tokenized_equation[0])>1 )or
                      (tokenized_equation[2][0]=='?' and len(tokenized_equation[2])>1 ) or
                      (tokenized_equation[4][0]=='?'and len(tokenized_equation[4])>1) or
                      (tokenized_equation[0][0]=='-' and tokenized_equation[0][1]=='?') or
                      (tokenized_equation[2][0]=='-' and tokenized_equation[2][1]=='?') or
                      (tokenized_equation[2][0]=='-' and tokenized_equation[2][1]=='?')):
            continue
        if str(i) not in used_digits:
            first = tokenized_equation[0].replace('?',str(i))
            second = tokenized_equation[2].replace('?',str(i))
            result = tokenized_equation[4].replace('?',str(i))
            if tokenized_equation[1] =='*'and int(first) * int(second) == int(result):
                return i
            if tokenized_equation[1] =='+' and int(first) + int(second) == int(result):
                return i
            if tokenized_equation[1] =='-' and int(first) - int(second) == int(result):
                return i
    return -1
def tokenize_equation(equation):
    # Define regular expression pattern to match numbers (including ?), operators, and equals sign
    pattern = r'(-?[0-9\?]+)(\+|\-|\*|\/)(-?[0-9\?]+)(\=)(-?[0-9\?]+)'

    # Tokenize the equation using the regular expression pattern
    match = re.match(pattern, equation)

    return match.groups()
@test.describe('Find the unknown digit')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(solve_runes("?8?170-1?6256=7?2?14"), 9, "Answer for runes = '?8?170-1?6256=7?2?14' ")
        test.assert_equals(solve_runes("-5?*-1=5?"), 0, "Answer for runes = '-5?*-1=5?' ")
        test.assert_equals(solve_runes("1+1=?"), 2, "Answer for runes = '1+1=?' ")
        test.assert_equals(solve_runes("123*45?=5?088"), 6, "Answer for runes = '123*45?=5?088' ")
        test.assert_equals(solve_runes("19--45=5?"), -1, "Answer for runes = '19--45=5?' ")
        test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for runes = '??*??=302?' ")
        test.assert_equals(solve_runes("?*11=??"), 2, "Answer for runes = '?*11=??' ")
        test.assert_equals(solve_runes("??*1=??"), 2, "Answer for runes = '??*1=??' ")