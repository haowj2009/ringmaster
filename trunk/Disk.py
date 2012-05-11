'''
Created on Apr 20, 2012

@author: root
'''

class Disk:
   
    deviceName = "\dev\sdb"
    partitionStatus = 0
    fsType = "xfs"
    diskStatus = 0
    fsStatus = 0
    rawCapacity = 0
    
    def get_deviceName(self):
        return self.deviceName
    
    def get_partionStatus(self):
        return self.partitionStatus
    
    def get_fsType(self):
        return self.fsType
    
    def get_fsStatus(self):
        return self.fsStatus
    
    def set_fsStatus(self,fsStatus):
        self.fsStatus = fsStatus
    
    def get_diskStatus(self):
        return self.diskStatus
    
    def get_rawCapacity(self):
        return self.rawCapacity
    
    def set_rawCapacity(self,rawCapacity):
        self.rawCapacity = rawCapacity
    
    
    
    def __init__(self, deviceName, partitionStatus, fsType, diskStatus, fsStatus):
        self.deviceName = deviceName
        self.partitionStatus = partitionStatus
        self.fsType = fsType
        self.diskStatus = diskStatus
        self.fsStatus = fsStatus

