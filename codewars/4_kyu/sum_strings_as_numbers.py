import codewars_test as test
def sum_strings(x, y):
    if x =="" and y=="":
        return "0"
    if x == '0' or x=='':
        return y
    if y == '0' or y =='':
        return x
    x_reversed = x.lstrip('0')[::-1]
    y_reversed = y.lstrip('0')[::-1]
    index = 0
    reminder = 0
    answer = []
    while index<len(x_reversed) or index<len(y_reversed):
        a=int(x_reversed[index]) if index<len(x_reversed) else 0
        b=int(y_reversed[index]) if index<len(y_reversed) else 0
        s = a+b+reminder
        answer.append(str(s%10))
        reminder = int(s/10)
        index+=1
    if reminder!=0:
        answer.append(str(reminder))
    return ''.join(answer[::-1])

@test.describe('Basic tests')
def test_examples():
    @test.it('Example tests')
    def basic_tests():
        test.assert_equals(sum_strings("1", "1"), "2")
        test.assert_equals(sum_strings("123", "456"), "579")
        test.assert_equals(sum_strings("0", "8670"), "8670")
        test.assert_equals(sum_strings("0", ""), "0")
        test.assert_equals(sum_strings("", ""), "0")
