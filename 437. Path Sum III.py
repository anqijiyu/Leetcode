# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, [sum])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t-node.val: hit += 1                          # count if sum == target
        targets = [t-node.val for t in targets]+[origin]         # update the targets
        return hit+self.helper(node.left, origin, targets)+self.helper(node.right, origin, targets)
        # 先从头结点开始遍历，求得满足条件的路径的个数后，再分别遍历其左右子树，求得满足条件的路径再累加。
        # def helper(root, sum):
        #     if not root:
        #         return 0
        #     res = 0
        #     if sum == root.val:
        #         res += 1
        #     res += helper(root.left, sum-root.val)
        #     res += helper(root.right, sum-root.val)
        #     return res
        # if not root:
        #     return 0
        # return helper(root, sum)+self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
