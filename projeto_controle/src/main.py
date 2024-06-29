from PySide6.QtCore import Qt
from window_controle import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec()
