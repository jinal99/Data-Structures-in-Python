# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:12:23 2021

@author: Jinal
"""

import numpy as np
class Node:
    def __init__(self, value, next_node= None):
        self.value = value
        self.next_node = next_node


class Singly_LinkedList:
    def __init__(self, head):
        self.head = head
        self.view_list()

        
    def view_list(self):
        current_node = self.head
        print_string = ""
        while True:
            print_string = print_string + str(current_node.value) + " -> " 
            if current_node.next_node is None:
                break
            current_node = current_node.next_node

        print(print_string + "x ")

    def insert_head(self, new_Node):
        if isinstance(new_Node, Node):
            new_Node.next_node = self.head
            self.head = new_Node
            self.view_list()
        else:
            print("Insert a type of Node.")
            self.view_list()
            
    def insert_tail(self, new_Node):
        if isinstance(new_Node, Node):
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_Node
            self.view_list()
        else:
            print("Insert a type of Node.")
            self.view_list()
        
            
    def delete_head(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            self.head = self.head.next_node
            self.view_list()
        
    
    def delete_tail(self):
        if self.head is None:
            print("LinkedList is empty")
            return 
        pointer_a = self.head
        pointer_b = pointer_a.next_node
        if pointer_b is None:
            self.head = None
            print("All elements deleted from the LinedList")
        else:
            while pointer_b is not None:
                pointer_a = pointer_b
                pointer_b = pointer_b.next_node
            pointer_a.next_node = None
            self.view_list()
        
    def delete_first_occurrence(self, value):
        if self.head is None:
            print("LinkedList is empty")
        else:
            pointer_a = self.head
            
            if pointer_a.value == value: 
                self.head = None
                
                if pointer_a.next_node is None:
                    print("LinkedList empty")
                else:
                    self.head = pointer_a.next_node
                    self.view_list()
                return 
            else:
                if pointer_a.next_node is None:
                    print("Element not found")
                    return
            
            pointer_b = pointer_a.next_node
            
            if pointer_b.value == value and pointer_b.next_node is None:
                self.head.next_node = None
                self.view_list()
                return 
            elif pointer_b.value != value and pointer_b.next_node is None:
                print("Element not found")
                return
                
            pointer_c = pointer_b.next_node
            flag = False
            while pointer_a.next_node is not None:
             #   print("pointer_b.value " + str(pointer_b.value))
                if pointer_b.value == value:
                    pointer_a.next_node = pointer_c
                    self.view_list()
                    flag = True
                    return
                else:
                    if pointer_a.next_node is not None:
                        pointer_a = pointer_a.next_node
                    if pointer_b.next_node is not None:
                        pointer_b = pointer_b.next_node
                    else:
                        pointer_b = None
                    if pointer_c.next_node is not None:
                        pointer_c = pointer_c.next_node
                    else:
                        pointer_c = None

            if flag:
                print("Element deleted")
            else:
                print("Element not found")
            


first_list = Singly_LinkedList(Node(0))
first_list.delete_first_occurrence(2)
first_list.delete_first_occurrence(0)

first_list = Singly_LinkedList(Node(1))
first_list.insert_tail(Node(2))
first_list.delete_first_occurrence(3)
first_list.delete_first_occurrence(1)
first_list.insert_head(Node(1))
first_list.delete_first_occurrence(2)

first_list = Singly_LinkedList(Node(1))
first_list.insert_tail(Node(2))
first_list.insert_tail(Node(3))
first_list.delete_first_occurrence(1)
first_list.insert_head(Node(1))
first_list.delete_first_occurrence(2)
first_list.insert_head(Node(0))
first_list.delete_first_occurrence(3)
first_list.insert_tail(Node(2))
first_list.insert_tail(Node(2))
first_list.insert_tail(Node(3))
first_list.delete_first_occurrence(2)


first_list.delete_tail()

first_list.delete_tail()
first_list.delete_head()



first_list.insert_head(Node(1))
first_list.insert_head(Node(2))

first_list.insert_tail(Node(-1))


first_list.insert_head(Node(0))

first_list.delete_head()
first_list.insert_tail(Node(10))
