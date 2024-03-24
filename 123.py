from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Shadowing")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("Hello, World!", self)
        self.label.setGeometry(50, 50, 200, 50)

        self.button = QPushButton("Shadow Text", self)
        self.button.setGeometry(50, 150, 100, 50)
        self.button.clicked.connect(self.shadow_text)

    def shadow_text(self):
        current_text = self.label.text()
        self.label.setText(f"<html><head/><body><p><span style='color:#aaaaaa;'>{current_text}</span></p></body></html>")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
