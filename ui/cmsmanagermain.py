from .Base.cmsmanager import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from ..Data.cmsdb import CMSDB_Client
from ..Controller.wtgtreecontroller import WTGTreeController
from ..Controller.componenttreecontroller import ComponentTreeController
from ..Controller.modeltreecontroller import ModelTreeController
from ..Controller.mdicontroller import MDIController
from ..Controller.contacttreecontroller import ContactTreeController

class CMSManagerMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, cmsdb: CMSDB_Client,parent=None):
        super().__init__()
        logging.debug('CMSManagerMain started')
        self.cmsdb = cmsdb
        
        self.setupUi(self)
        self.initUI()