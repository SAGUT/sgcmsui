import logging
from PySide6.QtWidgets import QDialog
from PySide6 import QtGui, QtCore
from .base.dialog_wtgtype import Ui_Dialog_WTGType

class WTGTypeDialog(QDialog,Ui_Dialog_WTGType):
    def __init__(self,objectdata,wtgtypedata,mdicontroller):
        super().__init__()
        
        self.wtgtypedata = wtgtypedata
        #print(wtgtypedata)
        self.objectdata = objectdata
        self.mdicontroller = mdicontroller
        self.wtgtypedata.update = False
        logging.debug('WTGTypeDialog started')
        self.closeHandled=False
        #print(self.windowFlags())
        self.setupUi(self)
        
        self.initUI()
    def initUI(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('initUI started')
        #presets
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | ~QtCore.Qt.WindowMinMaxButtonsHint)
        self.lineEdit_name.setText(str(self.wtgtypedata.name))
        self.lineEdit_nompower.setText(str(self.wtgtypedata.nominalpower))
        self.lineEdit_nompower.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_rotor.setText(str(self.wtgtypedata.rotordiameter))
        self.lineEdit_rotor.setValidator(QtGui.QDoubleValidator())
        if not self.wtgtypedata.drive is None:
            self.lineEdit_drive.setText(str(self.wtgtypedata.drive))
        if not self.wtgtypedata.windclass is None:
            self.lineEdit_wtgclass.setText(str(self.wtgtypedata.windclass))
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.lineEdit_name.textChanged.connect(self.onNameChanged)
        self.lineEdit_nompower.textChanged.connect(self.onNomPowerChanged)
        self.lineEdit_rotor.textChanged.connect(self.onRotorChanged)
        self.lineEdit_wtgclass.textChanged.connect(self.onWTGTypeClassChanged)
        self.lineEdit_drive.textChanged.connect(self.onDriveChanged)
        self.closeEvent = self.CloseEvent
        self.logger.debug('initUI finished')
    
    def onNameChanged(self):
        try:
            
            self.wtgtypedata.name=self.lineEdit_name.text()
            self.wtgtypedata.update = True
            #self.lineEdit_wtgclass.setText(str(value))
        except:
            print('WTGType name Class must be a string')
        print('WTG Class changed to: '+self.lineEdit_name.text())
    
    def onNomPowerChanged(self):
        try:
            value=float(self.lineEdit_nompower.text())
            #self.lineEdit_nompower.setText(str(value))
            self.wtgtypedata.nominalpower=value
            self.wtgtypedata.update = True
        except:
            print('Nominal Power must be a number')
        print('Nominal Power changed to: '+self.lineEdit_nompower.text())

    def onRotorChanged(self):
        try:
            value=float(self.lineEdit_rotor.text())
            self.wtgtypedata.rotordiameter=value
            self.wtgtypedata.update = True
            #self.lineEdit_rotor.setText(str(value))
        except:
            print('Rotor Diameter must be a number')
        print('Rotor Diameter changed to: '+self.lineEdit_rotor.text())

    def onWTGTypeClassChanged(self):
        try:
            
            self.wtgtypedata.windclass=self.lineEdit_wtgclass.text()
            self.wtgtypedata.update = True
            #self.lineEdit_wtgclass.setText(str(value))
        except:
            print('WTG Class must be a string')
        print('WTG Class changed to: '+self.lineEdit_wtgclass.text())

    def onDriveChanged(self):
        try:
            
            self.wtgtypedata.drive=self.lineEdit_drive.text()
            self.wtgtypedata.update = True
            #self.lineEdit_drive.setText(str(value))
        except:
            print('Drive must be a string')
        print('Drive changed to: '+self.lineEdit_drive.text())

    def CloseEvent(self, event):
        print("X is clicked")
        
        self.wtgtypedata.update = False
        self.mdicontroller.removeMDIChild(self.objectdata)

    def onAccept(self):
        print('OK button pressed')
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,self.wtgtypedata,self.update)
        #self.close()
        
    def onReject(self):
        print('Cancel button pressed')
        self.update = False
        #self.close()
        self.closeHandled=True
        self.mdicontroller.closeSubWindow(self.objectdata,self.wtgtypedata,self.update )
        #self.close()
