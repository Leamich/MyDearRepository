import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QMetaObject, QCoreApplication
from PyQt5 import uic


class UiWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QPushButton(self.centralwidget)
        self.btn.setGeometry(250, 550, 191, 41)
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Красные треугольники"))
        self.btn.setText(_translate("MainWindow", "Зелёный квадрат"))


class Window(QMainWindow, UiWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.need_to_draw = False

        self.btn.clicked.connect(self.draw_fig)

    def draw_fig(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.need_to_draw:
            x, y = randint(0, 600), randint(0, 450),
            qp.setBrush(QColor(randint(0, 200),
                               randint(0, 200),
                               randint(0, 200)))
            qp.drawEllipse(x, y,
                           randint(10, 700 - x),
                           randint(10, 550 - y))

        self.need_to_draw = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Window()
    wind.show()
    sys.exit(app.exec())
