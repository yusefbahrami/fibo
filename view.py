from PyQt5.QtWidgets import QPushButton, QLabel, QProgressBar, QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Fibo')
        self.setMinimumSize(400, 300)

        self.btn = QPushButton(text='Click', parent=self)
        self.btn.move(10, 10)

        self.prgs = QProgressBar(self)
        self.prgs.move(10, 40)
        self.prgs.setMinimumSize(300, 20)
        self.prgs.setValue(50)
        self.prgs.setMaximum(10000)

        self.lbl = QLabel('0', parent=self)
        self.lbl.move(10, 60)
