from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(400, 300)
        self.label = QtWidgets.QLabel(main)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label.setStyleSheet("font: 87 16pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(main)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 50, 31))
        self.pushButton_1.setStyleSheet("font: 87 14pt \"Arial Black\";")
        self.pushButton_1.setObjectName("pushButton")
        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.label.setText(_translate("main", "main"))
        self.pushButton_1.setText(_translate("main", "нажать"))

class Ui_window_1(object):
    def setupUi(self, window_1):
        window_1.setObjectName("window_1")
        window_1.resize(300, 200)
        self.label = QtWidgets.QLabel(window_1)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label.setStyleSheet("font: 87 16pt \"Arial Black\";")
        self.label.setObjectName("label")

        self.retranslateUi(window_1)
        QtCore.QMetaObject.connectSlotsByName(window_1)

    def retranslateUi(self, window_1):
        _translate = QtCore.QCoreApplication.translate
        window_1.setWindowTitle(_translate("window_1", "Form"))
        self.label.setText(_translate("window_1", "window_1"))

class Win(QtWidgets.QWidget, Ui_window_1):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setupUi(self)                                         # +++
        self.layout = QtWidgets.QVBoxLayout(self)                  # +++
        self.layout.addWidget(self.label)                          # +++

class Main(QtWidgets.QWidget, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("Main")
        self.pushButton_1.clicked.connect(self.Win_f)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label) 
        layout.addWidget(self.pushButton_1)

        self.wmain = Win()
        self.wmain.setWindowTitle("Win")
        self.wmain.btn = QtWidgets.QPushButton("Открыть Main", self.wmain, clicked=self.showMain)
        self.wmain.layout.addWidget(self.wmain.btn)

# ???       b = #определение открыто ли окно или нет


    def event(self, event):
        if event.type() == QtCore.QEvent.WindowActivate:
            print(f"Oкно стало активным; (WindowActivate).")
        elif event.type() == QtCore.QEvent.WindowDeactivate:
            print(f"Oкно стало НЕактивным; (WindowDeactivate).") 
        elif event.type() == QtCore.QEvent.Close:
            print(f"Oкно закрытo (QCloseEvent).") 

        return QtWidgets.QWidget.event(self, event)

    def showMain(self):
        self.show()

    def Win_f(self):
        self.wmain.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    w = Main()
    w.show()
    sys.exit(app.exec_())