import sys
import math
from PIL import ImageDraw, Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.compilation)
        self.colors = {"Синий": "blue", "Черный": "black",
                       "Желтый": "yellow", "Зеленый": "green",
                       "Красный": "red", "Оранжевый": "orange"}
        self.comboBox.addItems(self.colors.keys())
        self.setWindowTitle("Справочник по построению многоугольника")

    def compilation(self):
        number_of_sides = int(self.spinBox.value())
        size_of_side = int(self.spinBox_2.value())
        color = self.colors[self.comboBox.currentText()]
        correct_side = True
        picture = True
        im = Image.new("RGB", (400, 400), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        if number_of_sides == 0:
            if size_of_side == 0:
                self.textBrowser.setText("ERROR")
                self.textBrowser_2.setText("ERROR")
                self.textBrowser_3.setText("ERROR")
                correct_side = False
            else:
                self.textBrowser.setText(str(round(math.pi * size_of_side ** 2, 5)))
                self.textBrowser_2.setText(str(round(2 * math.pi * size_of_side, 5)))
                self.textBrowser_3.setText(str("0"))
                dr.ellipse((100, 100, 300, 300), fill=color, outline="black")
                picture = False
        elif number_of_sides != 0 and size_of_side == 0:
            self.textBrowser.setText("ERROR")
            self.textBrowser_2.setText("ERROR")
            self.textBrowser_3.setText("ERROR")
            correct_side = False
        elif number_of_sides == 1 or number_of_sides == 2:
            self.textBrowser.setText("ERROR")
            self.textBrowser_2.setText("ERROR")
            self.textBrowser_3.setText("ERROR")
            correct_side = False
        else:
            self.textBrowser.setText(str(round(number_of_sides / 4 * size_of_side ** 2 *
                                     (1 / math.tan(math.pi / number_of_sides)), 5)))
            self.textBrowser_2.setText(str(number_of_sides * size_of_side))
            self.textBrowser_3.setText(str(round((number_of_sides - 2) * 180 / number_of_sides, 5)))
        if correct_side and picture:
            x, y = 200, 200
            coords = [(x + 100 * math.cos(2 * math.pi * i / number_of_sides),
                      y + 100 * math.sin(2 * math.pi * i / number_of_sides)) for i in range(1, number_of_sides + 1)]
            dr.polygon(coords, fill=color, outline="black")
        im.save("new_paint.png")
        pixmap = QPixmap("new_paint.png")
        self.label_8.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
