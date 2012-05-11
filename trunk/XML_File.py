'''
Created on Apr 25, 2012

@author: root
'''

# This class represents an individual hadoop configuration File
import ssh
import threading
import Queue
import wx

from Log_XML import Log_XML
from xml.etree.ElementTree import parse

class XML_File:
   
    goldDir = "./conf/gold/"
    goldFile = ""
    remoteDir = "/usr/lib/gphd/conf/"
    Nodes = []
    Log = []
    Users = []
    returnQueue = Queue.Queue()
    Properties = []
    installUser = "root"
    installPW = "P@ssw0rd"
    
    
    def sshExec(self,cmd,node,goldFile,callingModule):
        try:
            sshCon = ssh.Connection(node.get_hostName(), username=self.installUser, password=self.installPW)
            (execStatus,execReturn) = sshCon.executeSt(cmd)
        except Exception, err:
            exception = "ERROR: Trouble with SSH Connection to "+node.get_hostName()+" : "+str(err)
            execReturn = exception
            execStatus = 1
            #self.fsLog.exception(exception)
        
        log_XML = Log_XML()
        log_XML.add(node.get_hostName(),callingModule,"SSHExec",goldFile ,execReturn,execStatus)
        self.Log.add_Log_XML(log_XML) 
        self.returnQueue.put((node.get_hostName(),execStatus,execReturn))

    
    def sshCopy(self,node, localFile,remoteFile,goldFile,callingModule):
        try:
            sshCon = ssh.Connection(node.get_hostName(), username=self.installUser, password=self.installPW)
           
            #Check on send a return status back.  SSH doesn't yet
           
            sshCon.put(localFile,remoteFile)
            execStatus = 0
            execReturn = "Copy Successful"
        except Exception, err:
            exception = "ERROR: Trouble with SSH Connection to "+node.get_hostName()+" : "+str(err)
            execReturn = exception
            execStatus = 1
            #self.fsLog.exception(exception)
        log_XML = Log_XML()
        log_XML.add(node.get_hostName(),callingModule,"SSHCopy",goldFile ,execReturn,execStatus)
        self.Log.add_Log_XML(log_XML) 
        self.returnQueue.put((node.get_hostName(),execStatus,execReturn))

    
    
    
    
    # This method will compare the remote XML Files versus a Gold Image
    def diff(self):   
        goldPath = self.goldDir + self.goldFile
        remoteGoldPath = "/tmp/"+self.goldFile
        remotePath = "/usr/lib/gphd/hadoop/conf/"+self.goldFile
        diffCMD = "sudo diff "+ remoteGoldPath+" "+remotePath
        threadCount = 0
        Threads = [] 
        for node in self.Nodes:
            Threads.append(threading.Thread(target=self.sshCopy,args=(node, goldPath, remoteGoldPath,self.goldFile, "XML_File:diff")))
            Threads[threadCount].daemon=True
            Threads[threadCount].start()     
            threadCount = threadCount + 1
        for thread in Threads:
            thread.join()
            (hostName,status,results) = self.returnQueue.get()
            
        threadCount = 0
        Threads = [] 
        for node in self.Nodes:
            Threads.append(threading.Thread(target=self.sshExec,args=(diffCMD, node, self.goldFile,"XML_File:diff")))
            Threads[threadCount].daemon=True
            Threads[threadCount].start()     
            threadCount = threadCount + 1
        for thread in Threads:
            thread.join()
            (hostName,status,results) = self.returnQueue.get()
           
    
    
    # Push Gold Image out to all Nodes    
    def push(self,progressbar=0):
        goldPath = self.goldDir + self.goldFile
        remotePath = "/usr/lib/gphd/hadoop/conf/"+self.goldFile
        threadCount = 0
        progress=0
        Threads = [] 
        for node in self.Nodes:
            Threads.append(threading.Thread(target=self.sshCopy,args=(node, goldPath, remotePath,self.goldFile, "XML_File:push")))
            Threads[threadCount].daemon=True
            Threads[threadCount].start()     
            threadCount = threadCount + 1
        for thread in Threads:
            thread.join()
            if progressbar:
                progress += (100/threadCount)
                progressbar.SetValue(progress)
                wx.Yield()
            (hostName,status,results) = self.returnQueue.get()
        
    # Modify Gold Image
    def modify(self,mod_propName,mod_propValue):
        goldPath = self.goldDir + self.goldFile
        print goldPath
        xmlFile = open(goldPath,'r')
        xmlTree = parse(xmlFile)
       
        # Change it in Properties Array for UI Purposes
        for prop in self.Properties:
            if (prop['name'] == mod_propName):
                prop['value'] = mod_propValue 
              
              
        # Change in actual gold image
                
        for element in xmlTree.findall('property'):
            nameFound = False
            for child in element.getchildren():
                prop = {}
                if (str(child.text).upper() == str(mod_propName).upper()):
                    nameFound = True
                elif  (str(child.tag).upper() == 'VALUE') and (nameFound):
                    nameFound = False
                    child.text = mod_propValue
    
        xmlTree.write(goldPath)
        #  Concatenate with base-site.xml to pick XML headers back up
        
        baseFile = open (self.goldDir+"base-site.xml","r")
        print "BASE:"+str(baseFile)
        goldFile = open (goldPath,"r")
        baseData = baseFile.read()
        goldData = goldFile.read()
        goldFile.close()
        new_goldFile = open(goldPath,"w")
        new_goldFile.write(baseData+"\n")      
        new_goldFile.write(goldData)
        new_goldFile.close()           
        
    def GetConfigFileName(self):
        return self.goldFile            
                    
                   
    def parseXML(self):
        goldPath = self.goldDir + self.goldFile
        try:
            xmlFile = open(goldPath,'r')
            xmlTree = parse(xmlFile)
            self.Properties = []
    
            for element in xmlTree.findall('property'):
                nameFound = False
                for child in element.getchildren():
                    prop = {}
                    if (str(child.tag).upper() == 'NAME'):
                        nameFound = True
                        propName = child.text
                    elif  (str(child.tag).upper() == 'VALUE') and (nameFound):
                        nameFound = False
                        propValue = child.text
                        prop['name'] = propName
                        prop['value'] = propValue
                        self.Properties.append(prop)
        except Exception, err:
            print err

        
    
    def getProperties(self):
        return self.Properties
            
            
    
    def set_Users(self):
        for user in self.Users:
            if user.get_role() == "r":
                self.installUser = user.get_userName()
                self.installPW = user.get_password()
            elif user.get_role() == "m":
                self.mapredUser = user.get_userName()
                self.mapredPW = user.get_password()
            elif user.get_role() == "h":
                self.hdfsUser = user.get_userName()
                self.hdfsPW = user.get_password()
                 
    def set_Nodes(self,Nodes):
        self.Nodes = Nodes
    

    def __init__(self,goldDir,goldFile,Log,Nodes,Users):
        self.Log = Log
        self.Users = Users
        self.Nodes = Nodes
        self.goldFile = goldFile
        self.goldDir = goldDir

        
        self.set_Users()
        self.parseXML()