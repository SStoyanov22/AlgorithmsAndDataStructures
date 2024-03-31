"""
Write a function that, given a string of text (possibly with punctuation and line-breaks),
 returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned,
 or an empty array if a text contains no words.
"""
import codewars_test as test
import re
def top_3_words(text):
    words = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
    word_counts = {word: words.count(word) for word in set(words)}
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_counts[:3]]

@test.describe("Top 3 words")
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
        test.assert_equals(top_3_words("  , e   .. "), ["e"])
        test.assert_equals(top_3_words("  ...  "), [])
        test.assert_equals(top_3_words("  '  "), [])
        test.assert_equals(top_3_words("  '''  "), [])
        test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])