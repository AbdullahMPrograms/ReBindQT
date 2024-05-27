# ALL GUI AND UI FUNCTIONS ARE DEFINED HERE
import sys
from PySide6.QtWidgets import *

def main():
    # Create the application object
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("Hello World")

    # Create a label
    label = QLabel("Hello, World!", parent=window)

    # Set layout
    layout = QVBoxLayout()
    layout.addWidget(label)
    window.setLayout(layout)

    # Show the window
    window.show()

    # Execute the application's main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()