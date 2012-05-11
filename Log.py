'''
Created on Apr 23, 2012

@author: root
'''

class Log:

    
    Log_FS=  []
    Log_Dev=[]
    Log_Software = []
    Log_Config = []
    Log_NodeCheck = []
    Log_XML = []
    Log_Java = []
    
    def add_Log_FS(self, log ):
        self.Log_FS.append(log)
    def add_Log_Dev(self, log ):
        self.Log_Dev.append(log)
    def add_Log_Software(self, log ):
        self.Log_Software.append(log)
    def add_Log_Config(self, log ):
        self.Log_Config.append(log)
    def add_Log_NodeCheck(self, log ):
        self.Log_NodeCheck.append(log)
    def add_Log_XML(self, log ):
        self.Log_XML.append(log)
    def add_Log_Java(self, log ):
        self.Log_Java.append(log)
        
    def get_Log_FS(self):
        return self.Log_FS
       
    def get_Log_Software(self):
        return self.Log_Software
    
    def get_Log_NodeCheck(self):
        return self.Log_NodeCheck
    
    def get_Log_XML(self):
        return self.Log_XML
    
    def get_Log_Java(self):
        return self.Log_Java
    
  
        

    

    #def __init__(self):
      

    
    
 
      
        