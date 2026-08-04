

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def in_order_traversal(root: BinaryTreeNode) -> list[int]:
        if root is None:
            return []

        ans = BinaryTreeNode.in_order_traversal(root.left)
        ans.append(root.val)
        ans.extend(BinaryTreeNode.in_order_traversal(root.right))

        return ans


    @staticmethod
    def pre_order_traversal(root: BinaryTreeNode) -> list[int]:
        if root is None:
            return []

        ans = [root.val]
        ans.extend(BinaryTreeNode.pre_order_traversal(root.left))
        ans.extend(BinaryTreeNode.pre_order_traversal(root.right))

        return ans


    @staticmethod
    def post_order_traversal(root: BinaryTreeNode) -> list[int]:
        if root is None:
            return []

        ans = BinaryTreeNode.post_order_traversal(root.left)
        ans.extend(BinaryTreeNode.post_order_traversal(root.right))
        ans.append(root.val)

        return ans