from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from forex_python.converter import CurrencyRates


# Vars:
curr = {u'USD': 1.0, u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}
c = CurrencyRates()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 306)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(30, 30, 211, 22))
        self.dateEdit.setAcceptDrops(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.dateChanged.connect(self.showDate)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(30, 70, 211, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(1000000)
        self.spinBox.valueChanged.connect(self.Amount)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 110, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(curr.keys())
        self.comboBox.activated[str].connect(self.From)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 150, 211, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(curr.keys())
        self.comboBox_2.activated[str].connect(self.To)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 211, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Go)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 211, 21))
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionExit = QtWidgets.QAction("Exit", MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)

        self.actionAbout.triggered.connect(self.About)
        self.actionExit.triggered.connect(self.Exit)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "From"))
        self.comboBox.setItemText(1, _translate("MainWindow", "USD"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EUR"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "To"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "EUR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "USD"))

        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd/M/yyyy"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))
        self.label.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def About(self):
        self.label.setText('About')
        self.label.adjustSize()
        msg = QMessageBox()
        msg.setWindowTitle("About cc")
        msg.setText("Currency converter v1.0")
        msg.setInformativeText("It converts currencies.")
        msg.setIcon(QMessageBox.Information)
        msg.setDetailedText("Some of the dates / exchange rates may not work...")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.buttonClicked.connect(self.popup)
        msg.exec_()

    def popup(self, i):
        print(i.text())

    def Exit(self):
        self.label.setText("Exit cc")
        self.label.adjustSize()
        app.quit()

    def Amount(self):
        self.Amount = int(self.spinBox.text())
        self.label.setText(self.spinBox.text())
        self.label.adjustSize()

    def From(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        if text == "From":
            self.label.setText('Select valid currency')
            self.label.adjustSize()
        else:
            self.From = str(text)

    def To(self, text):
        self.label.setText(text)
        self.label.adjustSize()
        if text == "To":
            self.label.setText('Select valid currency')
            self.label.adjustSize()
        else:
            self.To = str(text)

    def showDate(self, date):
        self.label.setText(date.toString("dd-MM-yyyy dddd"))
        self.label.adjustSize()
        self.pyDate = date.toPyDate()

    def Go(self):
        rate = c.get_rate(str(self.To), str(self.From), self.pyDate)
        result = str(round((self.Amount / rate), 2)) + " " + str(self.To)
        self.label.setText(result)
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 

