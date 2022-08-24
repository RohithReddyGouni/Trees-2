#Time Complexitiy: O(n)
#Space Complexity: O(height of the tree = Elements in Recursive call stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result=0;
        SumRoot=self.SumToRoot(root,0);
        
        return self.result;
    def SumToRoot(self,root,curSum):
       
        if root==None:
            return
        self.SumToRoot(root.left,curSum*10+root.val);
       
        if not root.left and not root.right:
           
            self.result+=curSum*10+root.val;
        
        self.SumToRoot(root.right,curSum*10+root.val);