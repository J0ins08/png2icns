from pathlib import Path

from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QStatusBar,
    QMenu,
    QAction,
    QVBoxLayout,
    QMenuBar,
    QFrame,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize


class MainWindowUI:
    def setup_ui(self, MainWindow: QMainWindow):

        # drop_icon label
        drop_icon_label = QLabel()
        drop_icon_label.setMaximumSize(QSize(50, 50))
        drop_icon = Path.cwd().joinpath('img/drop_icon.png')
        drop_icon_label.setPixmap(QPixmap(str(drop_icon)))
        drop_icon_label.setScaledContents(True)

        # label
        self.label = QLabel()
        font = QFont()
        font.setPointSize(45)
        self.label.setFont(font)
        self.label.setText('Drop image here')
        self.label.setStyleSheet("color:rgb(145, 145, 145)")

        # button
        self.button = QPushButton('Convert')
        self.button.setMinimumSize(100, 32)

        # statusbar
        self.statusbar = QStatusBar()

        # menubar
        menubar = QMenuBar()
        menu = QMenu(menubar)
        self.action = QAction('About', MainWindow)
        menu.addAction(self.action)
        menubar.addAction(menu.menuAction())

        # layout
        frame = QFrame()
        frame.setContentsMargins(20, 20, 20, 10)
        v_layout = QVBoxLayout(frame)
        for widget in (drop_icon_label, self.label, self.button):
            v_layout.addWidget(widget, 0, Qt.AlignHCenter)

        # setup mainwindow
        MainWindow.setWindowTitle('png2icns')
        MainWindow.resize(550, 250)
        MainWindow.setCentralWidget(frame)
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setMenuBar(menubar)
