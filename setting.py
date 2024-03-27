# -*- coding: utf-8 -*-
import json

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import config
from DataValidation import intCheck
import sys
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, InfoBarManager
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QWidget)
from qfluentwidgets import FluentIcon as FIF


from qfluentwidgets import (BodyLabel, CardWidget, HyperlinkButton, LineEdit,
    PrimaryPushButton, PushButton)

import config
from DataValidation import intCheck


class Ui_Setting(object):
    def setupUi(self, Setting):
        if not Setting.objectName():
            Setting.setObjectName(u"Setting")
        Setting.resize(911, 807)
        Setting.setMinimumSize(QSize(911, 807))
        self.gridLayoutWidget = QWidget(Setting)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(180, 10, 551, 361))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = CardWidget(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 531, 341))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_3 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit_7 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.lineEdit_8 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.lineEdit_6 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.label_3 = BodyLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_7 = BodyLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_10 = BodyLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)

        self.label_6 = BodyLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.lineEdit_4 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_4 = BodyLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_2 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label = BodyLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = BodyLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = BodyLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_5 = LineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.pushButton = PushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = PrimaryPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton_6 = PushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_7 = PrimaryPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_3.addWidget(self.pushButton_7, 3, 2, 1, 1)

        self.pushButton_8 = PushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_3.addWidget(self.pushButton_8, 4, 2, 1, 1)

        self.pushButton_9 = PrimaryPushButton(self.gridLayoutWidget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_3.addWidget(self.pushButton_9, 5, 2, 1, 1)

        self.pushButton_10 = PushButton(self.gridLayoutWidget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_3.addWidget(self.pushButton_10, 6, 2, 1, 1)

        self.pushButton_11 = PrimaryPushButton(self.gridLayoutWidget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_3.addWidget(self.pushButton_11, 7, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_3 = CardWidget(Setting)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 380, 891, 211))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_3)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 871, 191))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = BodyLabel(self.gridLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.pushButton_bd = HyperlinkButton(
            url='https://bestdori.com/',
            text='BestDori',
            parent=self.gridLayoutWidget_4,
            icon=FIF.BOOK_SHELF
        )
        self.pushButton_bd.setObjectName(u"pushButton_bd")

        self.gridLayout_4.addWidget(self.pushButton_bd, 2, 0, 1, 1)

        self.pushButton_official = HyperlinkButton(
            url='https://space.bilibili.com/171818544',
            text='邦邦官方账号',
            parent=self.gridLayoutWidget_4,
            icon=FIF.LINK
        )
        self.pushButton_official.setObjectName(u"pushButton_official")

        self.gridLayout_4.addWidget(self.pushButton_official, 2, 1, 1, 1)

        self.pushButton_mygo = HyperlinkButton(
            url='https://space.bilibili.com/1459104794',
            text='MyGo_AveMujica',
            parent=self.gridLayoutWidget_4,
            icon=FIF.LINK
        )

        self.pushButton_mygo.setObjectName(u"pushButton_mygo")

        self.gridLayout_4.addWidget(self.pushButton_mygo, 2, 2, 1, 1)

        self.pushButton_document = HyperlinkButton(
            url='https://www.bilibili.com/read/cv33421271/',
            text='使用说明',
            parent=self.gridLayoutWidget_4,
            icon=FIF.HELP
        )

        self.pushButton_document.setObjectName(u"pushButton_document")

        self.gridLayout_4.addWidget(self.pushButton_document, 2, 3, 1, 1)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 4)

        self.frame_4 = CardWidget(Setting)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 600, 891, 201))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_4)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 871, 181))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_5 = HyperlinkButton(
            url='https://gitee.com/nALiPukR1r/bangdream-pt-helper/issues',
            text='反馈',
            parent=self.gridLayoutWidget_5,
            icon=FIF.CHAT
        )
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 2, 2, 1, 1)

        self.pushButton_3 = HyperlinkButton(
            url='https://gitee.com/nALiPukR1r/bangdream-pt-helper',
            text='项目地址',
            parent=self.gridLayoutWidget_5,
            icon=FIF.GITHUB
        )
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_default = PushButton(self.gridLayoutWidget_5)
        self.pushButton_default.setObjectName(u"pushButton_default")

        self.gridLayout_5.addWidget(self.pushButton_default, 2, 3, 1, 1)

        self.label_9 = BodyLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 4)

        self.pushButton_4 = HyperlinkButton(
            url='https://www.bilibili.com/read/cv20061259',
            text='控分原理',
            parent=self.gridLayoutWidget_5,
            icon=FIF.INFO
        )
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.line2 = QFrame(self.gridLayoutWidget_4)
        self.line2.setObjectName(u"line2")
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4.addWidget(self.line2, 1, 0, 1, 4)

        self.line = QFrame(self.gridLayoutWidget_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.config_dict = {
            "SCORE_MISSION_MAX": "#",
            "SCORE_EX_MAX": "#",
            "SCORE_CP_MAX": "#",
            "SCORE_MATCH_MAX": "#",
            "SCORE_TEAM_MAX": "#",
            "SCORE_MEDLEY_MAX": "#",
            "SCORE_MIN_DEATH": "#",
            "SCORE_MIN": "#",
            "SCORE_MIN_MEDLEY": "#",
            "STEP_MAX": "#",
            "UP_RATE_MAX": "#"
        }

        self.load()

        self.pushButton.clicked.connect(self.edit_config_mission)
        self.pushButton_2.clicked.connect(self.edit_config_cp)
        self.pushButton_6.clicked.connect(self.edit_config_ex)
        self.pushButton_7.clicked.connect(self.edit_config_team)
        self.pushButton_8.clicked.connect(self.edit_config_medley)
        self.pushButton_9.clicked.connect(self.edit_config_match)
        self.pushButton_10.clicked.connect(self.edit_config_medley_min)
        self.pushButton_11.clicked.connect(self.edit_config_uprate)
        self.pushButton_default.clicked.connect(self.setDefault)

        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 4)


        self.retranslateUi(Setting)

        QMetaObject.connectSlotsByName(Setting)
    # setupUi

    def retranslateUi(self, Setting):
        about = "版本1.0\n本软件为开源软件，使用GPLv3授权。\nUI部分使用了QFluentWidgets组件库。\n详见下方项目地址；控分原理请参阅专栏。\nPs：个人开发水平有限，结果仅具有参考价值，算法和设置的不合理请多理解"
        Setting.setWindowTitle(QCoreApplication.translate("Setting", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Setting", u"EX Live - \u6700\u9ad8\u5206", None))
        self.label_7.setText(QCoreApplication.translate("Setting", u"\u7ec4\u66f2Live - \u6700\u4f4e\u5206", None))
        self.label_10.setText(QCoreApplication.translate("Setting", u"加成倍率 - 最大值", None))
        self.label_6.setText(QCoreApplication.translate("Setting", u"\u5bf9\u90a6Live - \u6700\u9ad8\u5206", None))
        self.label_4.setText(QCoreApplication.translate("Setting", u"5v5 Live - \u6700\u9ad8\u5206", None))
        self.label.setText(QCoreApplication.translate("Setting", u"\u4efb\u52a1Live - \u6700\u9ad8\u5206", None))
        self.label_2.setText(QCoreApplication.translate("Setting", u"CP Live - \u6700\u9ad8\u5206", None))
        self.label_5.setText(QCoreApplication.translate("Setting", u"\u7ec4\u66f2Live - \u6700\u9ad8\u5206", None))
        self.pushButton.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_6.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_7.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_8.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_9.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_10.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.pushButton_11.setText(QCoreApplication.translate("Setting", u"\u66f4\u65b0", None))
        self.label_8.setText(QCoreApplication.translate("Setting", config.HELP, None))
        self.pushButton_5.setText(QCoreApplication.translate("Setting", u"\u53cd\u9988", None))
        self.pushButton_3.setText(QCoreApplication.translate("Setting", u"\u9879\u76ee\u5730\u5740", None))
        self.label_9.setText(QCoreApplication.translate("Setting", about, None))
        #self.pushButton_4.setText(QCoreApplication.translate("Setting", u"\u5e2e\u52a9\u6587\u6863", None))
        self.pushButton_default.setText(QCoreApplication.translate("Setting", u"恢复默认设置", None))
    # retranslateUi

    def load(self):
        self.config_dict = {
            "SCORE_MISSION_MAX": "#",
            "SCORE_EX_MAX": "#",
            "SCORE_CP_MAX": "#",
            "SCORE_MATCH_MAX": "#",
            "SCORE_TEAM_MAX": "#",
            "SCORE_MEDLEY_MAX": "#",
            "SCORE_MIN_DEATH": "#",
            "SCORE_MIN": "#",
            "SCORE_MIN_MEDLEY": "#",
            "STEP_MAX": "#",
            "UP_RATE_MAX": "#"
        }
        self.lineEdit.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_MISSION_MAX": self.lineEdit.text()}))
        self.lineEdit_2.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_CP_MAX": self.lineEdit_2.text()}))
        self.lineEdit_3.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_EX_MAX": self.lineEdit_3.text()}))
        self.lineEdit_4.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_TEAM_MAX": self.lineEdit_4.text()}))
        self.lineEdit_5.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_MEDLEY_MAX": self.lineEdit_5.text()}))
        self.lineEdit_6.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_MATCH_MAX": self.lineEdit_6.text()}))
        self.lineEdit_7.editingFinished.connect(
            lambda: self.config_dict.update({"SCORE_MIN_MEDLEY": self.lineEdit_7.text()}))
        self.lineEdit_8.editingFinished.connect(
            lambda: self.config_dict.update({"UP_RATE_MAX": self.lineEdit_8.text()}))

    def edit_config_mission(self):
        num = self.config_dict["SCORE_MISSION_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_MISSION_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)

            self.createSuccessInfoBar()

    def edit_config_cp(self):
        num = self.config_dict["SCORE_CP_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_CP_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()

    def edit_config_ex(self):
        num = self.config_dict["SCORE_EX_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_EX_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()
    def edit_config_team(self):
        num = self.config_dict["SCORE_TEAM_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_TEAM_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()
    def edit_config_medley(self):
        num = self.config_dict["SCORE_MEDLEY_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_MEDLEY_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()
    def edit_config_match(self):
        num = self.config_dict["SCORE_MATCH_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_MATCH_MAX"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()
    def edit_config_medley_min(self):
        num = self.config_dict["SCORE_MIN_MEDLEY"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["SCORE_MIN_MEDLEY"] = int(num)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()
    def edit_config_uprate(self):
        num = self.config_dict["UP_RATE_MAX"]
        if intCheck(num) != config.CORRECT:
            self.createErrorInfoBar()
        else:
            config.config_data["UserSetting"]["UP_RATE_MAX"] = round(int(num) / 100,2)
            # 将修改后的配置数据写回JSON文件
            with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
                json.dump(config.config_data, file, indent=4)
            self.createSuccessInfoBar()



    def createSuccessInfoBar(self):
        # convenient class mothod
        InfoBar.success(
            title='修改成功！',
            content="新的设置将在重启后生效",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

    def createSuccessInfoBar_default(self):
        # convenient class mothod
        InfoBar.success(
            title='恢复初始设置成功！',
            content="所有设置更改将在重启后生效",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

    def createErrorInfoBar(self):
        InfoBar.error(
            title='修改失败！',
            content="【Error : 输入的数据有误】",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2000,  # won't disappear automatically
            parent=self
        )

    def setDefault(self):
        CONFIG_PATH = "config\config.json"
        # print(CONFIG_PATH)
        with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        config.config_data["UserSetting"]["SCORE_MISSION_MAX"] = config.config_data["DefaultSetting"]["SCORE_MISSION_MAX"]
        config.config_data["UserSetting"]["SCORE_EX_MAX"] = config.config_data["DefaultSetting"]["SCORE_EX_MAX"]
        config.config_data["UserSetting"]["SCORE_CP_MAX"] = config.config_data["DefaultSetting"]["SCORE_CP_MAX"]
        config.config_data["UserSetting"]["SCORE_MATCH_MAX"] = config.config_data["DefaultSetting"]["SCORE_MATCH_MAX"]
        config.config_data["UserSetting"]["SCORE_TEAM_MAX"] = config.config_data["DefaultSetting"]["SCORE_TEAM_MAX"]
        config.config_data["UserSetting"]["SCORE_MIN_DEATH"] = config.config_data["DefaultSetting"]["SCORE_MIN_DEATH"]
        config.config_data["UserSetting"]["SCORE_MEDLEY_MAX"] = config.config_data["DefaultSetting"]["SCORE_MEDLEY_MAX"]
        config.config_data["UserSetting"]["SCORE_MIN"] = config.config_data["DefaultSetting"]["SCORE_MIN"]
        config.config_data["UserSetting"]["SCORE_MIN_MEDLEY"] = config.config_data["DefaultSetting"]["SCORE_MIN_MEDLEY"]
        config.config_data["UserSetting"]["STEP_MAX"] = config.config_data["DefaultSetting"]["STEP_MAX"]
        config.config_data["UserSetting"]["UP_RATE_MAX"] = config.config_data["DefaultSetting"]["UP_RATE_MAX"]
        with open(config.CONFIG_PATH, 'w', encoding='utf-8') as file:
            json.dump(config.config_data, file, indent=4)

        self.createSuccessInfoBar_default()
