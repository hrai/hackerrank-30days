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
        if root is None:
            return -1

        left_ht = self.getHeight(root.left)
        right_ht = self.getHeight(root.right)

        return max(left_ht, right_ht)+1
