import logging
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from ui.wtgtype_dialog import WTGTypeDialog
from ui.testdialog import TestDialog
from .subcontroller.wtgtypecontroller import WTGTypeController
from .subcontroller.bachmanncontroller import BachmannCMSController
from .subcontroller.bkvcontroller import BKVCMSController
class MDIController:
    def __init__(self, mdiArea,cmsdb,auraapi):
        self.cmsdb = cmsdb
        self.auraapi=auraapi
        self.mdiArea = mdiArea
        self.children={}
        self.subcontroller={}
        self.setupSubController()

    def setupSubController(self):
        self.subcontroller[28]=WTGTypeController(self.cmsdb,self) 
        self.subcontroller[4]=BKVCMSController(self.cmsdb,self)
        self.subcontroller[6]=BachmannCMSController(self.cmsdb,self)  
        


    def addSubWindow(self,objectdata):
        print("request for subwindow: ",objectdata)
        title = "Type: "+str(objectdata['type'])+" ID: "+str(objectdata['id'])
        if not objectdata['id'] in self.children:
            sub=None
            #decide which dialog to generate
            if objectdata['type'] in self.subcontroller:
                sub=self.subcontroller[objectdata['type']].getDialog(objectdata)
           
            if not sub is None:
                self.children[objectdata['id']] = self.mdiArea.addSubWindow(sub)
                self.children[objectdata['id']].setWindowFlag(Qt.WindowFlags.WindowMinimizeButtonHint, False)
                self.children[objectdata['id']].setWindowFlag(Qt.WindowFlags.WindowMaximizeButtonHint , False)
                self.children[objectdata['id']].setWindowFlag(Qt.WindowFlags.WindowCloseButtonHint  , False)
                sub.exec()
        else:
            self.mdiArea.setActiveSubWindow(self.children[objectdata['id']])
            self.children[objectdata['id']].activateWindow()


    def mdiChildCloseEvent(self,event):
        print(event.type())
        print('close event')

    def closeSubWindow(self,objectdata,payload,update=False):
        print(payload,update)
        if objectdata['id'] in self.children:
            self.children[objectdata['id']].close()
            if update:
                print('update')
                if objectdata['type'] in self.subcontroller:
                    self.subcontroller[objectdata['type']].saveParameter(objectdata,payload)
                    
            else:
                print('no update')
            
    
    def removeMDIChild(self,objectdata):
        print("removing: ",objectdata)
        if objectdata['id'] in self.children:
            del self.children[objectdata['id']]

    def getDialog(self,objectdata):
        if objectdata['type'] in self.subcontroller:
            return self.subcontroller[objectdata['type']].getDialog(objectdata)

    def getWTGTypeDialog(self,objectdata):
        wtgtype=self.subcontroller[28].getParameter(objectdata)
        #print(wtgtype)
        if not wtgtype is None:
            sub=WTGTypeDialog(objectdata,wtgtype,self)
            sub.label_Company.setText(wtgtype.company)
            sub.setWindowTitle("WTG Type: "+str(wtgtype.name))                
            return sub




    def getObjectData(self,objectdata):
        pass










    