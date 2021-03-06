# leetcode
# microsoft
# https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms

"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
determine if a person could attend all meetings.

Input: [[0,30],[5,10],[15,20]]
Output: False

Input: [[7,10],[2,4]]
Output: True
"""


# Time Complexity: O(N)
# Space Complexity: O(1)
def find_possibility(input):
    slot = [0]*59

    for start, end in input:
        if sum(slot[start:end+1]) > 0:
            return False
        else:
            slot[start:end+1] = [1]*(end+1-start)
    return True       

if __name__ == '__main__':
    input1 = [[0,30],[5,10],[15,20]]
    input2 = [[7,10],[2,4]]

    result = find_possibility(input2)
    print(result)