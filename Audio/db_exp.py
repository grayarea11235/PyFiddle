import sys
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, 
        QPushButton, QTextEdit, 
        QGridLayout, QVBoxLayout,
        QWidget, QMenuBar,
        QMenu)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DB Exp")
        self.resize(800, 600)

        # Set the central widget of the Window.
        #self.setCentralWidget(self.button)

        self.initUI()


    def initUI(self):
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.onButtonClicked)

        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&File", self)
        self.menu_bar.addMenu(file_menu)

        self.command_window = QTextEdit()
        self.result_window = QTextEdit()
        self.result_window.setReadOnly(True)

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.command_window)
        self.h_layout.addWidget(self.result_window)

        w = QWidget()
        w.setLayout(self.h_layout)

        self.setCentralWidget(w)


    def onButtonClicked(self):
        print('CLICKED')


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
