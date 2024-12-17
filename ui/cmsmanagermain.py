import logging
from .base.mainwindowbase import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
'''
from ..Data.cmsdb import CMSDB_Client
from ..Controller.wtgtreecontroller import WTGTreeController
from ..Controller.componenttreecontroller import ComponentTreeController
from ..Controller.modeltreecontroller import ModelTreeController
from ..Controller.mdicontroller import MDIController
from ..Controller.contacttreecontroller import ContactTreeController
'''
from controller.assetcontroller import AssetController
from sgcmslib.database.cmsdbclient import CMSDBClient
class CMSManagerMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__()
        logging.debug('CMSManagerMain started')
        self.cmsdb = CMSDBClient("azure")
       
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        #self.logger = logging.getLogger(__name__)
        #self.logger.debug('initUI started')
        #self.mdiController = MDIController(self.mdiArea,self.cmsdb)
        self.assetTreeController = AssetController(self.asset_treewidget,self.cmsdb,None)
        #self.componentTreeController = ComponentTreeController(self.treeWidget_components,self.cmsdb,self.mdiController)
        #self.moodelTreeController = ModelTreeController(self.treeWidget_model,self.cmsdb,self.mdiController)
        #self.contactTreeController = ContactTreeController(self.treeWidget_contact,self.cmsdb,self.mdiController)
        #self.logger.debug('initUI finished')