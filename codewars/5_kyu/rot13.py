"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

"""
import codewars_test as test
def rot13(message):
    message_list = list(message)
    for i in range(len(message_list)):
        if message_list[i].isalpha():
            message_list[i] = replace_rot13(message_list[i])
    return ''.join(message_list)
def replace_rot13(s):
    return chr(ord(s) - 13) if ord(s.lower()) - ord('a') + 1 > 13 else chr(ord(s) + 13)


@test.describe("Fixed tests")
def tests():
    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(rot13('lYnDAy'), 'yLaQNl', 'Returned solution incorrect for fixed string = test')
        test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
                           'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')