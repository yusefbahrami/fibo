from PyQt5.QtWidgets import QApplication
from view import Window
from model import MyThread

app = QApplication([])
win = Window()


def setVal(e):
    win.prgs.setValue(e)
    win.lbl.setText(str(e))


def connect_to_setVal():
    m.start()
    m.newValue.connect(setVal)


m = MyThread()

win.btn.clicked.connect(connect_to_setVal)
win.show()
app.exec()
