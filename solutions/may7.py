# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

d=defaultdict()
def parent(node,val1,parent1,val2,parent2,c,level):
    if node is None:
        # print(1)
        return False
    # if node.val==val1:
    #     d['p1']=='par'
    #     print('hi')
    #     c+=1
    # if node.val==val1:
    #     d['p2']=='par'
    #     print('yo')
    #     c+=1
    if node.left is None:
        left = 'x'
    else:
        left = node.left.val
        
    if node.right is None:
        right = 'x'
    else:
        right = node.right.val
        
    if(left==val1 or right==val1):
        d['p1']=node.val
        d['l1']=level+1
        # print(2)
        c+=1
    if(left==val2 or right==val2):
        d['p2']=node.val
        d['l2']=level+1
        # print(3)
        c+=1
    if(c==2):
        # print('c done')
        return True
    if parent(node.left,val1,node.val,val2,node.val,c,level+1):
        # print(4)
        return True
    else:
        return parent(node.right,val1,node.val,val2,node.val,c,level+1)
    
    
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        print(parent(root,x,-1,y,-1,0,0))
        # print(d)
        if(d['p1']==d['p2']):
            return False
        if(d['l1']!=d['l2']):
            return False
        else:
            return True
            # print(parent(root,d['p1'],-1,d['p2'],-1,0,0))
            # # print(d)
            # if(d['p1']==d['p2']):
            #     return True
            # else:
            #     return False
        # print(d)
