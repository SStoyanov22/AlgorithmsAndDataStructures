"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
"""
import codewars_test as test
def solution(args):
    output = list()
    for i in len(args):
        if ranges.count()>0:
            if ranges[-1]+1==args[i]:
                ranges.append(i)
            else:
                if ranges.count()==1:
                    output.append(a)
                ranges=list()
            ranges.append(i)
        else:
            ranges.append(i)




@test.describe("Range extraction")
def desc1():

    @test.it("Sample Tests")
    def it1():
        test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
        test.assert_equals(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]), "-10--8,-6,-3-1,3-5,7-11,14,15,17-20")