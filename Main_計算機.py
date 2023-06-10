from PySide6.QtWidgets import QApplication,QMainWindow,QWidget
from Ui_計算機 import Ui_Form

class MyWindow(Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result=''
        self.bind()
    def bind(self):
        self.pushButton_0.clicked.connect(lambda:self.addtext(0))
        self.pushButton_1.clicked.connect(lambda:self.addtext(1))
        self.pushButton_2.clicked.connect(lambda:self.addtext(2))
        self.pushButton_3.clicked.connect(lambda:self.addtext(3))
        self.pushButton_4.clicked.connect(lambda:self.addtext(4))
        self.pushButton_5.clicked.connect(lambda:self.addtext(5))
        self.pushButton_6.clicked.connect(lambda:self.addtext(6))
        self.pushButton_7.clicked.connect(lambda:self.addtext(7))
        self.pushButton_8.clicked.connect(lambda:self.addtext(8))
        self.pushButton_9.clicked.connect(lambda:self.addtext(9))
        self.pushButton_plus.clicked.connect(lambda:self.addtext('+'))
        self.pushButton_subtract.clicked.connect(lambda:self.addtext('-'))
        self.pushButton_multiply.clicked.connect(lambda:self.addtext('*'))
        self.pushButton_divide.clicked.connect(lambda:self.addtext('/'))
        self.pushButton_dot.clicked.connect(lambda:self.addtext('.'))
        self.pushButton_leftBracket.clicked.connect(lambda:self.addtext('('))
        self.pushButton_rightBracket.clicked.connect(lambda:self.addtext(')'))
        self.pushButton_delete.clicked.connect(lambda:self.deltext())
        self.pushButton_esc.clicked.connect(lambda:self.delall())
        self.pushButton_enter.clicked.connect(lambda:self.calculate())
    def addtext(self,input):
        self.lineEdit_result.clear()
        input=str(input)
        self.result+=input
        self.lineEdit_result.setText(self.result)
    def deltext(self):
        self.lineEdit_result.clear()
        self.result=self.result[:-1]
        if self.result=='':
            self.lineEdit_result.setText('0')
        else:
            self.lineEdit_result.setText(self.result)
    def delall(self):
        self.lineEdit_result.clear()
        self.result=''
        self.lineEdit_result.setText('0')
    def calculate(self):
        self.lineEdit_result.clear()
        try:
            self.result=str(round(eval(self.result),5))
            if self.result=='0':
                self.result=''
            if self.result=='':
                self.lineEdit_result.setText('0')
            else:
                self.lineEdit_result.setText(self.result)
        except:
            self.result=''
            self.lineEdit_result.setText('WTF???')
if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()