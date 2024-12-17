# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_site.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SiteDialog(object):
    def setupUi(self, SiteDialog):
        if not SiteDialog.objectName():
            SiteDialog.setObjectName(u"SiteDialog")
        SiteDialog.resize(652, 498)
        SiteDialog.setMaximumSize(QSize(16777215, 651))
        self.verticalLayout = QVBoxLayout(SiteDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SiteDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_overview = QWidget()
        self.tab_overview.setObjectName(u"tab_overview")
        self.verticalLayout_2 = QVBoxLayout(self.tab_overview)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tab_overview)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 5, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 6, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout.addWidget(self.spinBox_2, 7, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout.addWidget(self.spinBox_3, 8, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.frame)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 9, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.frame)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout.addWidget(self.comboBox_5, 10, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFrameShape(QFrame.Shape.Box)

        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 11, 1, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.frame)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.gridLayout.addWidget(self.dateEdit_2, 12, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_contacts = QWidget()
        self.tab_contacts.setObjectName(u"tab_contacts")
        self.verticalLayout_3 = QVBoxLayout(self.tab_contacts)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.tab_contacts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(5, 11, 601, 381))

        self.verticalLayout_3.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_contacts, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit_Description = QTextEdit(self.tab)
        self.textEdit_Description.setObjectName(u"textEdit_Description")

        self.horizontalLayout.addWidget(self.textEdit_Description)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(SiteDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SiteDialog)
        self.buttonBox.accepted.connect(SiteDialog.accept)
        self.buttonBox.rejected.connect(SiteDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SiteDialog)
    # setupUi

    def retranslateUi(self, SiteDialog):
        SiteDialog.setWindowTitle(QCoreApplication.translate("SiteDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SiteDialog", u"Aura ID", None))
        self.label_2.setText(QCoreApplication.translate("SiteDialog", u"Latitude", None))
        self.label_3.setText(QCoreApplication.translate("SiteDialog", u"Longitude", None))
        self.label_4.setText(QCoreApplication.translate("SiteDialog", u"OEM", None))
        self.label_5.setText(QCoreApplication.translate("SiteDialog", u"No. of Turbines", None))
        self.label_6.setText(QCoreApplication.translate("SiteDialog", u"Data Connection", None))
        self.label_7.setText(QCoreApplication.translate("SiteDialog", u"Monitoring", None))
        self.label_8.setText(QCoreApplication.translate("SiteDialog", u"Grid Frequency", None))
        self.label_9.setText(QCoreApplication.translate("SiteDialog", u"SK Ownership", None))
        self.label_10.setText(QCoreApplication.translate("SiteDialog", u"Site Operation", None))
        self.label_11.setText(QCoreApplication.translate("SiteDialog", u"Site Maintenance", None))
        self.label_12.setText(QCoreApplication.translate("SiteDialog", u"End of Warranty", None))
        self.label_13.setText(QCoreApplication.translate("SiteDialog", u"End of CMS Service", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QCoreApplication.translate("SiteDialog", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contacts), QCoreApplication.translate("SiteDialog", u"Contacts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SiteDialog", u"Description", None))
    # retranslateUi

