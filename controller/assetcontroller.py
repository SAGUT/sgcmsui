import logging
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

class AssetController:
    def __init__(self, treewidget,cmsdb,mdicontroller):
        self.cmsdb = cmsdb
        self.treewidget = treewidget
        self.mdicontroller = mdicontroller
        self.treenodes={}
        self.initTree()

    def initTree(self):
        logging.debug('initTree started')
        self.treewidget.itemDoubleClicked.connect(self.onitemDoubleClicked)
        treeitems=self.cmsdb.getHierarchy('windparkroottype')
        for dbid,treeitem in treeitems.items():
            if treeitem['object_level']==1:
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(self.treewidget, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})
            else:
                parentnode=self.treenodes[treeitem['object_parent']]
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(parentnode, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})

    def onitemDoubleClicked(self, item, column):
        logging.debug('onItemClicked started')
        print(item.text(0),item.data(0,Qt.UserRole))