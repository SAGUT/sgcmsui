import logging
from .base.mainwindowbase import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from pathlib import Path
'''
from ..Data.cmsdb import CMSDB_Client
from ..Controller.wtgtreecontroller import WTGTreeController
from ..Controller.componenttreecontroller import ComponentTreeController
from ..Controller.modeltreecontroller import ModelTreeController
from ..Controller.mdicontroller import MDIController
from ..Controller.contacttreecontroller import ContactTreeController
'''
from controller.assetcontroller import AssetController
from controller.componentcontroller import ComponentController
from controller.configurationcontroller import ConfigurationController
from controller.contactcontroller import ContactController
from sgcmslib.database.cmsdbclient import CMSDBClient
from sgcmslib.api.aura.client import AuraClient
from controller.mdicontroller import MDIController
class CMSManagerMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__()
        logging.debug('CMSManagerMain started')
        self.cmsdb = CMSDBClient("azure")
        self.auraapi=AuraClient()
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        #self.logger = logging.getLogger(__name__)
        #self.logger.debug('initUI started')
        self.mdiController = MDIController(self.mdiArea,self.cmsdb,self.auraapi)
        self.assetTreeController = AssetController(self.asset_treewidget,self.cmsdb,self.mdiController)
        self.componentTreeController=ComponentController(self.treeWidget_components,self.cmsdb,self.mdiController)
        self.configurationTreeController=ConfigurationController(self.treeWidget_configurations,self.cmsdb,self.mdiController)
        self.contactTreeController=ContactController(self.treeWidget_contacts,self.cmsdb,self.mdiController)

        path_to_icon = 'ui/icons/ninja-icon512.png' #the path to your icon file, relative to the project root
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData( Path( path_to_icon ).read_bytes() )
        appIcon = QtGui.QIcon(pixmap)
        self.setWindowIcon(appIcon)
