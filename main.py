import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            qp.setBrush(QColor(255, 255, 0))
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
