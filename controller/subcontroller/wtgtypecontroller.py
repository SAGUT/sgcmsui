import logging
from ui.wtgtype_dialog import WTGTypeDialog

class WTGTypeController:
    def __init__(self,cmsdb,mdicontroller):
        self.cmsdb = cmsdb
        self.mdiController = mdicontroller
        
    def getDialog(self,objectdata):
        wtgtype=self.getParameter(objectdata)
        sub=None
        if not wtgtype is None:
            sub=WTGTypeDialog(objectdata,wtgtype,self.mdiController)
            sub.label_Company.setText(wtgtype.company)
            sub.setWindowTitle("WTG Type: "+str(wtgtype.name))                
        return sub
        

    def getParameter(self,objectdata):
        return self.cmsdb.getWtgType(objectdata['id'])
    

    def saveParameter(self,objectdata,wtgtype):
        print("saving:", wtgtype)
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

       
    
