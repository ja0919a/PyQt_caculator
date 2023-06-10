# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '計算機.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(356, 402)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_result = QLineEdit(Form)
        self.lineEdit_result.setObjectName(u"lineEdit_result")
        self.lineEdit_result.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.lineEdit_result.setFont(font)
        self.lineEdit_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_result.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.lineEdit_result)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_leftBracket = QPushButton(Form)
        self.pushButton_leftBracket.setObjectName(u"pushButton_leftBracket")
        self.pushButton_leftBracket.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_leftBracket.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_leftBracket)

        self.pushButton_rightBracket = QPushButton(Form)
        self.pushButton_rightBracket.setObjectName(u"pushButton_rightBracket")
        self.pushButton_rightBracket.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setUnderline(False)
        self.pushButton_rightBracket.setFont(font2)

        self.horizontalLayout_5.addWidget(self.pushButton_rightBracket)

        self.pushButton_esc = QPushButton(Form)
        self.pushButton_esc.setObjectName(u"pushButton_esc")
        self.pushButton_esc.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.pushButton_esc)

        self.pushButton_delete = QPushButton(Form)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.pushButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_divide = QPushButton(Form)
        self.pushButton_divide.setObjectName(u"pushButton_divide")
        self.pushButton_divide.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_divide)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_multiply = QPushButton(Form)
        self.pushButton_multiply.setObjectName(u"pushButton_multiply")
        self.pushButton_multiply.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButton_multiply)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_subtract = QPushButton(Form)
        self.pushButton_subtract.setObjectName(u"pushButton_subtract")
        self.pushButton_subtract.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_3.addWidget(self.pushButton_subtract)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(0, 50))
        self.pushButton_0.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_0)

        self.pushButton_dot = QPushButton(Form)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setMinimumSize(QSize(0, 50))
        self.pushButton_dot.setFont(font2)

        self.horizontalLayout_4.addWidget(self.pushButton_dot)

        self.pushButton_enter = QPushButton(Form)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_4.addWidget(self.pushButton_enter)

        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_4.addWidget(self.pushButton_plus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8a08\u7b97\u6a5f", None))
        self.lineEdit_result.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_leftBracket.setText(QCoreApplication.translate("Form", u"(", None))
        self.pushButton_rightBracket.setText(QCoreApplication.translate("Form", u")", None))
        self.pushButton_esc.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", u"<=", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_divide.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_multiply.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_subtract.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Form", u"\u8a08\u7b97", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

