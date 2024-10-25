import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 776)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 280, 381, 181))
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -30, 1231, 811))
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\Student\\Desktop\\BLISS\\DiDi.png"))
        self.label_3.setObjectName("label_3")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 580, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Frank Ruehl CLM")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet("background-color: rgb(255,255,255);")
        self.pushButton.setObjectName("pushButton")

        # Connect the button to the openFile method
        self.pushButton.clicked.connect(self.openFile)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">start</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START"))

    def openFile(self):
        # Define the specific file path you want to open
        file_path = "C:\\Users\\Student\\Desktop\\mains.py"  # Update with your file

        if file_path:
            try:
                # Run the specified Python file in a new command prompt
                subprocess.Popen(["python", file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
                # Minimize the main window after running the file
                QtWidgets.QApplication.instance().activeWindow().showMinimized()
            except Exception as e:
                print(f"Error running the file: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
