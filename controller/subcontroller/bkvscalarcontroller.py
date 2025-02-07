import logging
from ui.bkvcms_dialog import BKVCMSDialog

class BKVScalarController:
    def __init__(self,cmsdb,mdicontroller):
        self.cmsdb = cmsdb
        self.mdiController = mdicontroller
        #self.auraclient=self.mdiController.auraapi
        
    def getDialog(self,objectdata):
        bkvcs=self.getParameter(objectdata)
        sub=None
        if not bkvcs is None:
            #get modelid
            
            
            sub=BKVCMSDialog(objectdata,bkvcs,None,None,self.mdiController)
            title="BKV CMS: "+str(bkvcs.country)+"/"+str(bkvcs.site)+"/"+str(bkvcs.wtg)+"/"+str(bkvcs.name)
           
            sub.setWindowTitle("BKV CMS: "+title) 
            
            #wtglist=auraclient.get_SiteList()     
            #print(wtglist)          
        return sub
        

    def getParameter(self,objectdata):
        cmssystem=self.cmsdb.getBKVSystem(objectdata['id'])
        
        return cmssystem
    
    

    def saveParameter(self,objectdata,payload):
        print("saving:", objectdata,payload)
        
        '''
        curretnwtgtype=self.cmsdb.getWtgType(objectdata['id'])
        if str(curretnwtgtype.name) != str(wtgtype.name):
            #update tab_object
            self.cmsdb.updateName(objectdata['id'],wtgtype.name)
        nominalpower=curretnwtgtype.nominalpower
        if curretnwtgtype.nominalpower != wtgtype.nominalpower:
            try:
                nominalpower=int(wtgtype.nominalpower)
            except:
                nominalpower=wtgtype.nominalpower
        rotordiameter=curretnwtgtype.rotordiameter
        if curretnwtgtype.rotordiameter != wtgtype.rotordiameter:
            try:
                rotordiameter=int(wtgtype.rotordiameter)
            except:
                rotordiameter=wtgtype.rotordiameter
        drive=curretnwtgtype.drive
        if curretnwtgtype.drive != wtgtype.drive:
            drive=wtgtype.drive
        windclass=curretnwtgtype.windclass
        if curretnwtgtype.windclass != wtgtype.windclass:
            windclass=wtgtype.windclass
        self.cmsdb.updateWTGType(objectdata['id'],nominalpower,rotordiameter,drive,windclass)
        '''
