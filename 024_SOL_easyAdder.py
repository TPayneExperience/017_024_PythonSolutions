#!/usr/bin/env python

# -- MEDIUM --
beginningLines = '''
#!/usr/bin/env python

import sys
'''

finalLines = '''
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
'''

sourceFile = open('024_SOL_easyRAW.py', 'r')
lines = sourceFile.read()
sourceFile.close()

parts = lines.split('class Ui_Form(object):')

constructorCode = '''
class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        '''

f = open('024_SOL_easyFinal.py', 'w')
f.write(beginningLines)
f.write(parts[0])
f.write(constructorCode)
f.write(parts[1])
f.write(finalLines)
f.close()
