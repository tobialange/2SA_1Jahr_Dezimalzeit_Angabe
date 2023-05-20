from PyQt6.QtCore import QTimer, pyqtSignal, pyqtSlot, QDateTime


class TimerDecimal(QTimer):
    time = pyqtSignal(str)

    update = pyqtSlot()



    def update(self):
        currentTime = QDateTime.currentDateTime().time()






        decimalTime = "{:01d}:{:02d}:{:02d}".format(decimalHour, decimalMinute, decimalSecond)

        self.time.emit(decimalTime)
