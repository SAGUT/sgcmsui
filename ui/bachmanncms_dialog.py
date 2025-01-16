import logging
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6 import QtGui, QtCore
from .base.dialog_bachmanncms import Ui_Dialog_BachmannCMS
from.models.bachmannchannelmodel import BachmannCMSTableModel
import pendulum

class BachmannCMSDialog(QDialog,Ui_Dialog_BachmannCMS):
    def __init__(self,objectdata,cmsdata,mdicontroller):
        super().__init__()
        self.objectdata = objectdata
        self.cmsdata = cmsdata
        self.mdicontroller = mdicontroller
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('initUI started')
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
        # Getting the Model
        data=[[],[]]
        data[0]=['1.jan','2.jan','3.jan','4.jan','5.jan']
        data[1]=['1','2','3','4','5']
        self.model = BachmannCMSTableModel(data)

        # Creating a QTableView
        
        self.tableView.setModel(self.model)

        #self.publishTable()


    def publishTable(self):
        self.logger.debug('publishTable started')
        
        colnames=['number','identifier','label','speedlabel','powerlabel']
        for i in range(0,5):
            self.tableView.a  .insertColumn(i)
            self.tableView.setHorizontalHeaderItem(i, QListWidgetItem(colnames[i]))
        '''
        for key,value in self.cmsdata.__dict__.items():
            if key not in ['id','site','wtg','name','apiid','identity','vesname','commissioned','lastfilecheck']:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QListWidgetItem(key))
                self.tableWidget.setItem(rowPosition, 1, QListWidgetItem(str(value)))
        '''
        self.logger.debug('publishTable finished')

        
