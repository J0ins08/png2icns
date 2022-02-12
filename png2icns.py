import os
import sys
import shutil
from pathlib import Path
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

def statusBarShowMessage(message):
    ui.statusbar.showMessage(message)

def convertToIcns(imageName):
    imagePath = Path(imageName).parent
    tmpFolder = Path(imagePath).joinpath('tmp.iconset')
    Path(tmpFolder).mkdir(parents=True, exist_ok=True)
    sizeList = [16, 32, 32, 64, 128, 256, 256, 512, 512, 1024]
    iconSizeList = ['16x16', '16x16@2x', '32x32', '32x32@2x', '128x128', '128x128@2x', '256x256', '256x256@2x', '512x512', '512x512@2x']
    for i in range(10):
        cmdSips = f'sips -z {sizeList[i]} {sizeList[i]} {imageName} --out {tmpFolder}/icon_{iconSizeList[i]}.png'
        os.system(cmdSips)
    cmdIconutil = f"iconutil -c icns {tmpFolder} -o {Path(imagePath).joinpath('Icon.icns')}"
    os.system(cmdIconutil)
    shutil.rmtree(tmpFolder)
    target = Path(imagePath).joinpath('Icon.icns')
    prompt = f'Compiled to "{target}" successfully.'
    statusBarShowMessage(prompt)

class QWidgetEnableDrop(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        filePath = str(event.mimeData().text())
        filePath = filePath.replace('file://', '')
        statusBarShowMessage(filePath)
        ui.pushButton.clicked.connect(lambda:convertToIcns(filePath))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(400, 200))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidgetEnableDrop(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 171))
        self.widget.setAcceptDrops(True)
        self.widget.setObjectName("widget")
        self.labelImage = QtWidgets.QLabel(self.widget)
        self.labelImage.setGeometry(QtCore.QRect(180, 20, 40, 40))
        self.labelImage.setMinimumSize(QtCore.QSize(40, 40))
        self.labelImage.setMaximumSize(QtCore.QSize(40, 40))
        image = str(Path(sys.argv[0]).parent.joinpath('image.png'))
        self.labelImage.setPixmap(QPixmap(image))
        self.labelImage.setScaledContents(True)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 260, 50))
        self.label_2.setMinimumSize(QtCore.QSize(260, 50))
        self.label_2.setMaximumSize(QtCore.QSize(260, 50))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 120, 100, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "png2icns"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#9b9b9b;\">Drop image here</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Covert"))

if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())