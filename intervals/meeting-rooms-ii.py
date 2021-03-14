# leetcode
# microsoft
# https://medium.com/@edward.zhou/leetcode-253-meeting-rooms-ii-explained-python3-solution-3f8869612df

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1
"""

# Solution 1:
# Time Complexity:
# Space Complexity:
def find_possibility1(input):

    input.sort(key=lambda x:x[0])
    rooms = 0
    for index, (start, end) in enumerate(input[1:]):

        slot = end - start
        if start < input[index]:
            rooms += 1



if __name__ == '__main__':
    input1 = [[0,30],[5,10],[15,20]]
    input2 = [[7,10],[2,4]]

    result = find_possibility1(input1)
    print(result)