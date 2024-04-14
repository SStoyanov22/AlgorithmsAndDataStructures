"""
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own,
 to enjoy the process --myjinxin2015 said

Description:
There is a infinite string. You can imagine it's a combination of numbers from 1 to n, like this:

"123456789101112131415....n-2n-1n"
Please note: the length of the string is infinite. It depends on how long you need it(I can't offer it as a argument,
 it only exists in your imagination) ;-)

Your task is complete function findPosition that accept a digital string num. Returns the position(index)
 of the digital string(the first appearance).

For example:

findPosition("456") == 3
because "123456789101112131415".indexOf("456") = 3
            ^^^
Is it simple? No, It is more difficult than you think ;-)

findPosition("454") = ?
Oh, no! There is no "454" in "123456789101112131415",
so we should return -1?
No, I said, this is a string of infinite length.
We need to increase the length of the string to find "454"

findPosition("454") == 79
because "123456789101112131415...44454647".indexOf("454")=79
                                   ^^^
The length of argument num is 2 to 15. So now there are two ways: one is to create a huge own string
 to find the index position; Or thinking about an algorithm to calculate the index position.

Which way would you choose? ;-)

Some examples:
 findPosition("456") == 3
 ("...3456...")
       ^^^
 findPosition("454") == 79
 ("...444546...")
        ^^^
 findPosition("455") == 98
 ("...545556...")
       ^^^
 findPosition("910") == 8
 ("...7891011...")
        ^^^
 findPosition("9100") == 188
 ("...9899100101...")
         ^^^^
 findPosition("99100") == 187
 ("...9899100101...")
        ^^^^^
 findPosition("00101") == 190
 ("...99100101...")
         ^^^^^
 findPosition("001") == 190
 ("...9899100101...")
           ^^^
 findPosition("123456789") == 0
 findPosition("1234567891") == 0
 findPosition("123456798") == 1000000071
A bit difficulty, A bit of fun, happy coding ;-)

"""
import codewars_test as test
def find_position(num):
    num = str(num)
    indexes = []

    for step in range(0, len(num) + 1):
        for start in range(0, step):
            index = try_to_parse(num, start, step)
            if index >= 0:
                indexes.append(index)

    if not len(indexes):
        # special case, for all is zero
        return int(get_total_length(int('1' + num)) + 1)

    return int(min(indexes))


def try_to_parse(num, start, step):
    # print("num=", num, "start=", start, "step=", step)
    if start + step <= len(num):
        n = int(num[start:(start+step)])
    else:
        # |----num----|
        # |-p2-|--p1--|
        p1 = num[start:]
        p2 = num[0:start]
        common = len(p1) + len(p2) - step

        # |---step----|
        # |-xx-|--p2--|, n - 1
        # |--p1--|-xx-|, n
        chs = p2[common:]
        if chs == '9' * len(chs):
            p1 += '0' * len(chs)
            n = int(p1)
        else:
            p1 = p1 + p2[common:]
            n = int(p1) + 1
        if str(n - 1)[(step - len(p2)):] != p2:
            return -1

    tokens = []
    lena = 0

    if start:
        prev = str(n - 1)
        tokens.append(prev[(len(prev) - start):])
        lena += start

    x = n
    while lena < len(num):
        stra = str(x)
        if len(stra) + lena > len(num):
            tokens.append(stra[0:(len(num) - lena)])
            lena += len(num) - lena
        else:
            tokens.append(stra)
            lena += len(stra)
        x += 1

    if ''.join(tokens) == num:
        total = get_total_length(n)
        return total - start
    else:
        return -1


def get_total_length(n):
    # not include n
    total = 0
    lena = 1
    x = 10

    while n > x:
        total += lena * (x - x / 10)
        x *= 10
        lena += 1

    total += lena * (n - x / 10)
    return total
@test.describe("Example tests")
def example_tests():
    @test.it("Should pass fixed tests")
    def should_pass_fixed_tests():
        test.assert_equals(find_position("456") , 3,"...3456...")
        test.assert_equals(find_position("454") , 79,"...444546...")
        test.assert_equals(find_position("455") , 98,"...545556...")
        test.assert_equals(find_position("910") , 8,"...7891011...")
        test.assert_equals(find_position("9100") , 188,"...9899100...")
        test.assert_equals(find_position("99100") , 187,"...9899100...")
        test.assert_equals(find_position("00101") , 190,"...9899100...")
        test.assert_equals(find_position("001") , 190,"...9899100...")
        test.assert_equals(find_position("00") , 190,"...9899100...")
        test.assert_equals(find_position("123456789") , 0)
        test.assert_equals(find_position("1234567891") , 0)
        test.assert_equals(find_position("123456798") , 1000000071)
        test.assert_equals(find_position("10") , 9)
        test.assert_equals(find_position("53635") , 13034)
        test.assert_equals(find_position("040") , 1091)
        test.assert_equals(find_position("11") , 11)
        test.assert_equals(find_position("99") , 168)
        test.assert_equals(find_position("667") , 122)
        test.assert_equals(find_position("0404") , 15050)
        test.assert_equals(find_position("949225100") , 382689688)
        test.assert_equals(find_position("58257860625") , 24674951477)
        test.assert_equals(find_position("3999589058124") , 6957586376885)
        test.assert_equals(find_position("555899959741198") , 1686722738828503)
        test.assert_equals(find_position("01") , 10)
        test.assert_equals(find_position("091") , 170)
        test.assert_equals(find_position("0910") , 2927)
        test.assert_equals(find_position("0991") , 2617)
        test.assert_equals(find_position("09910") , 2617)
        test.assert_equals(find_position("09991") , 35286)