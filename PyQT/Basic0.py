
#https://m.blog.naver.com/sisosw/221419144691

import sys
from PyQt5.QtWidgets import *

#================================
#초기화
'''
app = QApplication(sys.argv)


#내용 채우기 
label = QLabel("Hello world")
label.show()


print("before event loop")
#여기서 무한 루프 
app.exec_()
print("after event loop")
'''

#=================================
#하드 코딩 버튼 생성
'''
def clicked_slot():
    print("clicked")

app = QApplication(sys.argv)

btn = QPushButton("Push")
btn.clicked.connect(clicked_slot)
btn.show()

app.exec_()
'''

#===========================================
#여러개 위젯 생성

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()



#===============================
#윈도우 클래스 상속 받아서 생성
'''
class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("윈도우 제목")
        self.setGeometry(300, 300, 300, 400)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    window.show()
    app.exec_()
'''

#=========================================
#코딩으로 버튼 기능 만들기
'''
class ButtonlabelWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("ButtonlabelWIndow")
        self.setGeometry(100, 100, 300, 100)

        self.label = QLabel("Message:",self)
        self.label.move(20, 20)
        self.label.resize(200, 20)

        btnSave = QPushButton("저장", self)
        btnSave.move(20, 50)
        btnSave.clicked.connect(self.btnSave_clicked)

        btnCancel = QPushButton("취소", self)
        btnCancel.move(120, 50)
        btnCancel.clicked.connect(self.btnCancel_clicked)

    def btnSave_clicked(self):
        self.label.setText("저장되었습니다.")

    def btnCancel_clicked(self):
        self.label.setText("취소 되었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonlabelWindow()
    window.show()
    app.exec_()

'''