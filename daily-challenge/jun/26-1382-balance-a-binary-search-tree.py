"""
1382. Balance a Binary Search Tree
Medium
Topics
Companies
Hint
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
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
    def leetcode(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        length = len(nums)

        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1

        return patches

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    a = [0,2,2]
    #a = [3,2,1,2,1,7]
    b = [5]
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    print(app.leetcode(k,w,profits,capital))
