import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRect


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Программа")
        self.setGeometry(100, 100, 400, 300)

        cw = QWidget()
        self.setCentralWidget(cw)
        lt = QVBoxLayout(cw)

        self.btn = QPushButton("Нарисовать")
        self.btn.clicked.connect(self.add_c)
        lt.addWidget(self.btn)

        self.ca = CA()
        lt.addWidget(self.ca)

    def add_c(self):
        self.ca.add_c()
        self.ca.update()


class CA(QWidget):
    def __init__(self):
        super().__init__()
        self.cs = []

    def add_c(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        s = random.randint(20, 100)
        self.cs.append((x, y, s))

    def paintEvent(self, e):
        tp = QPainter(self)

        for x, y, s in self.cs:
            tp.setBrush(QColor(255, 255, 0, 128))
            tp.drawEllipse(QRect(x - s // 2, y - s // 2, s, s))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MW()
    w.show()
    sys.exit(app.exec())