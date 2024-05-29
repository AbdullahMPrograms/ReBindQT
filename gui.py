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
        # Add more widgets and setup specific to the Home Page

class MacroPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Macro Page")
        layout.addWidget(label)
        # Add more widgets and setup specific to the Macro Page

class PluginPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Plugin Page")
        layout.addWidget(label)
        # Add more widgets and setup specific to the Plugin Page

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Profile Page")
        layout.addWidget(label)
        # Add more widgets and setup specific to the Profile Page

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        label = QLabel("Settings Page")
        layout.addWidget(label)
        # Add more widgets and setup specific to the Settings Page

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ReBind")
        self.setFixedSize(1250, 570)
        self.setWindowIcon(QIcon("resources/icons/icon_logo.png"))
        self.setStyleSheet("background-color: #141414; border-radius: 10px;")

        # Main layout
        mainLayout = QHBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setSpacing(0)

        # Create sidebar
        self.sidebarFrame = self.create_sidebar()
        mainLayout.addWidget(self.sidebarFrame)

        # Create right side layout
        rightLayout = QVBoxLayout()
        rightLayout.setContentsMargins(0, 0, 0, 0)
        rightLayout.setSpacing(0)

        # Create content frame
        self.contentFrame, self.stackedWidget = self.create_content_frame()
        rightLayout.addWidget(self.contentFrame)

        # Create version frame
        self.versionFrame = self.create_version_frame()
        rightLayout.addWidget(self.versionFrame)

        mainLayout.addLayout(rightLayout)

        # Animation setup
        self.sidebarAnimation = QPropertyAnimation(self.sidebarFrame, b"minimumWidth")
        self.sidebarAnimation.setDuration(250)
        self.sidebarAnimation.setEasingCurve(QEasingCurve.OutCubic)

        self.menuButton.clicked.connect(self.toggle_sidebar)

    def create_sidebar(self):
        sidebarFrame = QFrame()
        sidebarFrame.setMaximumWidth(200)
        sidebarFrame.setMinimumWidth(70)
        sidebarFrame.setStyleSheet("""
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
            }
        """)

        sidebarLayout = QVBoxLayout(sidebarFrame)
        sidebarLayout.setContentsMargins(0, 0, 0, 0)
        sidebarLayout.setSpacing(0)

        self.menuButton = QPushButton()
        self.menuButton.setIcon(QIcon("resources/icons/icon_menu.png"))
        self.menuButton.setIconSize(QSize(18, 18))
        sidebarLayout.addWidget(self.menuButton)

        buttons = [
            ("resources/icons/icon_home.png", lambda: self.stackedWidget.setCurrentIndex(0)),
            ("resources/icons/icon_macro.png", lambda: self.stackedWidget.setCurrentIndex(1)),
            ("resources/icons/icon_plugin.png", lambda: self.stackedWidget.setCurrentIndex(2)),
            ("resources/icons/icon_profile.png", lambda: self.stackedWidget.setCurrentIndex(3)),
            ("resources/icons/icon_debug.png", lambda: print("Debug Button Clicked")),
        ]

        for icon, func in buttons:
            button = QPushButton()
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(16, 16))
            button.clicked.connect(func)
            sidebarLayout.addWidget(button)

        sidebarLayout.addStretch(0)  # Add the stretch before the settings button

        settingsButton = QPushButton()
        settingsButton.setIcon(QIcon("resources/icons/icon_settings.png"))
        settingsButton.setIconSize(QSize(18, 18))
        settingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        sidebarLayout.addWidget(settingsButton)

        return sidebarFrame

    def create_content_frame(self):
        contentFrame = QFrame()
        contentFrame.setStyleSheet("background-color: #1a1a1a; border-radius: 10px;")

        stackedWidget = QStackedWidget(contentFrame)

        # Add pages to the stacked widget
        stackedWidget.addWidget(HomePage())
        stackedWidget.addWidget(MacroPage())
        stackedWidget.addWidget(PluginPage())
        stackedWidget.addWidget(ProfilePage())
        stackedWidget.addWidget(SettingsPage())

        contentLayout = QVBoxLayout(contentFrame)
        contentLayout.addWidget(stackedWidget)

        return contentFrame, stackedWidget

    def create_version_frame(self):
        versionFrame = QFrame()
        versionFrame.setStyleSheet("background-color: #141414; border-radius: 10px;")
        versionFrame.setFixedHeight(30)

        versionLabel = QLabel("v0.0.1")
        versionLabel.setStyleSheet("color: #a2a19b; font-size: 12px; font-family: 'Open Sans';")

        versionLayout = QHBoxLayout(versionFrame)
        versionLayout.addStretch(1)
        versionLayout.addWidget(versionLabel)
        versionLayout.setContentsMargins(0, 0, 15, 0)

        return versionFrame

    def toggle_sidebar(self):
        if self.sidebarFrame.minimumWidth() == 70:
            self.sidebarAnimation.setStartValue(70)
            self.sidebarAnimation.setEndValue(200)
            self.sidebarFrame.setMaximumWidth(200)  # Ensure max width is increased
        else:
            self.sidebarAnimation.setStartValue(200)
            self.sidebarAnimation.setEndValue(70)
            self.sidebarFrame.setMaximumWidth(70)  # Ensure max width is reduced
        self.sidebarAnimation.start()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
