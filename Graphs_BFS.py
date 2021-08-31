# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:46:24 2021

@author: Jinal
"""
from Graphs import Graph
import copy
from Queue import Queue

class vertex:
    
    def __init__(self, vertex_name):
        self.vertex_name = vertex_name
        self.color = "white"
        self.distance = -1
        self.parent = None
        
class Graphs_BFS():
    
    def __init__(self, graph, source ):
        for k, v in graph.__dict__.items():
            self.__dict__[k] = copy.deepcopy(v)
        self.source = source
        self.queue = Queue(len(self.vertex_list))
        self.vertex_attributes = [vertex(v) for v in self.vertex_list]
    
        for k, v in graph.__dict__.items():
            self.__dict__[k] = copy.deepcopy(v)
            
            
        self.queue.enqueue(source)
        source_index = self.vertex_list.index(source)
        self.vertex_attributes[source_index].color = "gray"
        self.vertex_attributes[source_index].distance = 0
        self.vertex_attributes[source_index].parent = None
        
        while not self.queue.is_empty():
            bool_dequeue, current_node = self.queue.dequeue()
            if bool_dequeue:
                current_node_index = self.vertex_list.index(current_node)
                current_node_adj_list = self.adjacency_list[current_node_index]
                current_node_adj_list.view_list()
                loop_adj_list_node = current_node_adj_list.head
                while loop_adj_list_node:
                    loop_adj_list_node_index = self.vertex_list.index(loop_adj_list_node.value)

                    if self.vertex_attributes[loop_adj_list_node_index].color == "white":
                        self.vertex_attributes[loop_adj_list_node_index].color = "gray"
                        self.vertex_attributes[loop_adj_list_node_index].distance = self.vertex_attributes[current_node_index].distance + 1
                        self.vertex_attributes[loop_adj_list_node_index].parent = current_node
                        bool_enqueue, _= self.queue.enqueue(loop_adj_list_node.value)
                        loop_adj_list_node  = loop_adj_list_node.next_node
                    else: 
                        loop_adj_list_node  = loop_adj_list_node.next_node
                    self.vertex_attributes[current_node_index].color = "black"
                
        
        for v in self.vertex_attributes:
            print(str(v.vertex_name) + " reached from the parent " + str(v.parent) + ". The distance from the source is " + str(v.distance))
        


        
my_graph = Graph(["r", "s", "t", "u", "v", "w", "x", "y"], [("r", "v"), ("r", "s"), ("s", "w"), ("w", "t"), ("w", "x"), ("t", "x"), ("t", "u") ,  ("u", "y") , ("u", "x") , ("x", "y")])

my_graph.view_adjacency_list()
my_graph_bfs = Graphs_BFS(my_graph,"s" )
