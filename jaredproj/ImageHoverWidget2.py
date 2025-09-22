from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap

class ImageHoverWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create the QLabel for the image
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)  # Enable scaling
        self.image_label.hide()  # Hide initially

        # Create a layout for proper resizing
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.setLayout(layout)

    def set_image(self, image_path):
        """Set the image to display."""
        self.image_label.setPixmap(QPixmap(image_path))

    def show_image(self):
        """Show the image."""
        self.image_label.show()

    def hide_image(self):
        """Hide the image."""
        self.image_label.hide()