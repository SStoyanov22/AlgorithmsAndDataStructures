"""
Your task is to sort a given string. Each word in the string will contain a single number.
 This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.


"""
import codewars_test as test
def order(sentence):
	if len(sentence)==0:
		return sentence
	else:
		words = sentence.strip().split(' ')
		ordered_sentence=[None]*len(words)
		for word in words:
			for char in word:
				if char.isdigit():
					ordered_sentence[int(char)-1] = word
					break
		return ' '.join(ordered_sentence)
@test.describe('Your order, please')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        test.assert_equals(order(""), "")