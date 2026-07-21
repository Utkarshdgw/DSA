class Solution(object):
    def isSymmetric(self, root):
        def sub(left, right):
            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            return sub(left.left, right.right) and sub(left.right, right.left)

        if root == None:
            return True

        return sub(root.left, root.right)