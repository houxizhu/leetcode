'''

'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for each in nums:
            dd[each] += 1

        return max(dd, key=dd.get)

if __name__ == "__main__":
    app = Solution()
    a = [1,1,2,3,3]
    a = 701
    print(app.leetcode(a))
