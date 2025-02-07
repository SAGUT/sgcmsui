# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_bkvcms.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_Dialog_BKVCMS(object):
    def setupUi(self, Dialog_BKVCMS):
        if not Dialog_BKVCMS.objectName():
            Dialog_BKVCMS.setObjectName(u"Dialog_BKVCMS")
        Dialog_BKVCMS.resize(900, 530)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_BKVCMS.sizePolicy().hasHeightForWidth())
        Dialog_BKVCMS.setSizePolicy(sizePolicy)
        Dialog_BKVCMS.setMinimumSize(QSize(900, 530))
        Dialog_BKVCMS.setMaximumSize(QSize(900, 530))
        self.verticalLayout = QVBoxLayout(Dialog_BKVCMS)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog_BKVCMS)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_overview = QWidget()
        self.tab_overview.setObjectName(u"tab_overview")
        self.verticalLayout_4 = QVBoxLayout(self.tab_overview)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.tab_overview)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_country = QLabel(self.widget)
        self.label_country.setObjectName(u"label_country")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_country)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_site = QLabel(self.widget)
        self.label_site.setObjectName(u"label_site")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_site)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_wtg = QLabel(self.widget)
        self.label_wtg.setObjectName(u"label_wtg")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_wtg)


        self.verticalLayout_4.addWidget(self.widget)

        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_channels = QWidget()
        self.tab_channels.setObjectName(u"tab_channels")
        self.verticalLayout_3 = QVBoxLayout(self.tab_channels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView_channels = QTableView(self.tab_channels)
        self.tableView_channels.setObjectName(u"tableView_channels")

        self.verticalLayout_3.addWidget(self.tableView_channels)

        self.tabWidget.addTab(self.tab_channels, "")
        self.tab_scalars = QWidget()
        self.tab_scalars.setObjectName(u"tab_scalars")
        self.verticalLayout_2 = QVBoxLayout(self.tab_scalars)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.tab_scalars)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_modelid = QLabel(self.widget_2)
        self.label_modelid.setObjectName(u"label_modelid")

        self.verticalLayout_5.addWidget(self.label_modelid)

        self.tableView_scalars = QTableView(self.widget_2)
        self.tableView_scalars.setObjectName(u"tableView_scalars")

        self.verticalLayout_5.addWidget(self.tableView_scalars)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_synch = QPushButton(self.widget_3)
        self.pushButton_synch.setObjectName(u"pushButton_synch")
        self.pushButton_synch.setMaximumSize(QSize(190, 16777215))

        self.verticalLayout_6.addWidget(self.pushButton_synch)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab_scalars, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog_BKVCMS)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_BKVCMS)
        self.buttonBox.accepted.connect(Dialog_BKVCMS.accept)
        self.buttonBox.rejected.connect(Dialog_BKVCMS.reject)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog_BKVCMS)
    # setupUi

    def retranslateUi(self, Dialog_BKVCMS):
        Dialog_BKVCMS.setWindowTitle(QCoreApplication.translate("Dialog_BKVCMS", u"BKV CMS", None))
        self.label.setText(QCoreApplication.translate("Dialog_BKVCMS", u"Country:", None))
        self.label_country.setText(QCoreApplication.translate("Dialog_BKVCMS", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_BKVCMS", u"Site:", None))
        self.label_site.setText(QCoreApplication.translate("Dialog_BKVCMS", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_BKVCMS", u"WTG:", None))
        self.label_wtg.setText(QCoreApplication.translate("Dialog_BKVCMS", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QCoreApplication.translate("Dialog_BKVCMS", u"Overview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_channels), QCoreApplication.translate("Dialog_BKVCMS", u"Channels", None))
        self.label_modelid.setText(QCoreApplication.translate("Dialog_BKVCMS", u"TextLabel", None))
        self.pushButton_synch.setText(QCoreApplication.translate("Dialog_BKVCMS", u"Synch", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scalars), QCoreApplication.translate("Dialog_BKVCMS", u"Scalars", None))
    # retranslateUi

