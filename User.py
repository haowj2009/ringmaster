'''
Created on Apr 20, 2012

@author: root
'''

class User:
    
    userName = ""
    password = ""
    role = ""
    description = ""

    def get_userName(self):
        return self.userName
    
    def get_password(self):
        return self.password
    
    def get_description(self):
        return self.description
    
    def get_role(self):
        return self.role
     
    def __init__(self, userName, password, role, description):
        self.userName = userName
        self.password = password
        self.role = role
        self.description = description

        