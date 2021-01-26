class Solution:
    def numTrees(self, n: int) -> int:
        """ 
        In a binary search tree, the nodes in its left sub-tree are all smaller than its root, and the nodes in its right sub-tree are all greater than its root. 
        Given a number as the root node, the numbers that are smaller than it are in its left sub-tree, and the numbers that are greater than it are in its right sub-tree.
        Recursively, the root of left and right sub-tree satisfy the above rule as well.
        """
        dp_list = [0 for i in range(n+1)]
        dp_list[0], dp_list[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp_list[i] += dp_list[j] * dp_list[i-j-1]
        return dp_list[n]
