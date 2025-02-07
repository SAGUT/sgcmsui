import logging
from ui.bachmanncms_dialog import BachmannCMSDialog
from .models.bachmannchannelmodel import BachmannCMSTableModel
#|
class BachmannCMSController:
    def __init__(self,cmsdb,mdicontroller):
        self.cmsdb = cmsdb
        self.mdiController = mdicontroller
        self.tablemodel=None
        
    def getDialog(self,objectdata):
        bachmanncms=self.getParameter(objectdata)
        sub=None
        if not bachmanncms is None:
            self.tablemodel=self.getChannelTableModel(objectdata)
            sub=BachmannCMSDialog(objectdata,bachmanncms,self.tablemodel,self.mdiController)
            
            sub.setWindowTitle("Bachmann CMS: "+str(bachmanncms.name))                
        return sub
        

    def getParameter(self,objectdata):
        cmssystem=self.cmsdb.getBachmannCMS(objectdata['id'])
        
        return cmssystem
    
    def getChannelTableModel(self,objectdata):
        channellist=self.cmsdb.getBachmannChannels(objectdata['id'])
        '''
            channeldbid
            ,[nordex_channel_wtgid] as wtgid
            ,[nordex_channel_cmsid] as cmsid
            ,[nordex_channel_number] as channel_number
            ,[nordex_channel_identifier] as identifier
            ,[nordex_channel_label] as label
            ,[nordex_channel_speedlabel] as speedlabel
            ,[nordex_channel_powerlabel] as powerlabel
        '''
        channeldbid=[]
        wtgid=[]
        cmsid=[]
        channel_number=[]
        identifier=[]
        label=[]
        speedlabel=[]
        powerlabel=[]
        for channel in channellist:
            channeldbid.append(channel['channeldbid'])
            wtgid.append(channel['wtgid'])
            cmsid.append(channel['cmsid'])
            channel_number.append(channel['channel_number'])
            identifier.append(channel['identifier'])
            label.append(channel['label'])
            speedlabel.append(channel['speedlabel'])
            powerlabel.append(channel['powerlabel'])
        data=[channeldbid,wtgid,cmsid,channel_number,identifier,label,speedlabel,powerlabel]
        
        model = BachmannCMSTableModel(data)
        return model

    def saveParameter(self,objectdata,payload):
        print("saving:", objectdata,payload)
        