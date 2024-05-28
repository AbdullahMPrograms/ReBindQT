# ALL GUI AND UI FUNCTIONS ARE DEFINED HERE
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

def main():
    app = QApplication()

    # Create the main window
    window = QWidget()
    window.setWindowTitle("ReBind")
    window.setFixedSize(1250, 570)
    window.setWindowIcon(QIcon("resources/icons/icon_logo.png"))
    window.setStyleSheet("background-color: #141414; border-radius: 10px;")

    # Content frame
    contentFrame = QFrame(window)
    contentFrame.setGeometry(70, 0, 1180, 540)
    contentFrame.setStyleSheet("background-color: #1a1a1a; border-radius: 10px;")

    # Stacked Widget (Pages)
    stackedWidget = QStackedWidget(contentFrame)
    
    # Home Page
    homePage = QWidget()
    homePageLayout = QVBoxLayout(homePage)
    homePageLabel = QLabel("Home Page")
    homePageLayout.addWidget(homePageLabel)
    stackedWidget.addWidget(homePage)

    # Macro Page
    macroPage = QWidget()
    macroPageLayout = QVBoxLayout(macroPage)
    macroPageLabel = QLabel("Macro Page")
    macroPageLayout.addWidget(macroPageLabel)
    stackedWidget.addWidget(macroPage)
    
    # Plugin Page
    pluginPage = QWidget()
    pluginPageLayout = QVBoxLayout(pluginPage)
    pluginPageLabel = QLabel("Plugin Page")
    pluginPageLayout.addWidget(pluginPageLabel)
    stackedWidget.addWidget(pluginPage)
    
    # Profile Page
    profilePage = QWidget()
    profilePageLayout = QVBoxLayout(profilePage)
    profilePageLabel = QLabel("Profile Page")
    profilePageLayout.addWidget(profilePageLabel)
    stackedWidget.addWidget(profilePage)
    
    # Settings Page
    settingsPage = QWidget()
    settingsPageLayout = QVBoxLayout(settingsPage)
    settingsPageLabel = QLabel("Settings Page")
    settingsPageLayout.addWidget(settingsPageLabel)
    stackedWidget.addWidget(settingsPage)
    
    # Sidebar frame
    sidebarFrame = QFrame(window)
    sidebarFrame.setGeometry(0, 0, 70, 570)
    sidebarFrame.setStyleSheet("background-color: #141414; border-radius: 10px;")

    # Sidebar Buttons
    sidebarLayout = QVBoxLayout(sidebarFrame)
    sidebarLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins
    sidebarLayout.setSpacing(0)  # Remove spacing
    
    # in code for now
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

    # Menu button
    menuButton = QPushButton()
    menuButton.setIcon(QIcon("resources/icons/icon_menu.png"))
    menuButton.setIconSize(QSize(18, 18))
    sidebarLayout.addWidget(menuButton)

    homeButton = QPushButton()
    homeButton.setIcon(QIcon("resources/icons/icon_home.png"))
    homeButton.setIconSize(QSize(16, 16))
    homeButton.clicked.connect(lambda: stackedWidget.setCurrentIndex(0))
    sidebarLayout.addWidget(homeButton)
    
    macroButton = QPushButton()
    macroButton.setIcon(QIcon("resources/icons/icon_macro.png"))
    macroButton.setIconSize(QSize(16, 16))
    macroButton.clicked.connect(lambda: stackedWidget.setCurrentIndex(1))
    sidebarLayout.addWidget(macroButton)
    
    pluginButton = QPushButton()
    pluginButton.setIcon(QIcon("resources/icons/icon_plugin.png"))
    pluginButton.setIconSize(QSize(16, 16))
    pluginButton.clicked.connect(lambda: stackedWidget.setCurrentIndex(2))
    sidebarLayout.addWidget(pluginButton)
    
    profileButton = QPushButton()
    profileButton.setIcon(QIcon("resources/icons/icon_profile.png"))
    profileButton.setIconSize(QSize(16, 16))
    profileButton.clicked.connect(lambda: stackedWidget.setCurrentIndex(3))
    sidebarLayout.addWidget(profileButton)
    
    debugButton = QPushButton()
    debugButton.setIcon(QIcon("resources/icons/icon_debug.png"))
    debugButton.setIconSize(QSize(16, 16))
    debugButton.clicked.connect(lambda: print("Debug Button Clicked")) # Dummy for now
    sidebarLayout.addWidget(debugButton)
    
    sidebarLayout.addStretch(0)  # Basically a spacer
    
    settingsButton = QPushButton()
    settingsButton.setIcon(QIcon("resources/icons/icon_settings.png"))
    settingsButton.setIconSize(QSize(18, 18))
    settingsButton.clicked.connect(lambda: stackedWidget.setCurrentIndex(4))
    sidebarLayout.addWidget(settingsButton)
    
    # Version frame
    versionFrame = QFrame(window)
    versionFrame.setGeometry(70, 540, 1180, 30)
    versionFrame.setStyleSheet("background-color: #141414; border-radius: 10px;")
    
    # Version label
    versionLabel = QLabel("v0.0.1")
    versionLabel.setStyleSheet("color: #a2a19b; font-size: 12px; font-family: 'Open Sans';")
    
    # Create a horizontal layout for the version frame
    versionLayout = QHBoxLayout(versionFrame)
    versionLayout.addStretch(1)
    versionLayout.addWidget(versionLabel)
    versionLayout.setContentsMargins(0, 0, 15, 0)  # Set right margin to 15px

    # Animation setup
    sidebarAnimation = QPropertyAnimation(sidebarFrame, b"geometry")
    sidebarAnimation.setDuration(300)
    sidebarAnimation.setEasingCurve(QEasingCurve.OutCubic)

    def toggleSidebar():
        if sidebarFrame.width() == 70:
            sidebarAnimation.setStartValue(QRect(0, 0, 70, 570))
            sidebarAnimation.setEndValue(QRect(0, 0, 200, 570))
        else:
            sidebarAnimation.setStartValue(QRect(0, 0, 200, 570))
            sidebarAnimation.setEndValue(QRect(0, 0, 70, 570))
        sidebarAnimation.start()

    menuButton.clicked.connect(toggleSidebar)

    window.show()

    # Execute the application's main loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
