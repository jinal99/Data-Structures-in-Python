# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:46:21 2021

@author: harsh.nandedkar
"""

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
        


class BST:
    def __init__(self,root_node):
        self.root_node=root_node
        
    def insertnode(self,node):
        if isinstance(node,int):
            node=Node(node)
        else:
            pass
        if self.root_node==None:
           print("Root Node is empty")
           self.root_node=node 
        else:
           current_node=self.root_node
           not_found=True
           while not_found: 
               if node.value>current_node.value:
                   print("Node greater than Root Node")
                   if current_node.right==None:
                       print("Current Node.Right is None and the value is the element you pushed in")
                       current_node.right=node
                       node.parent=current_node
                       not_found=False
                   elif current_node.right!=None:
                       print("Current Node.Right is not None and we are inserting a value")
                       current_node=current_node.right
               else:
                   print("Node lesser than Root Node")
                   if current_node.left==None:
                       print("Current Node.Left is None and the value is the element you pushed in")
                       current_node.left=node
                       node.parent=current_node
                       not_found=False
                   elif current_node.left!=None:
                       print("Current Node.Right is not None and we are inserting a value")
                       current_node=current_node.left
                     
                   
                
                
                   
                   



#root_node=Node(12)
#
#abc=BST(root_node)
#
#abc.insertnode(Node(14))
#abc.insertnode(Node(11))
#abc.insertnode(Node(10))
#abc.insertnode(30)