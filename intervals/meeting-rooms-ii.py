# leetcode
# microsoft
# https://www.youtube.com/watch?v=qx7Akat3xrM

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1
"""

import heapq

# Solution 1:
# Time Complexity:
# Space Complexity:
def find_possibility1(input):

    input.sort(key=lambda x:x[0])
    heap = [input[0][1]]
    for start, end in input[1:]:
        if start > heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)

    return len(heap)

if __name__ == '__main__':
    input1 = [[0,30],[5,10],[15,20]] #2
    input2 = [[7,10],[2,4]] #1

    result = find_possibility1(input2)
    print(result)