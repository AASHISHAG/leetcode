# leetcode
# microsoft
# https://www.youtube.com/watch?v=qx7Akat3xrM
# https://leetcode.com/problems/meeting-rooms-ii/

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
    hq = []
    heapq.heappush(hq, intervals[0][1])
    
    for start, end in input[1:]:
        if start >= hq[0]:
            heapq.heappop(hq)        
        heapq.heappush(hq, end)

    return len(hq)

# Time Complexity: O(Nlog N)
# Space Complexity: O(N)
def find_possibility1(input):
    
    starts, ends = [], []
    for start, end in input:
        starts.append(start)
        ends.append(end)

    starts.sort()
    ends.sort()
    
    rooms, index_end = 0, 0
    for start in starts:
        if start < ends[index_end]: rooms += 1
        else: index_end += 1
            
    return rooms
                

if __name__ == '__main__':
    input1 = [[0,30],[5,10],[15,20]] #2
    input2 = [[7,10],[2,4]] #1

    result = find_possibility1(input2)
    print(result)
