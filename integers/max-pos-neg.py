# https://leetcode.com/discuss/interview-question/406031/
# microsoft codility

"""
Largest K such that both K and -K exist in array.
Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exist in array A. If there is no such integer, the 
function should return 0.

Example 1:

    Input: [3, 2, -2, 5, -3]
    Output: 3

Example 2:

    Input: [1, 2, 3, -4]
    Output: 0
"""

import sys

# Time Complexity: O(N)
# Space Complexity: O(N)
def get_max_pos_neg_num(input: list):

    input_uniq = set(input)
    max_flag = False
    max_num = -sys.maxsize
    for elem in input:
        if -1*elem in input_uniq:
            if abs(elem) > max_num:
                max_num = abs(elem)
                max_flag = True
    return max_num if max_flag else 0

# Time Complexity: O(NlogN)
# Space Complexity: O(1)
def get_max_pos_neg_num_approach_2(input: list):

    input = sorted(input)
    left, right = 0, len(input - 1)
    while left < right:
        if input[left] + input[right] == 0:
            return input[right]
        elif input[left] + input[right] > 0:
            right -= 1
        else:
            left += 1
    return 0

if __name__ == '__main__':

    input1 = [3, 2, -2, 5, -3]
    input2 = [1, 2, 3, -4]
    result = get_max_pos_neg_num(input1)
    print(result)


