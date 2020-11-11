import sys
from PyQt5.QtWidgets import *

#초기화
app = QApplication(sys.argv)


#내용 채우기 
label = QLabel("Hello world")
label.show()


print("before event loop")
#여기서 무한 루프 
app.exec_()
print("after event loop")

