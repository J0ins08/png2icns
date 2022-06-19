from pathlib import Path

from PyQt5.QtWidgets import QDialog, QFrame, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QSize, Qt


class About_dialogUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # frame
        frame = QFrame()

        # layout in frame
        frame_v_layout = QVBoxLayout(frame)

        # app_icon label
        app_icon_label = QLabel()
        app_icon_label.setMaximumSize(QSize(64, 64))
        app_icon = Path.cwd().joinpath('img/app_icon.png')
        app_icon_label.setPixmap(QPixmap(str(app_icon)))
        app_icon_label.setScaledContents(True)

        # title label
        title_label = QLabel('png2icns')
        font = QFont()
        font.setPointSize(18)
        title_label.setFont(font)

        # version_label
        self.version_label = QLabel('Version: 1.0.0')

        # app_icon source label
        app_icon_source_label = QLabel(
            'App icon by: '
            '<a style="text-decoration: none" href="https://www.deviantart.com/octaviotti">'
            '@octaviotti </a>'
        )

        # drop_icon source label
        drop_icon_source_label = QLabel(
            'Drop icon by: '
            '<a style="text-decoration: none" href="http://www.customicondesign.com">'
            '@custom icon design </a>'
        )

        # theme source label
        theme_source_label = QLabel(
            'Theme by: '
            '<a style="text-decoration: none" href="https://github.com/5yutan5/PyQtDarkTheme">'
            '@5yutan5 </a>'
        )

        # setup layout
        for label in (
            app_icon_label,
            title_label,
            self.version_label,
            app_icon_source_label,
            drop_icon_source_label,
            theme_source_label,
        ):
            frame_v_layout.addWidget(label, 0, Qt.AlignHCenter)
            label.setOpenExternalLinks(True)

        # main layout
        main_v_layout = QVBoxLayout(self)
        main_v_layout.addWidget(frame)
