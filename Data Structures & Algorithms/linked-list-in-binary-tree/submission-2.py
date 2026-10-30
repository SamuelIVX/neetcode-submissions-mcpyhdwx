class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        sys.setrecursionlimit(3000)

        def dfs(node, curr):
            if curr is None: return True
            if node is None: return False
            if node.val != curr.val: return False

            return dfs(node.left, curr.next) or dfs(node.right, curr.next)

        def preorder(tree_node):
            if tree_node is None: return False

            if tree_node.val == head.val:
                if dfs(tree_node, head):
                    return True

            return preorder(tree_node.left) or preorder(tree_node.right)

        return preorder(root)