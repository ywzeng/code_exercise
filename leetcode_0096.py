class Solution:
    def numTrees(self, n: int) -> int:
        """ 
        In a binary search tree, the nodes in its left sub-tree are all smaller than its root, and the nodes in its right sub-tree are all greater than its root. 
        Given a number as the root node, the numbers that are smaller than it are in its left sub-tree, and the numbers that are greater than it are in its right sub-tree.
        Recursively, the roots of left and right sub-trees satisfy the above rule as well.
        Given a number n, we can have n types of root node, namely from 1 to n.
        Suppose the total type number of the n root nodes is T(n).
        Suppose that one certain root is i (1<=i<=n), and there are i-1 nodes in its left sub-tree, and n-i nodes in its right sub-tree. We suppose the type number of tree t(i)=T(i-1)*T(n-i).
        Therefore, T(n)=t(1)+t(2)+...+t(n), and t(i)=T(i-1)*T(n-i).
        This is the accumulation process. We can employ DP to solve this problem.
        """
        dp_list = [0 for i in range(n+1)]
        dp_list[0], dp_list[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp_list[i] += dp_list[j] * dp_list[i-j-1]
        return dp_list[n]
