# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_wtgtype.ui'
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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_WTGType(object):
    def setupUi(self, Dialog_WTGType):
        if not Dialog_WTGType.objectName():
            Dialog_WTGType.setObjectName(u"Dialog_WTGType")
        Dialog_WTGType.resize(450, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_WTGType.sizePolicy().hasHeightForWidth())
        Dialog_WTGType.setSizePolicy(sizePolicy)
        Dialog_WTGType.setMinimumSize(QSize(450, 200))
        Dialog_WTGType.setMaximumSize(QSize(450, 250))
        Dialog_WTGType.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.verticalLayout = QVBoxLayout(Dialog_WTGType)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_Company = QLabel(Dialog_WTGType)
        self.label_Company.setObjectName(u"label_Company")
        font = QFont()
        font.setPointSize(14)
        self.label_Company.setFont(font)

        self.verticalLayout.addWidget(self.label_Company)

        self.frame = QFrame(Dialog_WTGType)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_wtgclass = QLineEdit(self.frame)
        self.lineEdit_wtgclass.setObjectName(u"lineEdit_wtgclass")

        self.gridLayout.addWidget(self.lineEdit_wtgclass, 4, 1, 1, 2)

        self.lineEdit_nompower = QLineEdit(self.frame)
        self.lineEdit_nompower.setObjectName(u"lineEdit_nompower")

        self.gridLayout.addWidget(self.lineEdit_nompower, 1, 1, 1, 2)

        self.lineEdit_rotor = QLineEdit(self.frame)
        self.lineEdit_rotor.setObjectName(u"lineEdit_rotor")

        self.gridLayout.addWidget(self.lineEdit_rotor, 2, 1, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_drive = QLineEdit(self.frame)
        self.lineEdit_drive.setObjectName(u"lineEdit_drive")

        self.gridLayout.addWidget(self.lineEdit_drive, 5, 1, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.frame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialog_WTGType)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_WTGType)
        self.buttonBox.accepted.connect(Dialog_WTGType.accept)
        self.buttonBox.rejected.connect(Dialog_WTGType.reject)

        QMetaObject.connectSlotsByName(Dialog_WTGType)
    # setupUi

    def retranslateUi(self, Dialog_WTGType):
        Dialog_WTGType.setWindowTitle(QCoreApplication.translate("Dialog_WTGType", u"WTG Type", None))
        self.label_Company.setText(QCoreApplication.translate("Dialog_WTGType", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_WTGType", u"Rotor Diameter", None))
        self.label.setText(QCoreApplication.translate("Dialog_WTGType", u"Nominal power", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_WTGType", u"Drive", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_WTGType", u"WTG Class", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_WTGType", u"Name", None))
    # retranslateUi

