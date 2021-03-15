# leetcode
# facebook
# https://leetcode.com/problems/merge-intervals/

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Solution:
# Time Complexity: O(NLogN)
# Space Complexity: O(N)


from typing import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    if len(intervals) == 0:
        return []

    intervals.sort(key=lambda x: x[0])

    index = 0
    merged_intervals = [intervals[0]]
    for start, end in intervals[1:]:

        if start <= merged_intervals[index][1]:
            end = max(merged_intervals[index][1], end)
            merged_intervals[index] = [merged_intervals[index][0], end]
        else:
            index += 1
            merged_intervals.append([start, end])
    return merged_intervals


if __name__ == '__main__':

    input1 = [[1,3],[2,6],[8,10],[15,18]] # [[1,6],[8,10],[15,18]]
    input2 = [[1,4],[4,5]] # [[1,5]]
    result = merge(input1)
    print(result)
