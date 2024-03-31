import codewars_test as test
MORSE_CODE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': '`',
    '-.-.--': '!',
    '-..-.': '/',
    '-.--.': '(',
    '-.--.-': ')',
    '.-...': '&',
    '---...': ':',
    '-.-.-.': ';',
    '-...-': '=',
    '.-.-.': '+',
    '-....-': '-',
    '..--.-': '_',
    '.-..-.': '"',
    '...-..-': '$',
    '.--.-.': '@',
    '...-.-': 'End of work',
    '........': 'Error',
    '-.-.-': 'Starting Signal',
    '...-.': 'Understood',
    '...---...': 'SOS',
    '': ' ',
}

def decode_morse(morse_code: str) -> str:
    """
    In this kata you have to write a simple Morse code decoder.
    While the Morse code is now mostly superseded by voice and digital data communication channels,
     it still has its use in some applications around the world.
    The Morse code encodes every character as a sequence of "dots" and "dashes".
    For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−.
    The Morse code is case-insensitive, traditionally capital letters are used.
     When the message is written in Morse code, a single space is used to separate
     the character codes and 3 spaces are used to separate words.
     For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

    NOTE: Extra spaces before or after the code have no meaning and should be ignored.

    In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

    Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

    For example:

    decode_morse('.... . -.--   .--- ..- -.. .')
    #should return "HEY JUDE"
    NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

    :param morse_code:
    :return:
    """
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split(' ')) for word in morse_code.strip().split("   "))



@test.describe("Fixed tests")
def tests():
    @test.it("Should obtain correct decoding of Morse code from the description")
    def test_morse_hey_jude():
        test.assert_equals(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

    @test.it("Should obtain correct decoding of Morse code for basic examples")
    def test_morse_basic_examples():
        test.assert_equals(decode_morse('.-'), 'A')
        test.assert_equals(decode_morse('--...'), '7')
        test.assert_equals(decode_morse('...-..-'), '$')
        test.assert_equals(decode_morse('.'), 'E')
        test.assert_equals(decode_morse('..'), 'I')
        test.assert_equals(decode_morse('. .'), 'EE')
        test.assert_equals(decode_morse('.   .'), 'E E')
        test.assert_equals(decode_morse('...-..- ...-..- ...-..-'), '$$$')
        test.assert_equals(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
        test.assert_equals(decode_morse('.-... ---...   -..-. --...'), '&: /7')
        test.assert_equals(decode_morse('...---...'), 'SOS')
        test.assert_equals(decode_morse('... --- ...'), 'SOS')
        test.assert_equals(decode_morse('...   ---   ...'), 'S O S')

    @test.it("Should obtain correct decoding of Morse code for examples with extra spaces")
    def test_morse_basic_examples_with_extra_spaces():
        test.assert_equals(decode_morse(' . '), 'E')
        test.assert_equals(decode_morse('   .   . '), 'E E')

    @test.it(
        "Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
    def test_morse_complex_example():
        test.assert_equals(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
                           'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')