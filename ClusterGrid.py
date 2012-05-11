'''
Created on May 7, 2012

@author: root
'''

import wx.grid
from NodeInfo import NodeInfo

class ClusterGrid(wx.grid.Grid):
    
        Logs = []
        Nodes = []
        Users = []
    
        def __init__(self, parent,Logs,Nodes,Users):
            print "Init ClusterGRID"
            wx.grid.Grid.__init__(self, parent)
            self.CreateGrid(1, 5)
            self.SetMinSize((800,250))
            self.EnableScrolling(True,True)               
            self.EnableDragColSize(False)
            self.EnableDragGridSize(False)
            self.EnableDragRowSize(False)
            self.SetColLabelValue(0,"HostName")
            self.SetColLabelValue(1,"IP Address")
            self.SetColLabelValue(2,"CPUs")
            self.SetColLabelValue(3,"RAM")
            self.SetColLabelValue(4,"Disk Capacity (GB)")  
            self.SetColSize(0,140)
            self.SetColSize(1,140)
            self.SetColSize(2,140)
            self.SetColSize(3,140)
            self.SetColSize(4,150)
            self.SetMinSize((810,250))
            self.Logs = Logs
            self.Nodes = Nodes
            self.Users = Users
                
        
        def BuildTable(self,Nodes):
            rowIndex = 0
           # nodeInfo = NodeInfo()
           # Nodes = nodeInfo.ImportNodeList(nodeListPath)
            self.DeleteRows(0,self.NumberRows)
            self.Update()
            for node in Nodes:
                self.AppendRows(1)
                self.SetCellValue(rowIndex,0,str(node.get_hostName()))
                self.SetCellValue(rowIndex,1,str(node.get_ipAddress()))
                self.SetCellValue(rowIndex,2,str(node.get_cpuCount()))
                self.SetCellValue(rowIndex,3,str(node.get_ramInfo()))
                self.SetCellValue(rowIndex,4,str(node.get_total_rawCapacity()))
                self.SetReadOnly(rowIndex,0)
                if rowIndex % 2:
                    self.SetCellBackgroundColour(rowIndex,0,"white")
                    self.SetCellBackgroundColour(rowIndex,1,"white")
                    self.SetCellBackgroundColour(rowIndex,2,"white")
                    self.SetCellBackgroundColour(rowIndex,3,"white")
                    self.SetCellBackgroundColour(rowIndex,4,"white")
                else:
                    self.SetCellBackgroundColour(rowIndex,0,"lightblue")
                    self.SetCellBackgroundColour(rowIndex,1,"lightblue") 
                    self.SetCellBackgroundColour(rowIndex,2,"lightblue")
                    self.SetCellBackgroundColour(rowIndex,3,"lightblue") 
                    self.SetCellBackgroundColour(rowIndex,4,"lightblue")
                rowIndex += 1    
            #self.DeleteRows(rowIndex)
        