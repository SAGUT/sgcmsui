# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QSizePolicy, QSplitter, QStatusBar, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1615, 983)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.component_treewidget = QTabWidget(self.frame)
        self.component_treewidget.setObjectName(u"component_treewidget")
        self.component_treewidget.setMaximumSize(QSize(16777214, 16777215))
        self.component_treewidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tab_assets = QWidget()
        self.tab_assets.setObjectName(u"tab_assets")
        self.verticalLayout = QVBoxLayout(self.tab_assets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.asset_treewidget = QTreeWidget(self.tab_assets)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.asset_treewidget.setHeaderItem(__qtreewidgetitem)
        self.asset_treewidget.setObjectName(u"asset_treewidget")
        self.asset_treewidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.asset_treewidget.setRootIsDecorated(False)
        self.asset_treewidget.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.asset_treewidget)

        self.component_treewidget.addTab(self.tab_assets, "")
        self.tab_components = QWidget()
        self.tab_components.setObjectName(u"tab_components")
        self.verticalLayout_2 = QVBoxLayout(self.tab_components)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget_components = QTreeWidget(self.tab_components)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget_components.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget_components.setObjectName(u"treeWidget_components")
        self.treeWidget_components.setHeaderHidden(True)

        self.verticalLayout_2.addWidget(self.treeWidget_components)

        self.component_treewidget.addTab(self.tab_components, "")
        self.tab_configurations = QWidget()
        self.tab_configurations.setObjectName(u"tab_configurations")
        self.verticalLayout_3 = QVBoxLayout(self.tab_configurations)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeWidget_configurations = QTreeWidget(self.tab_configurations)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.treeWidget_configurations.setHeaderItem(__qtreewidgetitem2)
        self.treeWidget_configurations.setObjectName(u"treeWidget_configurations")
        self.treeWidget_configurations.setHeaderHidden(True)

        self.verticalLayout_3.addWidget(self.treeWidget_configurations)

        self.component_treewidget.addTab(self.tab_configurations, "")
        self.tab_contacts = QWidget()
        self.tab_contacts.setObjectName(u"tab_contacts")
        self.verticalLayout_4 = QVBoxLayout(self.tab_contacts)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.treeWidget_contacts = QTreeWidget(self.tab_contacts)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.treeWidget_contacts.setHeaderItem(__qtreewidgetitem3)
        self.treeWidget_contacts.setObjectName(u"treeWidget_contacts")
        self.treeWidget_contacts.setHeaderHidden(True)

        self.verticalLayout_4.addWidget(self.treeWidget_contacts)

        self.component_treewidget.addTab(self.tab_contacts, "")

        self.horizontalLayout.addWidget(self.component_treewidget)

        self.splitter.addWidget(self.frame)
        self.mdiArea = QMdiArea(self.splitter)
        self.mdiArea.setObjectName(u"mdiArea")
        self.splitter.addWidget(self.mdiArea)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1615, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.component_treewidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CMS Manager", None))
        self.component_treewidget.setTabText(self.component_treewidget.indexOf(self.tab_assets), QCoreApplication.translate("MainWindow", u"Assets", None))
        self.component_treewidget.setTabText(self.component_treewidget.indexOf(self.tab_components), QCoreApplication.translate("MainWindow", u"Compoments", None))
        self.component_treewidget.setTabText(self.component_treewidget.indexOf(self.tab_configurations), QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.component_treewidget.setTabText(self.component_treewidget.indexOf(self.tab_contacts), QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

