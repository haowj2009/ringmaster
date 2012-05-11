'''
Created on Apr 20, 2012

@author: root
'''
from Node import Node
from Disk import Disk
from User import User
from Log import Log
import csv


class NodeInfo:
   
    Nodes = []

    def ImportNodeList(self,nodeListPath):
        self.Nodes = []
        for row in csv.DictReader(open(nodeListPath), 'hostName IP'.split()):
            node = Node(row['hostName'],row['IP'],"")
            self.Nodes.append(node)
        return self.Nodes
    


    #def __init__(self):
        