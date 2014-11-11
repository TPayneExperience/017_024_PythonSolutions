
#!/usr/bin/env python

import sys
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '024_SOL_easy.ui'
#
# Created: Tue Nov 11 10:40:10 2014
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
        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_ham = QtGui.QPushButton(Form)
        self.btn_ham.setObjectName(_fromUtf8("btn_ham"))
        self.verticalLayout.addWidget(self.btn_ham)
        self.btn_superHam = QtGui.QPushButton(Form)
        self.btn_superHam.setObjectName(_fromUtf8("btn_superHam"))
        self.verticalLayout.addWidget(self.btn_superHam)
        self.btn_yellow = QtGui.QPushButton(Form)
        self.btn_yellow.setObjectName(_fromUtf8("btn_yellow"))
        self.verticalLayout.addWidget(self.btn_yellow)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_ham.setText(_translate("Form", "Print Ham", None))
        self.btn_superHam.setText(_translate("Form", "Print Super Ham", None))
        self.btn_yellow.setText(_translate("Form", "Print ???", None))


    @QtCore.pyqtSignature("on_btn_ham_clicked()")
    def printHam(self):
        print ("ham!")

    @QtCore.pyqtSignature("on_btn_superHam_clicked()")
    def printSuperHam(self):
        print ("SUPER HAM!")

    @QtCore.pyqtSignature("on_btn_yellow_clicked()")
    def printYellow(self):
        print ("My favorite smell is yellow!")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
