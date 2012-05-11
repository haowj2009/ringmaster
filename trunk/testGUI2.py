from Node import Node
from Disk import Disk
from Log import Log
from User import User
import time
#from NodeCheck import NodeCheck
from NodeInfo import NodeInfo
from XML_File import XML_File
from ClusterGrid import ClusterGrid
from PropertyGrid import PropertyGrid
from DiffGrid import DiffGrid


import wx.grid


class ClusterPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
class XmlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
class DiffPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
class ProgressBar:
    
    progressBar = ""
   
    def __init__ (self, parent, statusbar, barFields=3, barField=1, maxcount=100): 
        rect = statusbar.GetFieldRect(barField)
        barLocation = (rect[0],rect[1])
        if (barField+1 == barField) and (wx.Platform == '__WXMSW__'): 
            barSize = (rect [2]+35, rect [3])   # completely fill the last field 
        else: 
            barSize = (rect [2],    rect [3]) 
        self.progressBar = wx.Gauge(statusbar,50,maxcount,barLocation,barSize)

    def SetValue (self, value): 
        self.progressBar.SetValue (value) 
        
        
        

########################################################################
class MyForm(wx.Frame):
    
    xmlGrid = wx.grid
    progressbar = ""
    statusbar = ""
    Nodes = []
    goldDir = ""
  #  xmlPanel = wx.Panel
    wildcard = "Cluster Config (*.hdcfg)|*.hdcfg|" \
            "All files (*.*)|*.*"      
    
    activeCluster = "" 
  
   
    def OnRBClick(self,evt):
        
        radioBox = evt.GetEventObject()
        radioIndex = radioBox.GetSelection()
        fileChoice = radioBox.GetStringSelection()
        self.SetStatusText ( str ( radioIndex ) + ': ' + fileChoice )
        self.xmlGrid.BuildTable(fileChoice,self.goldDir)
 
    def OnPushClick(self,evt):
        pushButton = evt.GetEventObject()
        configFile = self.xmlGrid.GetConfigFile()
        configFile.push(self.progressbar)
        time.sleep(2)
        self.progressbar.SetValue(0)
        self.statusbar.SetStatusText("Push Completed",0)
      
    def OnGridEdit(self,evt):
        print "edit"
        grid = evt.GetEventObject()
        mod_propValue = grid.GetCellValue(evt.GetRow(), evt.GetCol())        
        mod_propName = grid.GetCellValue(evt.GetRow(), evt.GetCol()-1) 
        configFile = self.xmlGrid.GetConfigFile()
        configFile.modify(mod_propName, mod_propValue)
        
    def OnOpen(self,evt):
        print "open"
        nodeInfo = NodeInfo()
       
        file_dlg = wx.FileDialog(self, message="Choose a Cluster Config File",
            defaultDir="./conf",
            defaultFile="",
            wildcard=self.wildcard,
            style=wx.OPEN | wx.CHANGE_DIR 
            )
        if file_dlg.ShowModal() == wx.ID_OK:
            #paths = file_dlg.GetPaths()
            path = file_dlg.GetPath()
            file_dlg.Destroy()
            nodeInfo = NodeInfo()  
            
            self.Nodes = nodeInfo.ImportNodeList(path)
            self.xmlGrid.SetNodes(self.Nodes)
            self.clusterGrid.BuildTable(self.Nodes)
            self.goldDir = path[:-6]
            #self.xmlGrid = PropertyGrid(xmlPanel,Logs,self.Nodes,Users)
            self.xmlGrid.BuildTable("core-site",self.goldDir)
            self.diffGrid.BuildTable(self.Nodes)

        
        
    def OnExit(self,evt):  
        
        dlg = wx.MessageDialog(self, 'Exit Program?', 'Exit GPHD-CM?',wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            dlg.Destroy()
            self.Close(True)
        else:
            dlg.Destroy() 
        
        
        
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="EMC Greenplum HD Config Manager",size=(1000,350))
        self.statusbar = wx.StatusBar(self,50)
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2,-3,-2])
        self.statusbar.SetStatusText("Dan Baskette, EMC Greenplum, 2012",2)
        self.SetStatusBar(self.statusbar)
        self.SetMinSize((1000,350))
        self.SetMaxSize((1000,350))
     
        #Put Panel 
       
        mainPanel = wx.Panel(self)

        #Build notebook
        
        nb = wx.Notebook(mainPanel)
        clusterPanel = ClusterPanel(nb)
        xmlPanel = XmlPanel(nb)
        diffPanel  = DiffPanel(nb)
        nb.AddPage(clusterPanel,"Hadoop Cluster")
        nb.AddPage(xmlPanel,"Config Files")
        nb.AddPage(diffPanel,"Config Differences")
        
        #Build Menus
        fileMenu = wx.Menu()
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        menuOpen = fileMenu.Append(wx.ID_OPEN, "&Open","Open Host Information File")
        menuExit = fileMenu.Append(wx.ID_EXIT,"&Exit","Exit Application")
        
        hostMenu = wx.Menu()
        menu_addHost = hostMenu.Append(wx.ID_ADD,"&Add","Add a Host to Cluster")
        menu_delHost = hostMenu.Append(wx.ID_ADD,"&Delete","Delete a Host to Cluster")
            

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&File")
        menuBar.Append(hostMenu,"&Hosts")
        self.SetMenuBar(menuBar)
        
        # Setup Main Panel Sizer
        
        sizer_mainPanel = wx.BoxSizer(wx.HORIZONTAL) 
        sizer_mainPanel.Add(nb,1,wx.EXPAND)
        mainPanel.SetSizer(sizer_mainPanel)
        
      
        # Setup Panel Sizers
                
        sizer_xmlPanel = wx.BoxSizer(wx.HORIZONTAL)
        sizer_xmlgrid = wx.GridSizer(1,2,10,10)
        sizer_xmlctl = wx.GridSizer(4,1,10,10)
        sizer_xmlPanel.Add(sizer_xmlgrid,4)
        sizer_xmlPanel.Add(sizer_xmlctl,1)

        
        sizer_clusterPanel = wx.BoxSizer(wx.VERTICAL)
        sizer_clustergrid = wx.GridSizer(1,1,50,50)
        sizer_clusterPanel.Add(sizer_clustergrid,4)
        sizer_clusterPanel.AddSpacer(50,500)
        sizer_clusterbtns = wx.GridSizer(1,4,50,50)
        sizer_clusterPanel.Add(sizer_clusterbtns,1)
        
        
        sizer_diffPanel = wx.BoxSizer(wx.HORIZONTAL)
        sizer_diffgrid = wx.GridSizer(1,2,10,10)
        sizer_diffctl = wx.GridSizer(4,1,10,10)
        sizer_diffPanel.Add(sizer_diffgrid,4)
        sizer_diffPanel.Add(sizer_diffctl,1)

        

        xmlPanel.SetSizer(sizer_xmlPanel)
        clusterPanel.SetSizer(sizer_clusterPanel)
        diffPanel.SetSizer(sizer_diffPanel)
        # Build GRID for xmlPanel
        
        self.xmlGrid = PropertyGrid(xmlPanel,Logs,self.Nodes,Users)
      # self.xmlGrid.BuildTable("core-site",self.goldDir)

        # Build GRID for clusterPanel
        
        self.clusterGrid = ClusterGrid(clusterPanel,Logs,self.Nodes,Users)
     #   self.clusterGrid.BuildTable(self.Nodes)
      
      
        self.diffGrid = DiffGrid(diffPanel,Logs,self.Nodes,Users)
   
        
        # Create Radio Buttons
        
        configFile_List = ['core-site','hdfs-site','mapred-site']
        fileChoice_Box = wx.RadioBox(xmlPanel,10,"Configuration Files",size=(135,100),style=wx.VERTICAL,choices=configFile_List)
        fileChoiceDiff_Box = wx.RadioBox(diffPanel,10,"Configuration Files",size=(135,100),style=wx.VERTICAL,choices=configFile_List)

        # Create Buttons

        pushConfig_Btn = wx.Button(xmlPanel,id=20,label="Push Config",size=(100,50))
       
        
        # Add Grids to Sizers
        
        
        sizer_xmlgrid.Add(self.xmlGrid,4)
        sizer_xmlctl.Add(fileChoiceDiff_Box,1,wx.ALIGN_CENTER_HORIZONTAL)
        
    
        

        #sizer_xmlctl.Add(wx.StaticText(xmlPanel),1,wx.EXPAND)
        sizer_xmlctl.Add(pushConfig_Btn,1,wx.ALIGN_CENTER_HORIZONTAL)
        
        sizer_clustergrid.Add(self.clusterGrid,0)
        sizer_clusterbtns.Add(wx.StaticText(clusterPanel),1,wx.EXPAND)
        sizer_clusterbtns.Add(pushConfig_Btn,0)
       
        sizer_xmlgrid.Add(fileChoice_Box,0)
        
        
        sizer_diffgrid.Add(self.diffGrid,4)
        sizer_diffctl.Add(fileChoice_Box,1,wx.ALIGN_CENTER_HORIZONTAL)
  
        # Setup Event Processing
        
        self.Bind(wx.EVT_RADIOBOX, self.OnRBClick, id=10)
        self.Bind(wx.EVT_BUTTON,self.OnPushClick, id=20)
        self.Bind(wx.grid.EVT_GRID_CELL_CHANGE,self.OnGridEdit,id=30)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit,menuExit)



        self.progressbar = ProgressBar (self, self.statusbar) 






              

if __name__ == "__main__":
    
    Roles = []
    #Nodes = []
    Users = []
    adminUser = "root"
    adminPW  = "P@ssw0rd"
    Logs = Log()
    
#    nodeInfo = NodeInfo()
#    nodeListPath = "/tmp/nodes"
#    Nodes = nodeInfo.ImportNodeList(nodeListPath)
#    
#    
#    Users.append(User("root","P@ssw0rd","r","Adminstrative User"))
#
#    nc = NodeCheck(Logs,Nodes,Users)
#    nc.inventory()
   
    
    
   
  
    app = wx.PySimpleApp()
  #  frame = MyForm(Nodes).Show()
    frame = MyForm().Show()

    app.MainLoop()

