import logging
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

class ContactController:
    def __init__(self, treewidget,cmsdb,mdicontroller):
        self.cmsdb = cmsdb
        self.treewidget = treewidget
        self.mdicontroller = mdicontroller
        self.treenodes={}
        self.objecttypes={}
        self.icons={}
        self.loadIcons()
        self.initTree()

    def initTree(self):
        logging.debug('initTree started')
        self.treewidget.itemDoubleClicked.connect(self.onitemDoubleClicked)
        #self.treewidget.customContextMenuRequested.connect(self.onCustomMenu)
        treeitems=self.cmsdb.getHierarchy('contactroot')
        for dbid,treeitem in treeitems.items():
            print(treeitem)
            if treeitem['object_level']==1:
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(self.treewidget, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})
                if treeitem['object_type'] in self.icons:
                    self.treenodes[dbid].setIcon(0,self.icons[treeitem['object_type']])
            else:
                parentnode=self.treenodes[treeitem['object_parent']]
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(parentnode, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})
                if treeitem['object_type'] in self.icons:
                    self.treenodes[dbid].setIcon(0,self.icons[treeitem['object_type']])
                if treeitem['object_type'] in self.objecttypes:

                    self.treenodes[dbid].setToolTip(0,self.objecttypes[treeitem['object_type']]["objecttype_description"])

    def loadIcons(self):
        logging.debug('loadIcons started')
        self.objecttypes=self.cmsdb.getObjectTypes()
        self.icons[2]=QtGui.QIcon("ui/icons/site.png")
        self.icons[3]=QtGui.QIcon("ui/icons/wtg64.png")
        self.icons[4]=QtGui.QIcon("ui/icons/cms64.png")
        self.icons[5]=QtGui.QIcon("ui/icons/cms64.png")
        self.icons[6]=QtGui.QIcon("ui/icons/cms64.png")
        self.icons[7]=QtGui.QIcon("ui/icons/person.png")
        self.icons[8]=QtGui.QIcon("ui/icons/company.png")
        self.icons[9]=QtGui.QIcon("ui/icons/gearbox64.png")
        self.icons[10]=QtGui.QIcon("ui/icons/generator64.png")
        self.icons[11]=QtGui.QIcon("ui/icons/bearing64.png")
        self.icons[1]={"Country":QtGui.QIcon("ui/icons/Countries/Country.png"),
                       "Brazil":QtGui.QIcon("ui/icons/Countries/Brazil.png"),
                            "Germany":QtGui.QIcon("ui/icons/Countries/Germany.png"),
                            "Sweden":QtGui.QIcon("ui/icons/Countries/Sweden.png"),
                            "Norway":QtGui.QIcon("ui/icons/Countries/Norway.png"),
                            "Ireland":QtGui.QIcon("ui/icons/Countries/Ireland.png"),
                            "UK":QtGui.QIcon("ui/icons/Countries/UK.png")}
        self.icons[17]=QtGui.QIcon("ui/icons/group.png")
        self.icons[18]=QtGui.QIcon("ui/icons/person.png")

    def onitemDoubleClicked(self, item, column):
        logging.debug('onItemClicked started')
        print(item.text(0),item.data(0,Qt.UserRole))