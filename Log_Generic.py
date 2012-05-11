'''
Created on Apr 23, 2012

@author: root
'''

class Log_Java:
          
    nodeName = ""
    module = ""
    command = ""
    result = ""
  
    statusCode = ""
    
    def add(self,nodeName,module,command,xmlFile,result,statusCode):
        self.nodeName = nodeName
        self.module = module
        self.result = result
        self.command = command
        self.statusCode = statusCode
        
    def get_nodeName(self):
        return self.nodeName
    def get_module(self):
        return self.module
    def get_command(self):
        return self.command
    def get_results(self):
        return self.result
 
   
    def get(self):
        return str(self.nodeName)+","+str(self.module) +","+ str(self.result) + "," + str(self.statusCode)
         
        
        