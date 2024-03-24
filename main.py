from PyQt5.QtCore import Qt, QSize
import modul_system_cal
import modul_log
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QRadioButton, QLabel, \
    QLineEdit, QStyle




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

        self.label_input = QLabel("Chose a method:", self)
        self.label_input.move(50, 25)

        # Create radio buttons to select the encoding method
        self.radio_button1 = QRadioButton("Dec", self)
        self.radio_button1.move(50, 55)
        self.radio_button1.setChecked(True)

        self.radio_button2 = QRadioButton("Oct", self)
        self.radio_button2.move(125, 55)

        self.radio_button3 = QRadioButton("Hex", self)
        self.radio_button3.move(200, 55)

        self.radio_button4 = QRadioButton("Bin", self)
        self.radio_button4.move(275, 55)

        self.radio_button5 = QRadioButton("You\nOption", self)
        self.radio_button5.move(350, 55)

        # Labels above input fields
        self.label_input = QLabel("Input number:", self)
        self.label_input.move(50, 80)

        self.input_box = QLineEdit(self)
        self.input_box.move(50, 120)

        self.input_box.resize(self.width() - 100, 30)  # Stretch by width and height
        self.input_box.setPlaceholderText("Enter number...")

        # TODO: chack if it relevant
        # self.label_input_loop = QLabel("Input key:", self)
        # self.label_input_loop.move(50, 155)

        self.input_box_loop = QLineEdit(self)
        self.input_box_loop.move(425, 50)
        self.input_box_loop.resize(100, 30)
        self.input_box_loop.setPlaceholderText("Your Base")

        self.label_input = QLabel("Your answer: ", self)
        self.label_input.move(55, 160)

        # Button to get an answer
        self.button = QPushButton(self)
        self.button.clicked.connect(self.on_click)
        self.button.setText("The answer")
        self.button.move(450, 235)

        # self.button = QPushButton("The answer", self.on_click())
        # self.button.clicked.connect(lambda: modul_log.click(self))


        self.text_to_show = "qwert"

    def on_click(self):
        result= modul_log.click(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
