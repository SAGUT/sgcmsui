import logging
from PySide6.QtWidgets import QDialog
from .base.dialog_wtg_gbx import Ui_dialog_wtg_gbx

class WTG_GBX_Dialog(QDialog,Ui_dialog_wtg_gbx):
    def __init__(self,cmsdb,gbxitem):
        super().__init__()
        #self.objectName = 'dialog_wtg_gbx'
        logging.debug('WTG_GBX_Dialog started')
        self.setupUi(self)
        self.initUI()
    def initUI(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('initUI started')
        self.buttonBox.accepted.connect(self.onAccept)
        self.buttonBox.rejected.connect(self.onReject)
        self.logger.debug('initUI finished')

    def onAccept(self):
        print('OK button pressed')
        
    def onReject(self):
        print('Cancel button pressed')