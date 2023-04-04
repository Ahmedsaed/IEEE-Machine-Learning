from PySide6.QtWidgets import QApplication, QTabWidget
from PySide6.QtGui import QIcon 
from FirstTab import FirstTab
from SecondTab import SecondTab
from ThirdTab import ThirdTab

class MainWindow(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        # Structure
        self.firstTab = FirstTab()
        self.secondTab = SecondTab()
        self.thirdTab = ThirdTab()

        # Assembly
        self.addTab(self.firstTab, "Tab 1")
        self.addTab(self.secondTab, "Tab 2")
        self.addTab(self.thirdTab, "Tab 3")

        self.setWindowTitle("Awesome App")
        self.setWindowIcon(QIcon("./ok.png"))


if '__main__' in __name__:
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()
