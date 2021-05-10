# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:03:20 2021

@author: Jinal
"""
import numpy as np

# tail points to the location where the element has to be inserted, so insert the value and then increment the tail
# head points to the first element, queue the element pointing to the head

# this is a circular queue hence the total number of elements inserted are one less than the size to avoid confusion of underflow and overflow conditions
class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = np.empty(size)
        self.queue[:] = np.nan # because the np.empty is an array of 0s, we want nan as default values 
        self.head = 0
        self.tail = 0
        
    
    def view_queue(self):
        print(self.queue)
        
    def is_empty(self):
        if self.head == self.tail:
            return True
        else:
            return False
        
    def enqueue(self, element):
        if (self.tail + 1) % self.size == self.head:
            self.view_queue()
            return False, "Overflow"
        else:
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % self.size
            self.view_queue()
            return True, str(element) + " added to the queue"
        
    def dequeue(self):
        if self.head == self.tail:
            self.view_queue()
            return False, "Underflow"
        
        else:
            dequeued_element = self.queue[self.head]
            self.queue[self.head] = np.nan
            self.head = (self.head + 1)% self.size
            self.view_queue()
            return True, str(dequeued_element) + " removed from the queue"
            
        
        
my_queue = Queue(5)
my_queue.head 
my_queue.tail
my_queue.is_empty()
my_queue.enqueue(1)      
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.tail
my_queue.enqueue(5)   
my_queue.head
my_queue.tail

my_queue.dequeue()   #1
my_queue.head
my_queue.tail
 

my_queue.dequeue()    #2
my_queue.head
my_queue.tail
            
my_queue.dequeue()    #3
my_queue.head
my_queue.tail          
      
my_queue.enqueue(5)   
  
my_queue.dequeue()    #4
my_queue.head
my_queue.tail          

my_queue.enqueue(6)   
my_queue.head
my_queue.tail  

my_queue.dequeue()    #5
my_queue.head
my_queue.tail   
       
my_queue.dequeue()    #6
my_queue.head
my_queue.tail          


my_queue.is_empty()