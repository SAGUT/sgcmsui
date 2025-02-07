# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_bkvscalar.ui'
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
    QFormLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Dialog_BKVScalar(object):
    def setupUi(self, Dialog_BKVScalar):
        if not Dialog_BKVScalar.objectName():
            Dialog_BKVScalar.setObjectName(u"Dialog_BKVScalar")
        Dialog_BKVScalar.resize(1130, 532)
        self.verticalLayout = QVBoxLayout(Dialog_BKVScalar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog_BKVScalar)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_description = QLineEdit(self.widget)
        self.lineEdit_description.setObjectName(u"lineEdit_description")

        self.verticalLayout_2.addWidget(self.lineEdit_description)

        self.tableView_scalars = QTableView(self.widget)
        self.tableView_scalars.setObjectName(u"tableView_scalars")

        self.verticalLayout_2.addWidget(self.tableView_scalars)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Dialog_BKVScalar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog_BKVScalar)
        self.buttonBox.accepted.connect(Dialog_BKVScalar.accept)
        self.buttonBox.rejected.connect(Dialog_BKVScalar.reject)

        QMetaObject.connectSlotsByName(Dialog_BKVScalar)
    # setupUi

    def retranslateUi(self, Dialog_BKVScalar):
        Dialog_BKVScalar.setWindowTitle(QCoreApplication.translate("Dialog_BKVScalar", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_BKVScalar", u"Model ID: ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_BKVScalar", u"Model ID:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_BKVScalar", u"Description:", None))
    # retranslateUi

