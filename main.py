from PyQt5.QtCore import Qt, QSize
import modul_system_cal
import modul_log
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton,QLineEdit, QStyle, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initializing the main application window.
        """
        super().__init__()

        self.setWindowTitle("Base Change App")
        # Set the window size to the center of the screen
        self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, QSize(600, 280),
                                            QApplication.desktop().availableGeometry()))
        self.init_ui()  # вызываем метод инициализации интерфейса

        self.label_сhose = QLabel("Chose a method:", self)
        self.label_сhose.move(50, 120)

        # Create radio buttons to select the encoding method
        self.radio_but_dec = QRadioButton("Dec", self)
        self.radio_but_dec.move(50, 160)
        self.radio_but_dec.setChecked(True)

        self.radio_but_oct = QRadioButton("Oct", self)
        self.radio_but_oct.move(125, 160)

        self.radio_but_hex = QRadioButton("Hex", self)
        self.radio_but_hex.move(200, 160)

        self.radio_but_bin = QRadioButton("Bin", self)
        self.radio_but_bin.move(275, 160)

        self.radio_but_user_base = QRadioButton("You\nBase", self)
        self.radio_but_user_base.move(350, 160)

        # Labels above input fields
        self.label_input = QLabel("Input number: ", self)
        self.label_input.move(50, 25)

        self.input_box = QLineEdit(self)
        self.input_box.move(50, 55)

        self.input_box.resize(self.width() - 100, 30)
        self.input_box.setPlaceholderText("Enter number...")

        self.input_base = QLineEdit(self)
        self.input_base.move(425, 160)
        self.input_base.resize(100, 30)
        self.input_base.setPlaceholderText("Your Base")

        self.label_answer = QLabel("Your answer: ", self)
        self.label_answer.move(200, 215)

    def init_ui(self):
        """
        the function creates button updates the on_click
        :return: none
        """
        self.button = QPushButton(self)
        self.button.clicked.connect(self.on_click)
        self.button.setText("The answer")
        self.button.move(425, 215)

        self.label_out = QLabel(self)
        self.label_out.move(300, 215)

    def on_click(self):
        """
        :return: updates the label_out, puts there the answer
        """
        result = modul_log.click(self)
        self.label_out.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
