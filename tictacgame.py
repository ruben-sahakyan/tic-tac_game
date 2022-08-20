from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 549)
        
        #window size fixed
        MainWindow.setFixedSize(419, 549)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 461, 531))
        self.label.setStyleSheet("image: url(:/newPrefix/tic-tacdes.png);")
        self.label.setText("")
        self.label.setObjectName("label")


        self.btn_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_1))
        self.btn_1.setGeometry(QtCore.QRect(10, 140, 75, 71))
        self.btn_1.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 40pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")


        self.btn_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_5))
        self.btn_5.setGeometry(QtCore.QRect(120, 220, 121, 121))
        self.btn_5.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 70pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")


        self.btn_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_4))
        self.btn_4.setGeometry(QtCore.QRect(10, 270, 81, 81))
        self.btn_4.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 55pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")


        self.btn_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_7))
        self.btn_7.setGeometry(QtCore.QRect(10, 400, 91, 101))
        self.btn_7.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 40pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")


        self.btn_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_2))
        self.btn_2.setGeometry(QtCore.QRect(160, 130, 61, 51))
        self.btn_2.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 35pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")


        self.btn_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_6))
        self.btn_6.setGeometry(QtCore.QRect(280, 230, 141, 151))
        self.btn_6.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 80pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")


        self.btn_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_8))
        self.btn_8.setGeometry(QtCore.QRect(120, 390, 91, 101))
        self.btn_8.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 50pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")


        self.btn_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_9))
        self.btn_9.setGeometry(QtCore.QRect(290, 420, 91, 101))
        self.btn_9.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 50pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")


        self.btn_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.tuched(self.btn_3))
        self.btn_3.setGeometry(QtCore.QRect(310, 110, 91, 101))
        self.btn_3.setStyleSheet("color: rgb(54, 54, 54);\n"
        "background-color: None;\n"
        "font: 50pt \"Blackadder ITC\";\n"
        "border: None;\n"
        "")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")


        self.btn_newgame = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.new_game())
        self.btn_newgame.setGeometry(QtCore.QRect(10, -10, 131, 51))
        self.btn_newgame.setStyleSheet("color: rgb(154, 154, 154);\n"
        "background-color: None;\n"
        "font: 30pt \"Blackadder ITC\";\n"
        "border: None;")
        self.btn_newgame.setObjectName("btn_newgame")


        self.winnerlabel = QtWidgets.QLabel(self.centralwidget)
        self.winnerlabel.setGeometry(QtCore.QRect(290, 10, 121, 31))
        self.winnerlabel.setStyleSheet("color: rgb(89, 89, 89);\n"
        "background-color: None;\n"
        "font: 20pt \"Blackadder ITC\";\n"
        "border: None;")
        self.winnerlabel.setObjectName("winnerlabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_newgame.setText(_translate("MainWindow", "new game"))
        self.winnerlabel.setText(_translate("MainWindow", ""))
        import tictacdes
        self.count = 0


    def tuched(self, cl):
        if self.count %2 == 0:
            tictak = 'X'
        else:
            tictak = 'O'
        
        cl.setText(tictak)
        self.count +=1
        self.wins()

    def wins(self):
        #hotizontal line
        if self.btn_1.text() != "" and self.btn_1.text() == self.btn_2.text() and self.btn_1.text() == self.btn_3.text():
            self.winnerlabel.setText(f"Winner! {self.btn_1.text()}")
        elif self.btn_4.text() != "" and self.btn_4.text() == self.btn_5.text() and self.btn_4.text() == self.btn_6.text():
            self.winnerlabel.setText(f"Winner! {self.btn_4.text()}")
        elif self.btn_7.text() != "" and self.btn_7.text() == self.btn_8.text() and self.btn_7.text() == self.btn_9.text():
            self.winnerlabel.setText(f"Winner! {self.btn_7.text()}")
        #vertical line
        elif self.btn_1.text() != "" and self.btn_1.text() == self.btn_4.text() and self.btn_1.text() == self.btn_7.text():
            self.winnerlabel.setText(f"Winner! {self.btn_1.text()}")
        elif self.btn_2.text() != "" and self.btn_2.text() == self.btn_5.text() and self.btn_2.text() == self.btn_8.text():
            self.winnerlabel.setText(f"Winner! {self.btn_2.text()}")
        elif self.btn_3.text() != "" and self.btn_3.text() == self.btn_6.text() and self.btn_3.text() == self.btn_9.text():
            self.winnerlabel.setText(f"Winner! {self.btn_3.text()}")
        #diagonal line
        elif self.btn_1.text() != "" and self.btn_1.text() == self.btn_5.text() and self.btn_1.text() == self.btn_9.text():
            self.winnerlabel.setText(f"Winner! {self.btn_1.text()}")
        elif self.btn_3.text() != "" and self.btn_3.text() == self.btn_5.text() and self.btn_3.text() == self.btn_7.text():
            self.winnerlabel.setText(f"Winner! {self.btn_3.text()}")


    def new_game(self):
        self.winnerlabel.setText('')
        self.btn_1.setText('')
        self.btn_2.setText('')
        self.btn_3.setText('')
        self.btn_4.setText('')
        self.btn_5.setText('')
        self.btn_6.setText('')
        self.btn_7.setText('')
        self.btn_8.setText('')
        self.btn_9.setText('')



    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
