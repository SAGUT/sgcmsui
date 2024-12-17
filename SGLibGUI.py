import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#from sgcmslib.database.cmsdbclient import CMSDBClient

#dbclient = CMSDBClient("azure")
#dbclient.getHierarchy('cmsconfigurations')
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import sys
from ui.cmsmanagermain import CMSManagerMain

app = QtWidgets.QApplication(sys.argv)
window = CMSManagerMain()
window.show()
app.exec()