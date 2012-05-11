'''
Created on Apr 23, 2012

@author: root
'''

class Log_XML:
          
    nodeName = ""
    module = ""
    command = ""
    xmlFile = ""
    result = ""
  
    statusCode = ""
    
    def add(self,nodeName,module,command,xmlFile,result,statusCode):
        self.nodeName = nodeName
        self.module = module
        self.result = result
        self.command = command
        self.xmlFile = xmlFile
        self.statusCode = statusCode
        
    def get_nodeName(self):
        return self.nodeName
    def get_module(self):
        return self.module
    def get_command(self):
        return self.command
    def get_results(self):
        return self.result
    def get_xmlFile(self):
        return self.xmlFile
   
    def get_statusCode(self):
        return self.statusCode
    
    def set_statusCode(self,code):
        self.statusCode = code
    
    def set_xmlFile(self,xmlFile):
        self.xmlFile = xmlFile
        
    def get(self):
        return str(self.nodeName)+","+str(self.module) + "," + str(self.command) + "," + str(self.xmlFile) +","+ str(self.result) + "," + str(self.statusCode)
         
        
        