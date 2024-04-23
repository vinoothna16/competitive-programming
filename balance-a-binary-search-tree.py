# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorderTraversal(root):
            if not root:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        
        inorder_nodes = inorderTraversal(root)

        def sortedArrayToBST(arr, start, end): 
            # NOTE: base case to exit recursion
            if start > end: 
                return None

            # NOTE: can't do `mid = len(arr) // 2` 
            # because in recursive calls, we need to use the start and end pointers to get relevant part of input `arr`
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = sortedArrayToBST(arr, start, mid-1)
            root.right = sortedArrayToBST(arr, mid+1, end)
            return root
        
        return sortedArrayToBST(inorder_nodes, 0, len(inorder_nodes)-1)
