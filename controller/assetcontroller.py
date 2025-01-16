import logging
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from ui.wtg_gbx_dialog import WTG_GBX_Dialog
class AssetController:
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
        self.treewidget.customContextMenuRequested.connect(self.onCustomMenu)
        treeitems=self.cmsdb.getHierarchy('windparkroottype')
        for dbid,treeitem in treeitems.items():
            if treeitem['object_level']==1:
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(self.treewidget, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})
                if treeitem['object_type'] in self.icons:
                    if treeitem['object_type']!=1:
                        self.treenodes[dbid].setIcon(0,self.icons[treeitem['object_type']])
                    else:
                        if treeitem['object_name'] in self.icons[1]:
                            self.treenodes[dbid].setIcon(0,self.icons[1][treeitem['object_name']])
                        else:
                            self.treenodes[dbid].setIcon(0,self.icons[1]["Country"])
            else:
                parentnode=self.treenodes[treeitem['object_parent']]
                self.treenodes[dbid]=QtWidgets.QTreeWidgetItem(parentnode, [treeitem['object_name']])
                self.treenodes[dbid].setData(0,Qt.UserRole,{"id":dbid,"type":treeitem['object_type'],"parent":treeitem['object_parent']})
                if treeitem['object_type'] in self.icons:
                    if treeitem['object_type']!=1:
                        self.treenodes[dbid].setIcon(0,self.icons[treeitem['object_type']])
                    else:
                        if treeitem['object_name'] in self.icons[1]:
                            self.treenodes[dbid].setIcon(0,self.icons[1][treeitem['object_name']])
                        else:
                            self.treenodes[dbid].setIcon(0,self.icons[1]["Country"])
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
        self.icons[18]=QtGui.QIcon("ui/icons/person.png")
                       

    def mapObjectTypes(self, typecode: int):
        if typecode==1:
            return 'windparkroottype'
        elif typecode==2:
            return 'windparktype'
        elif typecode==3:
            return 'windparkobjecttype'
        elif typecode==4:
            return 'windparkobject'
        elif typecode==5:
            return 'windparkobjectattribute'
        elif typecode==6:
            return 'windparkobjectattributevalue'
        else:
            return 'unknown'
    
    
    def onitemDoubleClicked(self, item, column):
        logging.debug('onItemClicked started')
        print(item.text(0),item.data(0,Qt.UserRole))
        self.mdicontroller.addSubWindow(item.data(0,Qt.UserRole))

    def onCustomMenu(self, position):
        logging.debug('onCustomMenu started')
        #print(item.text(0),item.data(0,Qt.UserRole))
        indexes=self.treewidget.selectedIndexes()
        if not indexes is None:
            data=indexes[0].data(Qt.UserRole)
            print(data,data['id'])
            if data['id'] in self.treenodes:
                treeitem=self.treenodes[data['id']]
                if data['type']==3:
                    self.wtgContexMenu(treeitem, position)

            '''
                print(treeitem.text(0),treeitem.childCount())
                for i in range(treeitem.childCount()):
                    print(treeitem.child(i).text(0),treeitem.child(i).data(0,Qt.UserRole))
            menu = QtWidgets.QMenu()
            menu.addAction("Edit person")
            selecteditem=menu.exec_(self.treewidget.viewport().mapToGlobal(position))
            if not selecteditem is None:
                print(selecteditem.text())
            '''

    def wtgContexMenu(self,item,position):
        logging.debug('wtgContexMenu started')
        menu = QtWidgets.QMenu()
        editmenu=menu.addAction("Edit WTG")
        menu.addSeparator()
        addgearbox=menu.addAction("Add/Edit Gearbox")
        addgenerator=menu.addAction("Add/Edit Generator")
        #addgenerator.setDisabled(True)
        addbearing=menu.addAction("Add/Edit Bearing")
        selecteditem=menu.exec_(self.treewidget.viewport().mapToGlobal(position))
        children={}
        if not selecteditem is None:
            print(selecteditem.text())
            for i in range(item.childCount()):
                    print(item.child(i).text(0),item.child(i).data(0,Qt.UserRole))
                    children[item.child(i).text(0)]=item.child(i).data(0,Qt.UserRole)

        if selecteditem==addgearbox: 
            if 'Gearbox' in children:
                id=children['Gearbox']['id']
                config=self.cmsdb.getWTGGearboxes(id)
            
            dialog=WTG_GBX_Dialog(config)
            
            button=dialog.exec_()
            print('Gearbox',button)