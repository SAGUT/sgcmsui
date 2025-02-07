import logging
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6 import QtGui, QtCore
from .base.dialog_bachmanncms import Ui_Dialog_BachmannCMS
from.models.bachmannchannelmodel import BachmannCMSTableModel
import pendulum

class BachmannCMSDialog(QDialog,Ui_Dialog_BachmannCMS):
    def __init__(self,objectdata,cmsdata,tablemodel,mdicontroller):
        super().__init__()
        self.objectdata = objectdata
        self.cmsdata = cmsdata
        self.tablemodel = tablemodel
        self.mdicontroller = mdicontroller
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('initUI started')
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.closeEvent = self.CloseEvent
        self.label_site.setText(self.cmsdata.site)
        self.label_wtg.setText(self.cmsdata.wtg)
        self.lineEdit_name.setText(str(self.cmsdata.name))
        self.lineEdit_apiid.setText(str(self.cmsdata.apiid))
        self.lineEdit_identity.setText(str(self.cmsdata.identity))
        self.lineEdit_nordexname.setText(str(self.cmsdata.name))
        self.lineEdit_skcmsname.setText(str(self.cmsdata.vesname))
        if self.cmsdata.commissioned==1:
            self.checkBox_commissioned.setChecked(True)
        else:
            self.checkBox_commissioned.setChecked(False)
        
        lastfile=""
        try:
            lastfile=pendulum.from_timestamp(self.cmsdata.lastfilecheck).to_iso8601_string()
        except:
            print(self.cmsdata.lastfilecheck)
        
        self.label_lastfile.setText(lastfile)
        '''
        # Getting the Model
        data=[[],[]]
        data[0]=['1.jan','2.jan','3.jan','4.jan','5.jan']
        data[1]=[1.0,2.0,3.0,4.0,5.0]
        self.model = BachmannCMSTableModel(data)
        '''
        # Creating a QTableView
        
        self.tableView.setModel(self.tablemodel)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(1, True)
        self.tableView.setColumnHidden(2, True)

    def CloseEvent(self, event):
        print("X is clicked")
        
        self.cmsdata.update = False
        self.mdicontroller.removeMDIChild(self.objectdata)

    def onAccept(self):
        print('OK button pressed')
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,self.tablemodel,self.update)
        #self.close()
        
    def onReject(self):
        print('Cancel button pressed')
        self.update = False
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,self.tablemodel,self.update )
        #self.close()


   

    

        
