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