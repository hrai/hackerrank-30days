
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        q = [root] if root else []
        nodes = []

        if root is not None:
            q.append(root)
            nodes.append(str(root.data))

        while q:
            node = q.pop(0)
            # del q[0]

            print(len(q))

            if node.left is not None:
                q.append(node.left)
                nodes.append(str(node.left.data))
            if node.right is not None:
                q.append(node.right)
                nodes.append(str(node.right.data))

        print(" ".join(nodes))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
