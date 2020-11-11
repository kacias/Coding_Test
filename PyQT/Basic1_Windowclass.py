import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#=======================================
#QT Designer 위치
#C:\Users\SJK\anaconda3\Library\bin

#UI파일 연결
form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


#========================================
#UI 창 띄우기
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()