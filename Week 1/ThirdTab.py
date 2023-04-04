from PySide6.QtWidgets import QWidget, QPushButton, QFormLayout, QLineEdit, QTextEdit, QComboBox

class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        # Structure
        self.third_body = QFormLayout()

        # First Body Components
        self.name = QLineEdit()
        self.description = QTextEdit()
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female"])

        self.print_btn = QPushButton("Print information")

        # Functionality
        self.print_btn.clicked.connect(self.print_values)

        # Assembly
        self.third_body.addRow("Name: ", self.name)
        self.third_body.addRow("Description: ", self.description)
        self.third_body.addRow("Gender: ", self.gender)
        self.third_body.addWidget(self.print_btn)

        self.setLayout(self.third_body)

    def print_values(self):
        print(f"Name: {self.name.text()}")
        print(f"Description: {self.description.toPlainText()}")
        print(f"Gender: {self.gender.currentText()}")