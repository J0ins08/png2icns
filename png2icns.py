import os
import sys
import shutil
from pathlib import Path

import qdarktheme
import darkdetect
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QObject, QEvent

from ui.mainwindow_ui import MainWindowUI
from ui.dialog_ui import About_dialogUI


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        super().__init__(parent)

        # setup ui
        self.setup_ui(self)

        # setup theme
        self.setup_theme()

        # window accept drop
        self.setAcceptDrops(True)
        self.installEventFilter(self)

        # setup action
        dialog = About_dialogUI()
        self.action.triggered.connect(lambda: dialog.show())

        # button signal
        self.button.clicked.connect(self.convert)

    def setup_theme(self):
        theme = darkdetect.theme().lower()
        theme_stylesheet = qdarktheme.load_stylesheet(theme)
        QApplication.instance().setStyleSheet(theme_stylesheet)

    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.DragEnter:
            event.accept()
        elif event.type() == QEvent.Drop:
            img_path = event.mimeData().urls()[0].toLocalFile()
            img_suffix = Path(img_path).suffix
            if img_suffix == '.png':
                self.statusbar.showMessage(img_path)
            else:
                self.statusbar.showMessage(
                    'Oops, It seems not a png file, Please check out and try again.',
                    5000,
                )
        return super().eventFilter(obj, event)

    def convert(self):
        '''button slot'''
        img_path = self.statusbar.currentMessage()
        if img_path:
            if Path(img_path).exists():
                tmp_iconset = Path(img_path).parent.joinpath('tmp.iconset')
                tmp_iconset.mkdir(parents=True, exist_ok=True)
                pixels = [16, 32, 32, 64, 128, 256, 256, 512, 512, 1024]
                icon_set = (
                    '16x16',
                    '16x16@2x',
                    '32x32',
                    '32x32@2x',
                    '128x128',
                    '128x128@2x',
                    '256x256',
                    '256x256@2x',
                    '512x512',
                    '512x512@2x',
                )

                for pixel, icon_size in zip(pixels, icon_set):
                    cmd = f'sips -z {pixel} {pixel} "{img_path}" -o {tmp_iconset}/icon_{icon_size}.png'
                    os.system(cmd)

                icns = Path(img_path).parent.joinpath('icon.icns')
                cmd = f'iconutil -c icns {tmp_iconset} -o {icns}'
                os.system(cmd)

                # del tmp.iconset dir
                shutil.rmtree(tmp_iconset)

                self.statusbar.showMessage(f'Complied to {icns} successfully.')
            else:
                pass
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
