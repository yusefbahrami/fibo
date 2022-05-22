from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar, QLabel


fib_list = []
def fibo(n: int):
    global fib_list
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # yield fibo(n-1)+fibo(n-2)
        temp = fibo(n-2) + fibo(n-1)
        fib_list.append(temp)
        return temp
        # yield fibo(n-2)+fibo(n-1)


# f = fibo(8)
# print(fib_list)
# print(f)


class MyThread(QThread):
    newValue = pyqtSignal(int)

    def run(self) -> None:
        # return super().run()
        for i in range(10000+1):
            self.newValue.emit(i)
            with open('fibs.txt', 'a') as file:
                file.write(f"{str(i)}\n")


# test
# app = QApplication([])
# win = QMainWindow()
# win.setMinimumSize(400, 300)

# def setval(e):
#     p.setValue(e)
#     lbl.setText(str(e))

# p = QProgressBar(parent=win)
# p.setMaximum(100000)
# p.setMinimumWidth(300)
# lbl = QLabel(win)
# lbl.move(10, 50)
# m = MyThread()
# m.start()
# # m.newValue.connect(lambda e:p.setValue(e))
# m.newValue.connect(setval)
# win.show()
# app.exec()
