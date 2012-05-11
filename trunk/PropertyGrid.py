'''
Created on May 7, 2012

@author: root
'''
import wx.grid
#from Node import Node
#from Disk import Disk
#from User import User
from XML_File import XML_File


class PropertyGrid(wx.grid.Grid):
   
    configFile = ""
    Logs = []
    Nodes = []
    Users = []
   
    def __init__(self, parent,Logs,Nodes,Users):
        wx.grid.Grid.__init__(self, parent)
        self.CreateGrid(1, 2)
        self.SetColSize(0,300)
        self.SetColSize(1,500)
        self.SetMinSize((800,250))
        self.EnableScrolling(True,True)               
        self.EnableDragColSize(False)
        self.EnableDragGridSize(False)
        self.EnableDragRowSize(False)
        self.SetId(30)
        self.SetColLabelValue(0,"Property")
        self.SetColLabelValue(1,"Value")
        self.Logs = Logs
        self.Nodes = Nodes
        self.Users = Users
        
    def GetConfigFile(self):
        return self.configFile
    
    def SetNodes(self,Nodes):
        self.Nodes = Nodes
        
    def BuildTable(self,fileChoice,goldDir):
        rowIndex = 0
        
        self.DeleteRows(0,self.NumberRows)
        self.Update()
        self.SetColLabelValue(0,"Property")
        self.SetColLabelValue(1,"Value")
        
        # Build a Object representing File and then pull props
        self.configFile = XML_File(goldDir+"/",fileChoice+".xml",self.Logs,self.Nodes,self.Users)
        xmlPropList = self.configFile.getProperties()    
        
            
        for prop in xmlPropList:
            self.AppendRows(1)
           
            self.SetCellValue(rowIndex,0,str(prop['name']))
            self.SetCellValue(rowIndex,1,str(prop['value']))
            self.SetReadOnly(rowIndex,0)
            if rowIndex % 2:
                self.SetCellBackgroundColour(rowIndex,0,"white")
                self.SetCellBackgroundColour(rowIndex,1,"white")
            else:
                self.SetCellBackgroundColour(rowIndex,0,"lightblue")
                self.SetCellBackgroundColour(rowIndex,1,"lightblue") 
            rowIndex += 1  
        self.DeleteRows(rowIndex)



