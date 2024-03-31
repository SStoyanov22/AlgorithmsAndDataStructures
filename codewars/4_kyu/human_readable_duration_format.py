"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
"""
import codewars_test as test
def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        times = {
            "year": int(seconds/(365 * 60 * 60 * 24)),
            "day": int(seconds % (365 * 60 * 60 * 24) / (60 * 60 * 24)),
            "hour": int(seconds % (60 * 60 * 24) / (60 * 60)),
            "minute": int(seconds % (60 * 60) / 60),
            "second": int(seconds % 60),
        }
        chunks=[]
        for name, qty in times.items():
            if qty:
                if qty>1:
                    name+='s'
                chunks.append(str(qty) + " " + name)
    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(format_duration(0), "now")
        test.assert_equals(format_duration(1), "1 second")
        test.assert_equals(format_duration(62), "1 minute and 2 seconds")
        test.assert_equals(format_duration(120), "2 minutes")
        test.assert_equals(format_duration(3600), "1 hour")
        test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
        test.assert_equals(format_duration(15731080), "182 days, 1 hour, 44 minutes and 40 seconds")
        test.assert_equals(format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes")
        test.assert_equals(format_duration(205851834), "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
        test.assert_equals(format_duration(253374061), "8 years, 12 days, 13 hours, 41 minutes and 1 second")
        test.assert_equals(format_duration(242062374), "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
        test.assert_equals(format_duration(101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
        test.assert_equals(format_duration(33243586), "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
