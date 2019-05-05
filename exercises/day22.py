class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur

        print(cur)
        return root

    def getHeight(self,root):
        #Write your code here
        if root is None:
            return 0

        if root.left is None or root.right is None:
            return 1

        if root.left:
            left_ht = self.getHeight(root.left)+1

        if root.right:
            right_ht = self.getHeight(root.right)+1

        return max(left_ht, right_ht)
