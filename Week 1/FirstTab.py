from PySide6.QtWidgets import QCheckBox, QPushButton, QVBoxLayout, QWidget

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        # Structure
        self.first_body = QVBoxLayout()

        # First Body Components
        self.redCheckBox = QCheckBox("Red")
        self.greenCheckBox = QCheckBox("Green")
        self.blueCheckBox = QCheckBox("Blue")

        self.print_btn = QPushButton("Print Selected Colors")

        # Functionality
        self.print_btn.clicked.connect(self.print_values)

        # Assembly
        self.first_body.addWidget(self.redCheckBox)
        self.first_body.addWidget(self.greenCheckBox)
        self.first_body.addWidget(self.blueCheckBox)
        self.first_body.addWidget(self.print_btn)

        self.setLayout(self.first_body)

    def print_values(self):
        print(f"[{self.redCheckBox.isChecked()}, {self.greenCheckBox.isChecked()}, {self.blueCheckBox.isChecked()}]")