'''
Created on Apr 20, 2012

@author: root
'''

class Role:

    name = "Role Name"
    notation = "a"
    modules = []
    
    def get_modules(self):
        return self.modules
    
    def add_modules(self,RPM):
        self.modules.append(RPM)
        
    def get_notation(self):
        return self.notation
    
    def get_name(self):
        return self.name
   

    def __init__(self, name, notation):
        self.name = name
        self.notation = notation
        self.modules = []
