import sys

from PyQt5.QtWidgets import QApplication

from BuildWatermarkWidget import BuildWatermarkWidget
from ReadQss import ReadQss


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BuildWatermarkWidget()
    win.setStyleSheet(ReadQss.notepadqss())
    win.show()
    sys.exit(app.exec_())