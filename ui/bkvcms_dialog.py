import logging
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6 import QtGui, QtCore
from .base.dialog_bkvcms import Ui_Dialog_BKVCMS
import pendulum
from controller.subcontroller.models.bkvscalarmodel import BKVScalarTableModel
class BKVCMSDialog(QDialog,Ui_Dialog_BKVCMS):
    def __init__(self,objectdata,cmsdata,channelitems,scalaritems,mdicontroller):
        super().__init__()
        self.objectdata = objectdata
        self.cmsdata = cmsdata
        self.channelitems = channelitems
        self.scalaritems = scalaritems
        self.mdicontroller = mdicontroller
        self.cmsdata.update=False
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('initUI started')
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.closeEvent = self.CloseEvent
        self.pushButton_synch.clicked.connect(self.onSynch)
        self.label_country.setText(self.cmsdata.country)
        self.label_site.setText(self.cmsdata.site)
        self.label_wtg.setText(self.cmsdata.wtg)

    
    def CloseEvent(self, event):
        print("X is clicked")
        
        self.cmsdata.update = False
        self.mdicontroller.removeMDIChild(self.objectdata)

    def onSynch(self):
        #print('Synch button pressed')

        print("aura site id: "+str(self.cmsdata.site_aura_id), "aura wtg id: "+str(self.cmsdata.wtg_aura_id), "aura model id: "+str(self.cmsdata.bkv_aura_modelid))
        currentmodelid=self.mdicontroller.auraapi.getLatestValues(self.cmsdata.site_aura_id ,self.cmsdata.wtg_aura_id,self.cmsdata.bkv_aura_modelid,1)
        print(currentmodelid)
        rows=[]
        if len(currentmodelid)>0:
            if len(currentmodelid[0])>=1:
                if "values" in currentmodelid[0]:
                    self.modelid=int(currentmodelid[0]["values"][0])
                    self.modelidtime=pendulum.from_timestamp(int(currentmodelid[0]["timeStamp"][0]))
                    text="Model ID: "+str(self.modelid)+" Time: "+str(self.modelidtime)
                    self.label_modelid.setText(text)
                    #get scalqars from db
                    scalarlist=self.mdicontroller.cmsdb.getBKVDDAUScalarsbyModelID(self.modelid)
                    '''
                    self.scalarid=scalarid  
                    self.name=name
                    self.unit=unit
                    self.isvibration=isvibration
                    self.cdp=cdp
                    self.component=component
                    self.id=id
                    self.dbid=dbid
                    self.modelid=modelid
                    "Scalar no", "Name", "Unit", "Is Vibration", "CDP", "Component
                    '''
                    for name,scalar in scalarlist.items():
                        row=[scalar.scalarid,name,scalar.unit,scalar.isvibration,scalar.cdp,scalar.component]
                        rows.append(row)
                    tablemodel=BKVScalarTableModel(rows)
                    self.tableView_scalars.setModel(tablemodel)
                   
                
            
            
        else:
            print("No new data")
        #self.close()

    def onAccept(self):
        print('OK button pressed')
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,[self.cmsdata,self.channelitems,self.scalaritems],self.update)
        #self.close()
        
    def onReject(self):
        print('Cancel button pressed')
        self.update = False
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,[self.cmsdata,self.channelitems,self.scalaritems],self.update )
        #self.close()

        
        
        

   

    

        
