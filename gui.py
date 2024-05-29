import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Home Page")
        layout.addWidget(label)

class MacroPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Macro Page")
        layout.addWidget(label)

class PluginPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Plugin Page")
        layout.addWidget(label)

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Profile Page")
        layout.addWidget(label)

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Settings Page")
        layout.addWidget(label)

class Sidebar(QFrame):
    def __init__(self, parent, stacked_widget):
        super().__init__(parent)
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                margin: 0px;
                padding: 0px;
                color: white;
                width: 70px;
                height: 50px;
                border-radius: 0px;
            }
            QPushButton:hover {
                background-color: #1a1a1a;
                border-radius: 3px;
            }
        """)
        sidebarLayout = QVBoxLayout(self)
        sidebarLayout.setContentsMargins(0, 0, 0, 0)
        sidebarLayout.setSpacing(0)

        self.menuButton = QPushButton()
        self.menuButton.setIcon(QIcon("resources/icons/icon_menu.png"))
        self.menuButton.setIconSize(QSize(18, 18))
        sidebarLayout.addWidget(self.menuButton)

        buttons = [
            ("resources/icons/icon_home.png", lambda: self.stacked_widget.setCurrentIndex(0)),
            ("resources/icons/icon_macro.png", lambda: self.stacked_widget.setCurrentIndex(1)),
            ("resources/icons/icon_plugin.png", lambda: self.stacked_widget.setCurrentIndex(2)),
            ("resources/icons/icon_profile.png", lambda: self.stacked_widget.setCurrentIndex(3)),
            ("resources/icons/icon_debug.png", lambda: print("Debug Button Clicked")),
        ]

        for icon, func in buttons:
            button = QPushButton()
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(16, 16))
            button.clicked.connect(func)
            sidebarLayout.addWidget(button)

        sidebarLayout.addStretch(0)

        settingsButton = QPushButton()
        settingsButton.setIcon(QIcon("resources/icons/icon_settings.png"))
        settingsButton.setIconSize(QSize(18, 18))
        settingsButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        sidebarLayout.addWidget(settingsButton)

class ContentFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #1a1a1a; border-radius: 10px;")
        self.stackedWidget = QStackedWidget(self)

        self.stackedWidget.addWidget(HomePage())
        self.stackedWidget.addWidget(MacroPage())
        self.stackedWidget.addWidget(PluginPage())
        self.stackedWidget.addWidget(ProfilePage())
        self.stackedWidget.addWidget(SettingsPage())

        contentLayout = QVBoxLayout(self)
        contentLayout.addWidget(self.stackedWidget)

class VersionFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: #141414; border-radius: 10px;")
        self.setFixedHeight(30)

        versionLabel = QLabel("v0.0.1")
        versionLabel.setStyleSheet("color: #a2a19b; font-size: 12px; font-family: 'Open Sans';")

        versionLayout = QHBoxLayout(self)
        versionLayout.addStretch(1)
        versionLayout.addWidget(versionLabel)
        versionLayout.setContentsMargins(0, 0, 15, 0)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ReBind")
        self.setFixedSize(1250, 570)
        self.setWindowIcon(QIcon("resources/icons/icon_logo.png"))
        self.setStyleSheet("background-color: #141414; border-radius: 10px;")

        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        # Sidebar
        self.contentFrame = ContentFrame(self)
        self.sidebarFrame = Sidebar(self, self.contentFrame.stackedWidget)
        mainLayout.addWidget(self.sidebarFrame)

        # Right side layout
        rightLayout = QVBoxLayout()
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightLayout.setSpacing(0)
        rightLayout.addWidget(self.contentFrame)

        self.versionFrame = VersionFrame(self)
        rightLayout.addWidget(self.versionFrame)

        mainLayout.addLayout(rightLayout)

        self.sidebarAnimation = QPropertyAnimation(self.sidebarFrame, b"minimumWidth")
        self.sidebarAnimation.setDuration(250)
        self.sidebarAnimation.setEasingCurve(QEasingCurve.OutCubic)

        self.sidebarFrame.menuButton.clicked.connect(self.toggle_sidebar)

    def toggle_sidebar(self):
        if self.sidebarFrame.width() == 70:
            self.sidebarAnimation.setStartValue(70)
            self.sidebarAnimation.setEndValue(200)
        else:
            self.sidebarAnimation.setStartValue(200)
            self.sidebarAnimation.setEndValue(70)
        self.sidebarAnimation.start()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
