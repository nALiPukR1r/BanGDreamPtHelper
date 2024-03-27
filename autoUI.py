# -*- coding: utf-8 -*-

################################################################################
## AutoInterface generated from reading UI file 'cal.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QSizePolicy, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, LineEdit,
                            PrimaryPushButton, PushButton, TextEdit, SwitchButton)

from AutoPlan import autoPlan
import config
from CpLive import CpLive
from ExLive import ExLive
from MatchLive import MatchLive
from MedleyLive import MedleyLive
from MissionLive import MissionLive
from ParaInput import Para
from TeamLive import TeamLive


class UI_AutoInterface(object):
    def setupUi(self, AutoInterface):
        if not AutoInterface.objectName():
            AutoInterface.setObjectName(u"AutoInterface")
        AutoInterface.setMinimumSize(QSize(911, 807))
        self.horizontalLayout = QHBoxLayout(AutoInterface)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 40, 20, 20)
        self.frame_3 = CardWidget(AutoInterface)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 831, 131))
        self.label_4.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 2)

        self.pushButton_2 = PushButton(AutoInterface)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton = PrimaryPushButton(AutoInterface)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.frame = CardWidget(AutoInterface)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(416, 200))
        self.frame.setMaximumSize(QSize(416, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(9, 9, 401, 181))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = BodyLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = BodyLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = BodyLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox = ComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)

        self.lineEdit = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText('当前PT')
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setPlaceholderText('目标PT')
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = CardWidget(AutoInterface)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(416, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(9, 9, 411, 181))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_4 = CardWidget(AutoInterface)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 831, 301))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_result = TextEdit(self.gridLayoutWidget_4)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_result.setTextInteractionFlags(Qt.LinksAccessibleByMouse | Qt.TextEditable)
        self.label_result.setPlaceholderText("计算结果")

        self.lineList = []
        self.labelList = []
        # self.labelCreate(3)
        # labelStr = ["加成倍率", "其他人分数", "支援乐队综合力"]
        # self.labelTextCrate(labelStr)
        # self.lineList[0].setPlaceholderText('如114%加成 - 输入114')
        # self.lineList[1].setPlaceholderText('若单人游戏请输入0')
        # self.lineList[2].setPlaceholderText('支援乐队综合力')

        self.gridLayout_4.addWidget(self.label_result, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 2)

        self.liveType = config.TYPE_NONE
        self.horizontalLayout.addLayout(self.gridLayout)
        self.info = config.notice_auto

        '''

        信号与槽函数，当信号那一行的代码被触发时才会执行（不是顺序执行）

        '''
        # 绑定下拉栏和动态输入界面
        self.comboBox.currentTextChanged.connect(self.dynamicInput)
        self.comboBox.currentTextChanged.connect(self.getInputType)
        self.pushButton.clicked.connect(self.analyze_and_show)

        self.pushButton_2.clicked.connect(self.clearInput)
        self.pushButton_2.clicked.connect(self.clearComboBox)
        # 此输入包括目标和当前pt，只有在用户手动清理以及点击清楚数据按钮时才会清空
        self.inputList_usr = {}
        # 这个输入按照不同的活动区分，当下拉栏切换或手动点击时清空数据
        self.inputList_live = {}

        # 获取输入框输入
        self.lineEdit_2.editingFinished.connect(lambda: self.inputList_usr.update(
            {"Target": self.lineEdit_2.text()}))
        self.lineEdit.editingFinished.connect(lambda: self.inputList_usr.update(
            {"Current": self.lineEdit.text()}))

        self.retranslateUi(AutoInterface)

        QMetaObject.connectSlotsByName(AutoInterface)

    # 当点击“开始计算”时触发的槽函数
    def analyze_and_show(self):
        # for k,v in self.inputList_live.items():
        #     print(k,v)
        res_list = []
        p = Para(int(self.inputList_usr["Target"]), int(self.inputList_usr["Current"]))
        if self.liveType == config.TYPE_MISSION_LIVE:
            mlAP = autoPlan(p,int(self.inputList_live[config.USR_AVG_SCORE]),config.TYPE_MISSION_LIVE,
                            int(self.inputList_live[config.UP_RATE]),False,3,False,False,5,
                            int(self.inputList_live[config.SUPPORT_BAND]))
            res_list = mlAP.auto()

        elif self.liveType == config.TYPE_CP_LIVE:
            clAP = autoPlan(p,int(self.inputList_live[config.USR_AVG_SCORE]),config.TYPE_CP_LIVE,
                            int(self.inputList_live[config.UP_RATE]),self.inputList_live["isCP"])
            res_list = clAP.auto()
        elif self.liveType == config.TYPE_EX_LIVE:
            exlAP = autoPlan(p,int(self.inputList_live[config.USR_AVG_SCORE]),
                             config.TYPE_EX_LIVE,int(self.inputList_live[config.UP_RATE]))
            res_list = exlAP.auto()
        elif self.liveType == config.TYPE_TEAM_LIVE:
            teamAP = autoPlan(p, int(self.inputList_live[config.USR_AVG_SCORE]),
                             config.TYPE_TEAM_LIVE,0,False,3,False,
                              self.inputList_live["isWin"],int(self.inputList_live["ranking"]))
            res_list = teamAP.auto()
        elif self.liveType == config.TYPE_MEDLEY_LIVE:
            mdlAP = autoPlan(p, int(self.inputList_live[config.USR_AVG_SCORE]),
                             config.TYPE_MEDLEY_LIVE,0,False,
                             int(self.inputList_live["songNum"]))
            res_list = mdlAP.auto()
        elif self.liveType == config.TYPE_MATCH_LIVE:
            mtlAP = autoPlan(p, int(self.inputList_live[config.USR_AVG_SCORE]),
                             config.TYPE_MATCH_LIVE,0,False,3,
                             self.inputList_live["isMatch"],False,
                             int(self.inputList_live["ranking"]))
            res_list = mtlAP.auto()
        else:
            pass

        self.label_result.setText('\n'.join(res_list))


    def getInputType(self):

        # 用户指定平均分
        self.lineList[0].editingFinished.connect(lambda: self.inputList_live.update(
            {config.USR_AVG_SCORE: self.lineList[0].text()}))


        if self.liveType == config.TYPE_MISSION_LIVE:
            self.lineList[1].editingFinished.connect(lambda: self.inputList_live.update(
                {config.UP_RATE: self.lineList[1].text()}))
            self.lineList[2].editingFinished.connect(lambda: self.inputList_live.update(
                {config.SUPPORT_BAND: self.lineList[2].text()}))
        elif self.liveType == config.TYPE_CP_LIVE:
            self.lineList[1].editingFinished.connect(lambda: self.inputList_live.update(
                {config.UP_RATE: self.lineList[1].text()}))
            self.inputList_live.update({"isCP": False})
            self.radioButton.checkedChanged.connect(lambda status: self.inputList_live.update({"isCP": status}))
        elif self.liveType == config.TYPE_EX_LIVE:
            self.lineList[1].editingFinished.connect(lambda: self.inputList_live.update(
                {config.UP_RATE: self.lineList[1].text()}))
        elif self.liveType == config.TYPE_TEAM_LIVE:
            self.inputList_live.update({"isWin": False})
            self.radioButton1.checkedChanged.connect(lambda status: self.inputList_live.update({"isWin": status}))
            self.comboBox_ranking.currentTextChanged.connect(lambda index : self.inputList_live.update({"ranking":index}))
        elif self.liveType == config.TYPE_MEDLEY_LIVE:
            self.comboBox_songNum.currentTextChanged.connect(lambda index : self.inputList_live.update({"songNum":index}))
        elif self.liveType == config.TYPE_MATCH_LIVE:
            self.inputList_live.update({"isMatch": False})
            self.radioButton.checkedChanged.connect(lambda status: self.inputList_live.update({"isMatch": status}))
            self.comboBox_ranking.currentTextChanged.connect(
                lambda index: self.inputList_live.update({"ranking": index}))
        else:
            pass

    def clearInput(self):
        #清除左侧
        self.lineEdit_2.clear()
        self.lineEdit.clear()

        for line in self.lineList:
            line.clear()

    def clearComboBox(self):
        if self.liveType == config.TYPE_MEDLEY_LIVE:
            self.comboBox_songNum.setCurrentIndex(-1)
        elif self.liveType == config.TYPE_MATCH_LIVE:
            self.comboBox_ranking.setCurrentIndex(-1)

    # setupUi
    def retranslateUi(self, AutoInterface):
        AutoInterface.setWindowTitle(QCoreApplication.translate("AutoInterface", u"AutoInterface", None))

        self.label_4.setText(QCoreApplication.translate("AutoInterface", self.info, None))

        self.pushButton_2.setText(QCoreApplication.translate("AutoInterface", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton.setText(QCoreApplication.translate("AutoInterface", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("AutoInterface", u"\u76ee\u6807PT", None))
        self.label.setText(QCoreApplication.translate("AutoInterface", u"\u5f53\u524dPT", None))
        self.label_3.setText(QCoreApplication.translate("AutoInterface", u"\u6d3b\u52a8\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("AutoInterface", "请选择活动类型", None))
        self.comboBox.setPlaceholderText("请选择活动类型")
        self.comboBox.setItemText(1, QCoreApplication.translate("AutoInterface", u"\u4efb\u52a1Live", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("AutoInterface", u"CP Live", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("AutoInterface", u"EX Live", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("AutoInterface", u"5v5 Live", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("AutoInterface", u"\u7ec4\u66f2Live", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("AutoInterface", u"\u5bf9\u90a6Live", None))

        #self.label_result.setText(QCoreApplication.translate("AutoInterface", u"\u7ed3\u679c", None))

    # retranslateUi
    def noticeInfo(self, tag):
        info = [
            config.notice_mission_auto,
            config.notice_cp_auto,
            config.notice_ex_auto,
            config.notice_team_auto,
            config.notice_medley_auto,
            config.notice_match_auto,
            config.notice_auto
        ]
        self.info = info[tag]

    def dynamicInput(self, text):
        # self.label_4.setText(text)
        # self.label_4.close()
        self.clearGridLayout(self.gridLayout_3)
        self.liveType = ""
        self.lineList.clear()
        self.labelList.clear()
        self.inputList_live.clear()
        self.liveType = config.TYPE_LIVE_LIST[text]

        if text == '任务Live':
            self.noticeInfo(0)
            self.labelCreate(3)
            labelStr = ["平均分数","固定加成倍率", "支援乐队综合力"]
            self.labelTextCrate(labelStr)
            self.lineList[0].setPlaceholderText('平均分数')
            self.lineList[1].setPlaceholderText('如114%加成 - 输入114')
            self.lineList[2].setPlaceholderText('支援乐队综合力')
        elif text == "CP Live":
            self.noticeInfo(1)
            self.labelCreate(2)
            labelStr = ["平均分数","加成倍率"]
            self.labelTextCrate(labelStr)
            self.lineList[0].setPlaceholderText('平均分数')
            self.lineList[1].setPlaceholderText('如114%加成 - 输入114')
            self.addSwitchButton(3, "挑战Live(否/是)", None, 3)
        elif text == "EX Live":
            self.noticeInfo(2)
            self.labelCreate(2)
            labelStr = ["平均分数","加成倍率"]
            self.lineList[0].setPlaceholderText('平均分数')
            self.lineList[1].setPlaceholderText('如114%加成 - 输入114')
            self.labelTextCrate(labelStr)
        elif text == "5v5 Live":
            self.labelCreate(1)
            labelStr = ["平均分数"]
            self.lineList[0].setPlaceholderText('平均分数')
            self.labelTextCrate(labelStr)
            self.noticeInfo(3)

            idx = 2
            self.label_swtbtn1 = BodyLabel(self.gridLayoutWidget_3)
            self.label_swtbtn1.setObjectName(f"label_btn_{idx}")
            self.gridLayout_3.addWidget(self.label_swtbtn1, idx, 0, 1, 1)
            self.label_swtbtn1.setText(QCoreApplication.translate("AutoInterface", "输/赢", None))

            self.label_ranking = BodyLabel(self.gridLayoutWidget_3)
            self.label_ranking.setObjectName(u"label_ranking ")
            self.gridLayout_3.addWidget(self.label_ranking, 1, 0, 1, 1)
            self.label_ranking.setText(QCoreApplication.translate("AutoInterface", u"队伍内排名", None))

            self.comboBox_ranking = ComboBox(self.gridLayoutWidget_3)
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .addItem("")
            self.comboBox_ranking .setObjectName(u"comboBox_ranking")
            self.comboBox_ranking .setPlaceholderText("请选择队伍内排名")
            self.comboBox_ranking .setItemText(0,
                                              QCoreApplication.translate("AutoInterface", u"请选择队伍内排名", None))
            self.comboBox_ranking .setItemText(1, QCoreApplication.translate("AutoInterface", u"5", None))
            self.comboBox_ranking .setItemText(2, QCoreApplication.translate("AutoInterface", u"4", None))
            self.comboBox_ranking .setItemText(3, QCoreApplication.translate("AutoInterface", u"3", None))
            self.comboBox_ranking .setItemText(4, QCoreApplication.translate("AutoInterface", u"2", None))
            self.comboBox_ranking .setItemText(5, QCoreApplication.translate("AutoInterface", u"1", None))
            self.gridLayout_3.addWidget(self.comboBox_ranking , 1, 1, 1, 1)

            self.radioButton1 = SwitchButton(self.gridLayoutWidget_3)
            self.radioButton1.checkedChanged.connect(self.onCheckedChanged_winloss)
            self.radioButton1.setObjectName(u"radioButton1")
            self.gridLayout_3.addWidget(self.radioButton1, idx, 1, 1, 1)
            self.radioButton1.setText(QCoreApplication.translate("AutoInterface", "", None))
        elif text == "组曲Live":
            self.labelCreate(1)
            labelStr = ["平均分数"]
            self.lineList[0].setPlaceholderText('平均分数')
            self.labelTextCrate(labelStr)

            self.noticeInfo(4)
            self.label_songNum = BodyLabel(self.gridLayoutWidget_3)
            self.label_songNum .setObjectName(u"label_songNum ")
            self.gridLayout_3.addWidget(self.label_songNum , 1, 0, 1, 1)
            self.label_songNum.setText(QCoreApplication.translate("AutoInterface", u"歌曲数量", None))

            self.comboBox_songNum = ComboBox(self.gridLayoutWidget_3)
            self.comboBox_songNum.addItem("")
            self.comboBox_songNum.addItem("")
            self.comboBox_songNum.addItem("")
            self.comboBox_songNum.addItem("")
            self.comboBox_songNum.setObjectName(u"comboBox_songNum")
            self.comboBox_songNum.setPlaceholderText("请选择完成歌曲数量")
            self.comboBox_songNum.setItemText(0, QCoreApplication.translate("AutoInterface", u"请选择完成歌曲数量", None))
            self.comboBox_songNum.setItemText(1, QCoreApplication.translate("AutoInterface", u"1", None))
            self.comboBox_songNum.setItemText(2, QCoreApplication.translate("AutoInterface", u"2", None))
            self.comboBox_songNum.setItemText(3, QCoreApplication.translate("AutoInterface", u"3", None))
            self.gridLayout_3.addWidget(self.comboBox_songNum, 1, 1, 1, 1)
        elif text == "对邦Live":
            self.labelCreate(1)
            labelStr = ["平均分数"]
            self.lineList[0].setPlaceholderText('平均分数')
            self.labelTextCrate(labelStr)

            self.noticeInfo(5)
            self.addSwitchButton(2, "自由/对邦", None, 1)

            self.label_rank = BodyLabel(self.gridLayoutWidget_3)
            self.label_rank.setObjectName(u"label_songNum ")
            self.gridLayout_3.addWidget(self.label_rank, 1, 0, 1, 1)
            self.label_rank.setText(QCoreApplication.translate("AutoInterface", u"排名", None))

            self.comboBox_ranking = ComboBox(self.gridLayoutWidget_3)
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.addItem("")
            self.comboBox_ranking.setObjectName(u"comboBox_ranking")
            self.comboBox_ranking.setPlaceholderText("请选择排名")
            self.comboBox_ranking.setItemText(0,
                                              QCoreApplication.translate("AutoInterface", u"请选择排名", None))
            self.comboBox_ranking.setItemText(1, QCoreApplication.translate("AutoInterface", u"5", None))
            self.comboBox_ranking.setItemText(2, QCoreApplication.translate("AutoInterface", u"4", None))
            self.comboBox_ranking.setItemText(3, QCoreApplication.translate("AutoInterface", u"3", None))
            self.comboBox_ranking.setItemText(4, QCoreApplication.translate("AutoInterface", u"2", None))
            self.comboBox_ranking.setItemText(5, QCoreApplication.translate("AutoInterface", u"1", None))
            self.gridLayout_3.addWidget(self.comboBox_ranking, 1, 1, 1, 1)
            # self.radioButton.setChecked(True)
        else:
            self.noticeInfo(6)
            # self.labelCreate(0)

        self.label_4.setText(self.info)
        self.label_result.clear()
        # self.getInputType()

    def clearInput(self):

        #清除左侧
        self.lineEdit_2.clear()
        self.lineEdit.clear()

        #清除右侧,fingChildren的返回结果是列表
        for line in self.lineList:
            line.clear()

    def labelTextCrate(self, list):

        for index, item in enumerate(list):
            self.labelList[index].setText(QCoreApplication.translate("AutoInterface", item, None))

    def labelCreate(self, num):
        for i in range(num):
            self.lineList.append(LineEdit(self.gridLayoutWidget_3))
            self.lineList[i].setObjectName(f"lineEdit_spLive_{i}")
            self.gridLayout_3.addWidget(self.lineList[i], i, 1, 1, 1)

            self.labelList.append(BodyLabel(self.gridLayoutWidget_3))
            self.labelList[i].setObjectName(f"label_splive_{i}")

            self.gridLayout_3.addWidget(self.labelList[i], i, 0, 1, 1)

    def addSwitchButton(self, idx, text1, text2,text_choose):
        self.label_swtbtn = BodyLabel(self.gridLayoutWidget_3)
        self.label_swtbtn.setObjectName(f"label_btn_{idx}")
        self.gridLayout_3.addWidget(self.label_swtbtn, idx, 0, 1, 1)
        self.label_swtbtn.setText(QCoreApplication.translate("AutoInterface", text1, None))

        self.radioButton = SwitchButton(self.gridLayoutWidget_3)

        if text_choose == 1:
            self.radioButton.checkedChanged.connect(self.onCheckedChanged)
        elif text_choose == 2:
            self.radioButton.checkedChanged.connect(self.onCheckedChanged_winloss)
        else:
            self.radioButton.checkedChanged.connect(self.onCheckedChanged_yesno)

        self.radioButton.setObjectName(u"radioButton")
        self.gridLayout_3.addWidget(self.radioButton, idx, 1, 1, 1)
        self.radioButton.setText(QCoreApplication.translate("AutoInterface", "", None))

    # def onCheckedChanged_test(self, isChecked: bool, on, off, button):
    #     text = on if isChecked else off
    #     button.setText(text)

    def onCheckedChanged(self, isChecked: bool):
        text = "对邦" if isChecked else "自由"
        self.radioButton.setText(text)

    def onCheckedChanged_winloss(self, isChecked: bool):
        text = "赢" if isChecked else "输"
        self.radioButton1.setText(text)

    def onCheckedChanged_yesno(self, isChecked: bool):
        text = "是" if isChecked else "否"
        self.radioButton.setText(text)

    def clearGridLayout(self, layout):
        """
        Clears all widgets from the given QGridLayout.

        Parameters:
        layout (QGridLayout): The layout from which widgets should be removed.
        """
        # 存储要删除的控件列表
        widgetsToDelete = []

        # 遍历布局中的所有控件
        for i in range(layout.count()):
            # 获取控件
            child = layout.takeAt(0)
            widget = child.widget()

            # 如果控件存在，将其添加到删除列表中
            if widget is not None:
                widgetsToDelete.append(widget)

        # 删除所有控件
        for widget in widgetsToDelete:
            layout.removeWidget(widget)
            widget.deleteLater()

