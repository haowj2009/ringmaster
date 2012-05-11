'''
Created on Apr 20, 2012

@author: root
'''

class Node:
    
    hostName = "Hostname"
    ipAddress = "192.168.100.100"
    javaVersion = "Sun 1.7"
    personalities= "njd"
    cpuCount = ""
    cpuType = ""
    total_rawCapacity = ""
    ramInfo = ""
    adminUser = ""
    adminPW = ""
    Disks = []
    Roles = []
    Services = []
    
    def get_hostName(self):
        return self.hostName
    
    def get_ipAddress(self):
        return self.ipAddress
    
    
    def add_Disk(self,disk):
        self.Disks.append(disk)
    
    def get_Disks(self):
        return self.Disks
    
    def get_total_rawCapacity(self):
        return self.total_rawCapacity
    
    def set_total_rawCapacity(self,total_rawCapacity):
        self.total_rawCapacity = total_rawCapacity
    
        
    def get_Roles(self):
        return self.Roles
    
    def set_javaVersion(self,javaVersion):
        self.javaVersion = javaVersion
        
    def get_javaVersion(self):
        return self.javaVersion
    
    def set_cpuCount(self,cpuCount):
        self.cpuCount = cpuCount
        
    def set_cpuType(self,cpuType):
        self.cpuType = cpuType
        
    def get_cpuCount(self):
        return self.cpuCount
    
    def get_cpuType(self):
        return self.cpuType
    
    def set_ramInfo(self,ramInfo):
        self.ramInfo = ramInfo
        
    def get_ramInfo(self):
        return self.ramInfo
    
    def set_adminUser(self,adminUser):
        self.adminUser = adminUser
    
    def get_adminUser(self):
        return self.adminUser
    
    def set_adminPW(self,adminPW):
        self.adminPW = adminPW
    
    def get_adminPW(self):
        return self.adminPW
    
    def add_Role(self,Role):
        self.Roles.append(Role)
        
    def get_personalities(self):
        return self.personalities
    def set_personalities(self,personalities):
        self.personalities = personalities
    

    def __init__(self, hostName, ipAddress,personalities):
        self.hostName = hostName
        self.ipAddress = ipAddress
        self.personalities = personalities
        self.Roles = []
        self.Disks = []

