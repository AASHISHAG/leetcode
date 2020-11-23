# https://www.geeksforgeeks.org/maximum-sum-of-two-elements-whose-digit-sum-is-equal/
# microsoft codility

import sys
from collections import defaultdict

# Time Complexity: O(N)
# Space Complexity: O(N)
def find_numbers(nums):
    map = defaultdict(list)
    max_sum = -sys.maxsize
    for num in nums:
        sum_num = [int(x) for x in str(num)]
        sum_num = sum(sum_num)
        
        if sum_num in map:
            max_sum = max(max_sum, sum_num)

        map[sum_num].append(num)

    return map[max_sum]

if __name__ == '__main__':
    nums = [55, 23, 32, 88, 46]
    nums = find_numbers(nums)
    
    print(nums)
    