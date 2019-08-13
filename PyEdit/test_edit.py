#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow
from PyQt5.QtWidgets import QAction, qApp, QFileDialog, QTextEdit, QVBoxLayout
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtGui import QIcon


class MyEdit(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def onFileOpen(self):
        print('In onFileOpen!')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            filenames = dlg.selectedFiles()

        print(filenames[0])

        with open(filenames[0], 'r') as in_file:
            text = in_file.readlines()

        print(text)
        
        self.editor.setPlainText(str(text))

    def initMenu(self):

        self.openAct = QAction(QIcon('open.png'), '&Open...', self)        
        self.openAct.setShortcut('Ctrl+O') 
        self.openAct.setStatusTip('Open file')
        self.openAct.triggered.connect(self.onFileOpen)

        self.exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        self.exitAct.setShortcut('Ctrl+Q') 
        
        self.exitAct.setStatusTip('Exit application')
        self.exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.openAct)
        fileMenu.addAction(self.exitAct)

        
    def initUI(self):               

        self.initMenu()

        self.editor = QTextEdit()
        self.editor.setPlainText('Some test text')

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        
        self.setGeometry(300, 300, 640, 480)        
        self.setWindowTitle('Test Edit')
        self.setLayout(layout)
        self.myCentralWidget = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.myCentralWidget.addTab(self.tab1,"Tab 1")
        self.myCentralWidget.addTab(self.tab2,"Tab 2")
        
        self.myCentralWidget.setLayout(layout)
        self.setCentralWidget(self.myCentralWidget)
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def run():
    pass
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myEdit = MyEdit()
    sys.exit(app.exec_())
#    run()
