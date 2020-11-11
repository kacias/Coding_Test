#QTPY

#참조
#https://www.youtube.com/watch?v=Ss7dDDS-DhU&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&ab_channel=%EC%9E%AC%EC%A6%90%EB%B3%B4%ED%94%84
#https://wikidocs.net/35478
#https://appia.tistory.com/298


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QFileDialog, QTextEdit, QHBoxLayout, QVBoxLayout


class QtGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Notepad")
        menubar = self.menuBar()

        Filemenu = menubar.addMenu("File")
        Filemenu1 = menubar.addMenu("Edit")
        Filemenu2 = menubar.addMenu("Format")

        loadfile = QAction('laod File ...', self)
        savefile = QAction('save File ...', self)
        exit = QAction('Exit', self)

        loadfile.triggered.connect(self.add_open)
        savefile.triggered.connect(self.add_save)
        exit.triggered.connect(qApp.quit)
        Filemenu.addAction(loadfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(exit)

        self.text1 = QTextEdit(self)
        self.text1.setAcceptRichText(True)
        self.setCentralWidget(self.text1)
        self.show()

    def add_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        f = open(FileOpen[0], 'r')
        textcontenct = f.read()
        self.text1.setText(textcontenct)
        f.close()

    def add_save(self):
        FileSave = QFileDialog.getSaveFileName(self, 'Save file', './')
        textcontent = self.text1.toPlainText()
        f = open(FileSave[0], 'w')
        f.write(textcontent)
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
