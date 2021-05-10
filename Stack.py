# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:34:28 2021

@author: Jinal
"""


# top points to the location where the element has to be inserted, so insert the value and then increment the top
import numpy as np 

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = np.empty(size)
        self.stack[:] = np.nan # because the np.empty is an array of 0s, we want nan as default values 
        self.top = 0
        
    def view_stack(self):
        print(self.stack)
        
    def is_empty(self):
        if self.top ==0:
            return True
        else:
            return False
        
    def Push(self, element):
        if self.top == self.size:
            return False, "Overflow"
        else:
            self.stack[self.top] = element
            self.top = self.top + 1
            self.view_stack()
            return True, str(element) + " added to the stack"
        
    def Pop(self):
        if self.top == 0:
            return False, "Underflow"
        else:
            self.top = self.top - 1
            popped_element = self.stack[self.top]
            self.stack[self.top] = np.nan
            self.view_stack()
            return True, popped_element
        
            

my_stack = Stack(5)
my_stack.top
my_stack.is_empty()
my_stack.Push(1)
my_stack.Push(2)
my_stack.Push(3)
my_stack.Push(4)
my_stack.Push(5)
my_stack.Push(6)
my_stack.top
my_stack.Pop() #5
my_stack.Pop() #4
my_stack.Pop() #3
my_stack.Pop() #2
my_stack.Pop() #1
my_stack.Pop() # underflow

my_stack_1 = Stack(3)
my_stack_1.Push(1)

