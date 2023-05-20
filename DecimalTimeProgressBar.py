from PyQt6.QtWidgets import QProgressBar


class DecimalTimeProgressBar(QProgressBar):
    def __init__(self,                parent=None):
        super(DecimalTimeProgressBar, self).__init__(parent)
