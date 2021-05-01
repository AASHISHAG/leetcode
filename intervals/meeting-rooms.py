# leetcode
# microsoft
# https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms
# https://leetcode.com/problems/meeting-rooms/

"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
determine if a person could attend all meetings.

Input: [[0,30],[5,10],[15,20]]
Output: False

Input: [[7,10],[2,4]]
Output: True
"""

# Solution 1:
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def find_possibility1(input):

    new_input = []
    for sub_list in input:
        new_input.extend(sub_list)
    max_input = max(new_input)

    slot = [0]*max_input

    for start, end in input:
        if sum(slot[start:end+1]) > 0:
            return False
        else:
            slot[start:end+1] = [1]*(end+1-start)
    return True


# Solution 2:
# Time Complexity: O(NlogN)
# Space Complexity: O(1)
# https://www.youtube.com/watch?v=aby3aYFjFT0
def find_possibility2(input):

    print(input)
    input.sort(key=lambda x: x[0])
    print(input)
    for index, (start, end) in enumerate(input[1:]):
        if start < input[index][1]:
            return False
    return True

if __name__ == '__main__':
    input1 = [[0,30],[5,10],[15,20]]
    input2 = [[7,10],[2,4]]

    result = find_possibility1(input2)
    print(result)
