# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 19:09:49 2021

@author: Jinal
"""
import Singly_LinkedList as ll
import numpy as np
class Graph:
    def __init__(self, vertex_list, edge_list, directed = False):
        self.adjacency_list = None
        self.adjacency_matrix = None
        self.vertex_list = None
        self.edge_list = None
        self.directed = directed
        if vertex_list is not None:
            self.vertex_list = vertex_list
            self.adjacency_list = [None]*len(self.vertex_list)
            self.adjacency_matrix = np.array([[0]*len(self.vertex_list)]*len(self.vertex_list))
            
            
        if edge_list is not None:
            self.edge_list = edge_list
            for s,d in self.edge_list:
                source_added = False
                destination_added = False
                print(s,d)
                if self.adjacency_list[self.vertex_list.index(s)] is None:
                   self.adjacency_list[self.vertex_list.index(s)] = ll.Singly_LinkedList(ll.Node(d))
                   source_added = True
                   
                   
                if not self.directed and self.adjacency_list[self.vertex_list.index(d)] is None:
                     self.adjacency_list[self.vertex_list.index(d)] = ll.Singly_LinkedList(ll.Node(s)) 
                     destination_added = True
                     
                     
                  
                if self.directed:
                    if not source_added: self.adjacency_list[self.vertex_list.index(s)].insert_tail(ll.Node(d)) 
                else:
                    if not source_added : self.adjacency_list[self.vertex_list.index(s)].insert_tail(ll.Node(d)) 
                    if not destination_added: self.adjacency_list[self.vertex_list.index(d)].insert_tail(ll.Node(s)) 
                   
                if self.directed:
                    self.adjacency_matrix[self.vertex_list.index(s)][self.vertex_list.index(d)] = 1
                else:
                    self.adjacency_matrix[self.vertex_list.index(s)][self.vertex_list.index(d)] = 1
                    self.adjacency_matrix[self.vertex_list.index(d)][self.vertex_list.index(s)] = 1
        
    def view_adjacency_list(self):
        for v in self.vertex_list:
            print(str(v) + " : " , end =" ")
            if self.adjacency_list[self.vertex_list.index(v)] is not None:
                self.adjacency_list[self.vertex_list.index(v)].view_list()

            print()
                
    def view_adjacency_matrix(self):
        print(self.adjacency_matrix)
                
        

my_graph = Graph([1,2,3,4,5], [(1,2), (5,1), (2,5), (2,4), (2,3), (3,4), (5,4)])


print("************ Undirected ************")    
my_graph.view_adjacency_list()
my_graph.view_adjacency_matrix()
        
     
my_graph = Graph([1,2,3,4,5], [(1,2), (5,1), (2,5), (2,4), (2,3), (3,4), (5,4)], True)


print("************ Directed ************")    
my_graph.view_adjacency_list()
my_graph.view_adjacency_matrix()
