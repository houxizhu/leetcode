"""
1005. Maximize Sum Of Array After K Negations
Easy
Topics
Companies
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.



Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].


Constraints:

1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int], k: int) -> int:
        ll = len(nums)
        index = 0
        result = 0
        nums.sort()
        while index < ll and nums[index] <= 0 and k > 0:
            k -= 1
            if nums[index] < 0:
                result -= nums[index]
                index += 1
            elif nums[index] == 0:
                k -= k%2
                index += 1
                break

        if index == ll:
            result += nums[-1]*(k%2)
        elif k == 0:
            result += sum(nums[index:])
        else:
            #print(result)
            result += sum(nums[index:])
            #print(result)
            result -= nums[index]*2*(k%2)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
