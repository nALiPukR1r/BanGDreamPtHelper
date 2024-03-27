# coding:utf-8
import sys

from PySide6.QtCore import Qt, QUrl, QSize, QEventLoop, QTimer
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QApplication
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme,
                            NavigationAvatarWidget,  SplitFluentWindow, FluentTranslator)
from qfluentwidgets import FluentIcon as FIF
import sys
from PySide6.QtCore import Qt, QRect, QUrl
from PySide6.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, qrouter, FluentWindow, NavigationAvatarWidget)
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import SplashScreen
from cal_Interface import CalInterface
from auto_Interface import AutoInterface
from setting_Interface import SettingInterface

class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.initWindow()

        self.createSubInterface()
        #self.home_Interface = HomeInterface(self)
        self.cal_Interface = CalInterface(self)
        self.auto_Interface = AutoInterface(self)
        self.settingInterface = SettingInterface(self)

        self.splashScreen.finish()
        self.initNavigation()


    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(1000, loop.quit)
        loop.exec()

    def initNavigation(self):
        # add sub interface
        pos = NavigationItemPosition.SCROLL
        #self.addSubInterface(self.home_Interface, FIF.HOME, '主页',pos)
        self.addSubInterface(self.cal_Interface, FIF.LABEL, '控分计算',pos)
        self.addSubInterface(self.auto_Interface, FIF.PLAY, '自动规划',pos)

        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', pos)

    def initWindow(self):
        self.resize(911, 807)
        self.setWindowIcon(QIcon('game_logo.png'))
        self.setWindowTitle('邦邦控分助手 1.0')


        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(250, 250))
        self.splashScreen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()


if __name__ == '__main__':
    #setTheme(Theme.DARK)

    app = QApplication(sys.argv)

    # install translator
    # create application
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    w = Window()
    w.show()
    app.exec()
