
#!/usr/bin/env python

import sys
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '024_SOL_hard.ui'
#
# Created: Tue Nov 11 10:33:53 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.output = "0"
        self.update_text()
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(340, 216)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_output = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_output.setFont(font)
        self.label_output.setLineWidth(1)
        self.label_output.setText(_fromUtf8(""))
        self.label_output.setTextFormat(QtCore.Qt.PlainText)
        self.label_output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_output.setObjectName(_fromUtf8("label_output"))
        self.verticalLayout.addWidget(self.label_output)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.btn_1 = QtGui.QPushButton(Form)
        self.btn_1.setObjectName(_fromUtf8("btn_1"))
        self.horizontalLayout_7.addWidget(self.btn_1)
        self.btn_2 = QtGui.QPushButton(Form)
        self.btn_2.setObjectName(_fromUtf8("btn_2"))
        self.horizontalLayout_7.addWidget(self.btn_2)
        self.btn_3 = QtGui.QPushButton(Form)
        self.btn_3.setObjectName(_fromUtf8("btn_3"))
        self.horizontalLayout_7.addWidget(self.btn_3)
        self.btn_add = QtGui.QPushButton(Form)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.horizontalLayout_7.addWidget(self.btn_add)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.btn_4 = QtGui.QPushButton(Form)
        self.btn_4.setObjectName(_fromUtf8("btn_4"))
        self.horizontalLayout_6.addWidget(self.btn_4)
        self.btn_5 = QtGui.QPushButton(Form)
        self.btn_5.setObjectName(_fromUtf8("btn_5"))
        self.horizontalLayout_6.addWidget(self.btn_5)
        self.btn_6 = QtGui.QPushButton(Form)
        self.btn_6.setObjectName(_fromUtf8("btn_6"))
        self.horizontalLayout_6.addWidget(self.btn_6)
        self.btn_sub = QtGui.QPushButton(Form)
        self.btn_sub.setObjectName(_fromUtf8("btn_sub"))
        self.horizontalLayout_6.addWidget(self.btn_sub)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_7 = QtGui.QPushButton(Form)
        self.btn_7.setObjectName(_fromUtf8("btn_7"))
        self.horizontalLayout_5.addWidget(self.btn_7)
        self.btn_8 = QtGui.QPushButton(Form)
        self.btn_8.setObjectName(_fromUtf8("btn_8"))
        self.horizontalLayout_5.addWidget(self.btn_8)
        self.btn_9 = QtGui.QPushButton(Form)
        self.btn_9.setObjectName(_fromUtf8("btn_9"))
        self.horizontalLayout_5.addWidget(self.btn_9)
        self.btn_mul = QtGui.QPushButton(Form)
        self.btn_mul.setObjectName(_fromUtf8("btn_mul"))
        self.horizontalLayout_5.addWidget(self.btn_mul)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.btn_clear = QtGui.QPushButton(Form)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.btn_0 = QtGui.QPushButton(Form)
        self.btn_0.setObjectName(_fromUtf8("btn_0"))
        self.horizontalLayout_4.addWidget(self.btn_0)
        self.btn_equal = QtGui.QPushButton(Form)
        self.btn_equal.setObjectName(_fromUtf8("btn_equal"))
        self.horizontalLayout_4.addWidget(self.btn_equal)
        self.btn_div = QtGui.QPushButton(Form)
        self.btn_div.setObjectName(_fromUtf8("btn_div"))
        self.horizontalLayout_4.addWidget(self.btn_div)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TPayne Calculator!", None))
        self.btn_1.setText(_translate("Form", "1", None))
        self.btn_2.setText(_translate("Form", "2", None))
        self.btn_3.setText(_translate("Form", "3", None))
        self.btn_add.setText(_translate("Form", "+", None))
        self.btn_4.setText(_translate("Form", "4", None))
        self.btn_5.setText(_translate("Form", "5", None))
        self.btn_6.setText(_translate("Form", "6", None))
        self.btn_sub.setText(_translate("Form", "-", None))
        self.btn_7.setText(_translate("Form", "7", None))
        self.btn_8.setText(_translate("Form", "8", None))
        self.btn_9.setText(_translate("Form", "9", None))
        self.btn_mul.setText(_translate("Form", "*", None))
        self.btn_clear.setText(_translate("Form", "CLEAR", None))
        self.btn_0.setText(_translate("Form", "0", None))
        self.btn_equal.setText(_translate("Form", "=", None))
        self.btn_div.setText(_translate("Form", "/", None))

    @QtCore.pyqtSignature("on_btn_1_clicked()")
    def btn_1_fun(self):
        self.output += '1'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_2_clicked()")
    def btn_2_fun(self):
        self.output += '2'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_3_clicked()")
    def btn_3_fun(self):
        self.output += '3'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_4_clicked()")
    def btn_4_fun(self):
        self.output += '4'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_5_clicked()")
    def btn_5_fun(self):
        self.output += '5'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_6_clicked()")
    def btn_6_fun(self):
        self.output += '6'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_7_clicked()")
    def btn_7_fun(self):
        self.output += '7'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_8_clicked()")
    def btn_8_fun(self):
        self.output += '8'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_9_clicked()")
    def btn_9_fun(self):
        self.output += '9'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_0_clicked()")
    def btn_0_fun(self):
        self.output += '0'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_add_clicked()")
    def btn_add_fun(self):
        if self.output_check():
            self.output += '+'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_sub_clicked()")
    def btn_sub_fun(self):
        if self.output_check():
            self.output += '-'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_div_clicked()")
    def btn_div_fun(self):
        if self.output_check():
            self.output += '/'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_mul_clicked()")
    def btn_mul_fun(self):
        if self.output_check():
            self.output += '*'
        self.update_text()

    @QtCore.pyqtSignature("on_btn_equal_clicked()")
    def btn_equal_fun(self):
        self.output = str(eval(self.output))
        self.update_text()

    @QtCore.pyqtSignature("on_btn_clear_clicked()")
    def btn_clear_fun(self):
        self.output = '0'
        self.update_text()

    def output_check(self):
        digit = self.output[-1]
        return digit not in ['+', '-', '*', '/']

    def update_text(self):
        if len(self.output) >1:
            if self.output[0] == '0':
                self.output = self.output[1:]
        self.label_output.setText(_translate(
                    "Form", self.output, None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())