from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout

class SecondTab(QWidget):
    def __init__(self):
        super().__init__()

        # Structure
        self.second_body = QHBoxLayout()

        # First Body Components
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        
        self.print_btn = QPushButton("Print Slider Value")

        # Functionality
        self.print_btn.clicked.connect(self.print_values)

        # Assembly
        self.second_body.addWidget(self.slider)
        self.second_body.addWidget(self.print_btn)

        self.setLayout(self.second_body)

    def print_values(self):
        print(f"Slider Value: {self.slider.value()}")