# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_bachmanncms.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QSizePolicy,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Dialog_BachmannCMS(object):
    def setupUi(self, Dialog_BachmannCMS):
        if not Dialog_BachmannCMS.objectName():
            Dialog_BachmannCMS.setObjectName(u"Dialog_BachmannCMS")
        Dialog_BachmannCMS.resize(800, 530)
        Dialog_BachmannCMS.setMinimumSize(QSize(800, 530))
        Dialog_BachmannCMS.setMaximumSize(QSize(800, 530))
        self.verticalLayout = QVBoxLayout(Dialog_BachmannCMS)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog_BachmannCMS)
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
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_site = QLabel(self.frame_2)
        self.label_site.setObjectName(u"label_site")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_site)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_wtg = QLabel(self.frame_2)
        self.label_wtg.setObjectName(u"label_wtg")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_wtg)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_apiid = QLineEdit(self.frame_2)
        self.lineEdit_apiid.setObjectName(u"lineEdit_apiid")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_apiid)

        self.lineEdit_identity = QLineEdit(self.frame_2)
        self.lineEdit_identity.setObjectName(u"lineEdit_identity")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_identity)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_nordexname = QLineEdit(self.frame_2)
        self.lineEdit_nordexname.setObjectName(u"lineEdit_nordexname")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_nordexname)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_name = QLineEdit(self.frame_2)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.checkBox_commissioned = QCheckBox(self.frame_2)
        self.checkBox_commissioned.setObjectName(u"checkBox_commissioned")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.checkBox_commissioned)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_skcmsname = QLineEdit(self.frame_2)
        self.lineEdit_skcmsname.setObjectName(u"lineEdit_skcmsname")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_skcmsname)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.label_lastfile = QLabel(self.frame_2)
        self.label_lastfile.setObjectName(u"label_lastfile")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_lastfile)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_channels = QWidget()
        self.tab_channels.setObjectName(u"tab_channels")
        self.verticalLayout_3 = QVBoxLayout(self.tab_channels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.tab_channels)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.tabWidget.addTab(self.tab_channels, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog_BachmannCMS)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_BachmannCMS)
        self.buttonBox.accepted.connect(Dialog_BachmannCMS.accept)
        self.buttonBox.rejected.connect(Dialog_BachmannCMS.reject)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog_BachmannCMS)
    # setupUi

    def retranslateUi(self, Dialog_BachmannCMS):
        Dialog_BachmannCMS.setWindowTitle(QCoreApplication.translate("Dialog_BachmannCMS", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"Site:", None))
        self.label_site.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"WTG:", None))
        self.label_wtg.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"API id:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"Nordex name:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"Identity:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"commissioned:", None))
        self.checkBox_commissioned.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"SK CMS name:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"Last File:", None))
        self.label_lastfile.setText(QCoreApplication.translate("Dialog_BachmannCMS", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QCoreApplication.translate("Dialog_BachmannCMS", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_channels), QCoreApplication.translate("Dialog_BachmannCMS", u"Channels", None))
    # retranslateUi

