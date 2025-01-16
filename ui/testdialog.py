from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import Qt

class TestDialog(QDialog):
    def __init__(self, parent ):
        super().__init__()
        self.setWindowTitle("My dialog")
        self.setWindowFlag(Qt.WindowFlags.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowFlags.WindowCloseButtonHint  , False)
        #self.setWindowFlags(Qt.WindowFlags.CustomizeWindowHint | Qt.WindowFlags.WindowTitleHint | ~Qt.WindowFlags.WindowMinMaxButtonsHint)
        #self.setWindowFlag(Qt.WindowFlags.CustomizeWindowHint , True)
        #self.setWindowFlag(Qt.WindowFlags.WindowMinimizeButtonHint, False)
        