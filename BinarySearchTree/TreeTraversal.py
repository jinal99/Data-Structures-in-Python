# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:27:38 2021

@author: harsh.nandedkar
"""

import BST_Insertion as bst

root_node=bst.Node(12)
abc=bst.BST(root_node)
abc.insertnode(bst.Node(14))
abc.insertnode(bst.Node(11))
abc.insertnode(bst.Node(10))
abc.insertnode(6)
abc.insertnode(3)
abc.insertnode(9)
abc.insertnode(13)
#abc.insertnode(30)

def Inorder(root_node):
    if root_node is not None:
        Inorder(root_node.left)
        print(root_node.value)
        Inorder(root_node.right)
        
def Postorder(root_node):
    if root_node is not None:
        Postorder(root_node.left)
        Postorder(root_node.right)
        print(root_node.value)
        
def Preorder(root_node):
    if root_node is not None:
        print(root_node.value)
        Postorder(root_node.left)
        Postorder(root_node.right)


def Search_Node(root_node,value_tosearch):
    if root_node is None:
        print("Value not found!")
        return False
    elif value_tosearch>root_node.value:
        return Search_Node(root_node.right,value_tosearch)
        
    elif value_tosearch<root_node.value:
        return Search_Node(root_node.left,value_tosearch)
    elif value_tosearch==root_node.value:
        print("Value Found!")
        print("WXYZ")
        return True

def Min_BST(root_node):
    while root_node.left!=None:
        root_node=root_node.left
    
    print("Minimum is: ",root_node.value)
    return root_node.value
def Max_BST(root_node):
    while root_node.right!=None:
        root_node=root_node.right
    
    print("Maximum is: ",root_node.value)
    
    return root_node.value

def Successor(root_node,value):
    if Search_Node(root_node,value):
        current_node=root_node
        print(current_node.value)
        while current_node.value!=value:
            if current_node.value>value:
                current_node=current_node.left
            elif current_node.value<value:
                current_node=current_node.right
        print(current_node.value)
        if current_node.right!=None:
            return Min_BST(current_node.right)
        else:
            y=current_node.parent
            while y.parent!=None and y.right==current_node:
                current_node=y
                y=current_node.parent
        
            return y.value
    else:
        return "Value not Found!"


def Predeccesor(root_node,value):
    if Search_Node(root_node,value):
        current_node=root_node
        print(current_node.value)
        while current_node.value!=value:
            if current_node.value>value:
                current_node=current_node.left
            elif current_node.value<value:
                current_node=current_node.right
        print(current_node.value)
        if current_node.left!=None:
            return Max_BST(current_node.left)
        else:
            y=current_node.parent
            while y.parent!=None and y.left==current_node:
                current_node=y
                y=current_node.parent
        
            return y.value
    else:
        return "Value not Found!"
                
            
                
def Transplant(tree,value_node,value_toreplacewith_node):
    # root_node=tree.root_node
    # if Search_Node(root_node,value) and Search_Node(root_node,value_toreplacewith):
    #     value_node=root_node
    #     while value_node.value!=value:
    #         if value_node.value>value:
    #             value_node=value_node.left
    #         elif value_node.value<value:
    #             value_node=value_node.right
    #     print(value_node.value)
        
    #     value_toreplacewith_node=root_node
    #     while value_toreplacewith_node.value!=value:
    #         if value_toreplacewith_node.value>value:
    #             value_toreplacewith_node=value_toreplacewith_node.left
    #         elif value_toreplacewith_node.value<value:
    #             value_toreplacewith_node=value_toreplacewith_node.right
    #     print(value_toreplacewith_node.value)
        
        if value_node.parent!=None:
            tree.root_node=value_toreplacewith_node
        elif value_node==value_node.parent.left:
            value_node.parent.left=value_toreplacewith_node
        else:
            value_node.parent.right=value_toreplacewith_node
        
        if value_toreplacewith_node.value!=None:
            value_toreplacewith_node.parent=value_node.parent
            

def Deletion(tree,value):
    root_node=tree.root_node
    if Search_Node(root_node,value):
        value_node=root_node
        while value_node.value!=value:
            if value_node.value>value:
                value_node=value_node.left
            elif value_node.value<value:
                value_node=value_node.right
        
        if value_node.left==None:
            Transplant(tree,value_node,value_node.right)
        elif value_node.right==None:
            Transplant(tree,value_node,value_node.left)
        else:
            y=Successor(root_node, value)
            y_node=tree.root_node
            while y_node.value!=y:
                if y_node.value>y:
                    y_node=y_node.left
                elif y<y_node.value:
                    y_node.value=y_node.right
            
            if y_node.parent!=value_node:
                Transplant(tree,y_node,y_node.right)
                y_node.parent=value_node.parent
                y_node.left=value_node.left
                y_node.right=value_node.right
            else:
                Transplant(tree,value_node,y_node)
                y_node.parent=value_node.parent
                y_node.left=value_node.left
                
                
                
                
            
            
                
                
        
            
        
        
        
        
        
    
        
    
        
        
Inorder(root_node)
Postorder(root_node)
Preorder(root_node)

        

        


    
    