# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target=targetSum;
        self.result=[]
        self.CheckTargetSum(root,0,[]);
        return self.result;
    def CheckTargetSum(self,root,curSum,path):
        if root==None:
            return;
        path.append(root.val);
        
        curSum+=root.val;
        
        self.CheckTargetSum(root.left,curSum,path);
        if not root.left and not root.right:
            if curSum==self.target:
                temp=path[:];
                self.result.append(temp);
        self.CheckTargetSum(root.right,curSum,path);
        
        path.pop();
        