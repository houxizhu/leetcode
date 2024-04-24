'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        leftq  = [root]
        rightq = [root]

        while leftq or rightq:
            if leftq == None and rightq == None:
                return True
            elif leftq and rightq:
                leftnode = leftq.pop(0)
                rightnode = rightq.pop(0)

                if leftnode == None and rightnode == None:
                    continue
                elif leftnode and rightnode:
                    pass
                else:
                    #print(2222)
                    return False

                if leftnode.val != rightnode.val:
                    #print(3333)
                    return False
                
                leftq.append(leftnode.left)
                leftq.append(leftnode.right)
                rightq.append(rightnode.right)
                rightq.append(rightnode.left)
            else:
                return False
            
        return True

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
