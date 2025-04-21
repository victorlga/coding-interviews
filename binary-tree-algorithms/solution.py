# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):

        from collections import defaultdict

        def dfs(node, current_sum, prefix_sums):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums[current_sum - targetSum]
            prefix_sums[current_sum] += 1

            count += dfs(node.left, current_sum, prefix_sums)
            count += dfs(node.right, current_sum, prefix_sums)

            prefix_sums[current_sum] -= 1  # backtrack
            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # base case: sum = 0 occurs once

        return dfs(root, 0, prefix_sums)
