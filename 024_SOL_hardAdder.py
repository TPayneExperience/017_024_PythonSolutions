#!/usr/bin/env python

sourceFile = open('024_SOL_hardRAW.py', 'r')
sourceCode = sourceFile.read()
sourceFile.close()

sourceCodeSplit = sourceCode.split('class Ui_Form(object):')

beginningLines = '''
#!/usr/bin/env python

import sys
'''

constructorCode = '''
class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.output = "0"
        self.update_text()
        '''

endFunctionsFile = open('024_SOL_hardFunctions.py', 'r')
finalLines = endFunctionsFile.read()
endFunctionsFile.close()

f = open('024_SOL_hardFinal.py', 'w')
f.write(beginningLines)
f.write(sourceCodeSplit[0])
f.write(constructorCode)
f.write(sourceCodeSplit[1])
f.write(finalLines)
f.close()
