# coding:utf-8
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon, setFont, InfoBarIcon

#from test1 import Ui_Form
from cal_ui import UI_CalInterface


class CalInterface(UI_CalInterface, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        #set the icon of button
        # self.pinButton.setIcon(FluentIcon.PIN)
        # self.moreButton.setIcon(FluentIcon.MORE)
        # self.startFocusButton.setIcon(FluentIcon.POWER_BUTTON)
        # self.editButton.setIcon(FluentIcon.EDIT)
        # self.addTaskButton.setIcon(FluentIcon.ADD)
        # self.moreTaskButton.setIcon(FluentIcon.MORE)
        # self.taskIcon1.setIcon(InfoBarIcon.SUCCESS)
        # self.taskIcon2.setIcon(InfoBarIcon.WARNING)
        # self.taskIcon3.setIcon(InfoBarIcon.WARNING)
        #
        # setFont(self.progressRing, 16)

        # add shadow effect to card
        self.setShadowEffect(self.frame)
        self.setShadowEffect(self.frame_2)
        self.setShadowEffect(self.frame_3)
        self.setShadowEffect(self.frame_4)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)
