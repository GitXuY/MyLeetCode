class Solution(object):
    def maxDepth(self, root):
        depth = 0;
        leftDepth = rightDepth = 0;
        if root == None:
            depth = 0;
        else:
            leftDepth = self.maxDepth(root.left);
            rightDepth = self.maxDepth(root.right);
            depth = max(leftDepth, rightDepth);
        return depth;
