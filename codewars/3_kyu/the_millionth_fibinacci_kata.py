"""
The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him.
Gabriel thunders to the pope:

Gather all of the learned men in Pisa, especially Leonardo Fibonacci.
In order for the crusades in the holy lands to be successful,
these men must calculate the millionth number in Fibonacci's recurrence.
Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history,
he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus;
this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul),
but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision.
Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n)
if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.
"""

import codewars_test as test
from numpy import matrix
def fib(n):
    return (matrix(
        '1 1; 1 0' if n >= 0 else '1 -1; 1 0', object
        ) ** abs(n-1    ))[0, 0]

def small_positive_numbers():
    for n, result in [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)]:
        @test.it(f"fib({n}) == {result}")
        def _():
            actual = fib(n)
            test.assert_equals(actual, result)


@test.describe("Small negative numbers")
def small_negative_numbers():
    @test.it("fib(-1) == 1")
    def _():
        test.assert_equals(fib(-1), 1)

    @test.it("fib(-6) == -8")
    def _():
        test.assert_equals(fib(-6), -8)

    @test.it("fib(-96) == -51680708854858323072")
    def _():
        test.assert_equals(fib(-96), -51680708854858323072)


@test.describe("Large Numbers")
def large_numbers():
    @test.it("fib(-500)")
    def _():
        test.assert_equals(
            fib(-500),
            -139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        )

    @test.it("fib(1000)")
    def _():
        test.assert_equals(
            fib(1000),
            43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        )
