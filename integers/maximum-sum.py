# https://www.geeksforgeeks.org/maximum-sum-of-two-elements-whose-digit-sum-is-equal/
# microsoft codility

import sys
from collections import defaultdict

# Time Complexity: O(N)
# Space Complexity: O(N)
def find_numbers(nums):
    map = defaultdict(list)
    max_sum = -sys.maxsize
    digit_sum = 0
    for num in nums:
        sum_num = [int(x) for x in str(num)]
        sum_num = sum(sum_num)

        if sum_num in map:
            map[sum_num].append(num)
            if len(map[sum_num]) > 2:
                map[sum_num] = sorted(map[sum_num])[1:3]
            max_new = max(max_sum, sum(map[sum_num]))
            if max_new > max_sum:
                max_sum = max_new
                digit_sum = sum_num
        else:
            map[sum_num] = [num]
    return map[digit_sum], digit_sum, sum(map[digit_sum])

if __name__ == '__main__':
    nums1 = [55, 23, 32, 88, 46] # ([55, 46], 10, 101)
    nums2 = [51, 32, 42] # ([51, 42], 6, 93)
    nums3 = [51, 71, 17, 42] # ([51, 42], 6, 93)
    nums4 = [42, 33, 60] # ([42, 60], 6, 102)
    nums5 = [51, 32, 43] # ([], 0, 0)
    result = find_numbers(nums1)
    
    print(result)