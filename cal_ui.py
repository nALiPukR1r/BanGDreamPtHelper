# -*- coding: utf-8 -*-

################################################################################
## CalInterface generated from reading UI file 'cal.ui'
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
                               QLabel, QSizePolicy, QWidget, QLineEdit)

from qfluentwidgets import (BodyLabel, CardWidget, ComboBox, LineEdit,
                            PrimaryPushButton, PushButton, TextEdit, SwitchButton)
import config
from CpLive import CpLive
from ExLive import ExLive
from MatchLive import MatchLive
from MedleyLive import MedleyLive
from MissionLive import MissionLive
from ParaInput import Para
from TeamLive import TeamLive


class UI_CalInterface(object):
    def setupUi(self, CalInterface):
        if not CalInterface.objectName():
            CalInterface.setObjectName(u"CalInterface")
        CalInterface.setMinimumSize(QSize(911, 807))
        self.horizontalLayout = QHBoxLayout(CalInterface)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 40, 20, 20)
        self.frame_3 = CardWidget(CalInterface)
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
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 2)

        self.pushButton_2 = PushButton(CalInterface)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton = PrimaryPushButton(CalInterface)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.frame = CardWidget(CalInterface)
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

        self.frame_2 = CardWidget(CalInterface)
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

        self.frame_4 = CardWidget(CalInterface)
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
        self.label_5 = TextEdit(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.lineList = []
        self.labelList = []
        # self.labelCreate(3)
        # labelStr = ["加成倍率", "其他人分数", "支援乐队综合力"]
        # self.labelTextCrate(labelStr)
        # self.lineList[0].setPlaceholderText('如114%加成 - 输入114')
        # self.lineList[1].setPlaceholderText('若单人游戏请输入0')
        # self.lineList[2].setPlaceholderText('支援乐队综合力')

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 2)

        self.liveType = config.TYPE_NONE
        self.horizontalLayout.addLayout(self.gridLayout)
        self.info = config.notice_cal

        '''
        
        信号与槽函数，当信号那一行的代码被触发时才会执行（不是顺序执行）
        
        '''
        # 绑定下拉栏和动态输入界面
        self.comboBox.currentTextChanged.connect(self.dynamicInput)

        self.pushButton.clicked.connect(self.analyze_and_show)
        self.pushButton_2.clicked.connect(self.clearInput)

        # 此输入包括目标和当前pt，只有在用户手动清理以及点击清楚数据按钮时才会清空
        self.inputList_usr = {}
        # 这个输入按照不同的活动区分，当下拉栏切换或手动点击时清空数据
        self.inputList_live = {}

        #获取输入框输入
        self.lineEdit_2.editingFinished.connect(lambda : self.inputList_usr.update(
            {"Target": self.lineEdit_2.text()}))
        self.lineEdit.editingFinished.connect(lambda : self.inputList_usr.update(
            {"Current": self.lineEdit.text()}))

        self.retranslateUi(CalInterface)

        QMetaObject.connectSlotsByName(CalInterface)

    # 当点击“开始计算”时触发的槽函数
    def analyze_and_show(self):
        # for k,v in self.inputList_usr.items():
        #     print(k,v)
        res_list = []
        p = Para(int(self.inputList_usr["Target"]),int(self.inputList_usr["Current"]))
        if self.liveType == config.TYPE_MISSION_LIVE:
            ml = MissionLive(p,int(self.inputList_live[config.UP_RATE]),
                int(self.inputList_live[config.OTHERS_SCORE]),int(self.inputList_live[config.SUPPORT_BAND]))
            res_list = ml.ScoreCal()


        elif self.liveType == config.TYPE_CP_LIVE:
            cl = CpLive(p, int(self.inputList_live[config.UP_RATE]),
                                int(self.inputList_live[config.OTHERS_SCORE]),
                                self.inputList_live["isCP"])
            res_list = cl.ScoreCal()
        elif self.liveType == config.TYPE_EX_LIVE:
            exl = ExLive(p, int(self.inputList_live[config.UP_RATE]),
                             int(self.inputList_live[config.OTHERS_SCORE]))
            res_list = exl.ScoreCal()

        elif self.liveType == config.TYPE_TEAM_LIVE:
            tl = TeamLive(p,self.inputList_live["isWin"],self.inputList_live["easyMode"])
            res_list = tl.ScoreCal()
        elif self.liveType == config.TYPE_MEDLEY_LIVE:
            mdl = MedleyLive(p)
            res_list = mdl.ScoreCal()
        elif self.liveType == config.TYPE_MATCH_LIVE:
            mtl = MatchLive(p,self.inputList_live["easyMode"])
            res_list = mtl.ScoreCal()
        else:
            pass

        text = '\n-------------------------------------------------------------\n'.join(res_list)
        self.label_5.setText(text)


    def getInputType(self):
        if self.liveType == config.TYPE_MISSION_LIVE:
            self.lineList[0].editingFinished.connect(lambda :self.inputList_live.update(
                {config.UP_RATE : self.lineList[0].text()}))
            self.lineList[1].editingFinished.connect(lambda :self.inputList_live.update(
                {config.OTHERS_SCORE:self.lineList[1].text()}))
            self.lineList[2].editingFinished.connect(lambda :self.inputList_live.update(
                {config.SUPPORT_BAND : self.lineList[2].text()}))
        elif self.liveType == config.TYPE_CP_LIVE:
            self.lineList[0].editingFinished.connect(lambda :self.inputList_live.update(
                {config.UP_RATE:self.lineList[0].text()}))
            self.lineList[1].editingFinished.connect(lambda :self.inputList_live.update(
                {config.OTHERS_SCORE:self.lineList[1].text()}))
            self.inputList_live.update({"isCP":False})
            self.radioButton.checkedChanged.connect(lambda status: self.inputList_live.update({"isCP":status}))
        elif self.liveType == config.TYPE_EX_LIVE:
            self.lineList[0].editingFinished.connect(lambda :self.inputList_live.update(
                {config.UP_RATE:self.lineList[0].text()}))
            self.lineList[1].editingFinished.connect(lambda :self.inputList_live.update(
                {config.OTHERS_SCORE:self.lineList[1].text()}))
        elif self.liveType == config.TYPE_TEAM_LIVE:
            self.inputList_live.update({"isWin": False})
            self.inputList_live.update({"easyMode": True})
            self.radioButton1.checkedChanged.connect(lambda status: self.inputList_live.update({"isWin":status}))
            self.radioButton2.checkedChanged.connect(lambda status: self.inputList_live.update({"easyMode":status}))
        elif self.liveType == config.TYPE_MEDLEY_LIVE:
            pass
        elif self.liveType == config.TYPE_MATCH_LIVE:
            self.inputList_live.update({"easyMode": True})
            self.radioButton.checkedChanged.connect(lambda status: self.inputList_live.update({"easyMode": status}))
        else:
            pass

    # setupUi
    def retranslateUi(self, CalInterface):
        CalInterface.setWindowTitle(QCoreApplication.translate("CalInterface", u"CalInterface", None))

        self.label_4.setText(QCoreApplication.translate("CalInterface", self.info, None))

        self.pushButton_2.setText(QCoreApplication.translate("CalInterface", u"\u6e05\u7a7a\u6570\u636e", None))
        self.pushButton.setText(QCoreApplication.translate("CalInterface", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("CalInterface", u"\u76ee\u6807PT", None))
        self.label.setText(QCoreApplication.translate("CalInterface", u"\u5f53\u524dPT", None))
        self.label_3.setText(QCoreApplication.translate("CalInterface", u"\u6d3b\u52a8\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CalInterface", "请选择活动类型", None))
        self.comboBox.setPlaceholderText("请选择活动类型")
        self.comboBox.setItemText(1, QCoreApplication.translate("CalInterface", u"\u4efb\u52a1Live", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("CalInterface", u"CP Live", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("CalInterface", u"EX Live", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("CalInterface", u"5v5 Live", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("CalInterface", u"\u7ec4\u66f2Live", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("CalInterface", u"\u5bf9\u90a6Live", None))

        #self.label_5.setText(QCoreApplication.translate("CalInterface", u"\u7ed3\u679c", None))
        self.label_5.setPlaceholderText("计算结果")
    # retranslateUi
    def noticeInfo(self,tag):
        info = [
            config.notice_mission,
            config.notice_cp,
            config.notice_ex,
            config.notice_team,
            config.notice_medley,
            config.notice_match,
            config.notice_cal,
        ]
        self.info = info[tag]

    def clearInput(self):

        # 清除左侧
        self.lineEdit_2.clear()
        self.lineEdit.clear()

        for line in self.lineList:
            line.clear()

    # def clearComboBox(self):
    #     self.comboBox_songNum.setCurrentIndex(-1)

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
            labelStr = ["加成倍率","其他人分数","支援乐队综合力"]
            self.labelTextCrate(labelStr)
            self.lineList[0].setPlaceholderText('如114%加成 - 输入114')
            self.lineList[1].setPlaceholderText('若单人游戏请输入0')
            self.lineList[2].setPlaceholderText('支援乐队综合力')
        elif text == "CP Live":
            self.noticeInfo(1)
            self.labelCreate(2)
            labelStr = ["加成倍率", "其他人分数"]
            self.labelTextCrate(labelStr)
            self.lineList[0].setPlaceholderText('如114%加成 - 输入114')
            self.lineList[1].setPlaceholderText('若单人游戏请输入0')
            #self.lineList[2].setPlaceholderText('若单人游戏请输入0')
            self.addSwitchButton(3,"挑战Live(否/是)",None,False,3)
        elif text == "EX Live":
            self.noticeInfo(2)
            self.labelCreate(2)
            labelStr = ["加成倍率", "其他人分数"]
            self.lineList[0].setPlaceholderText('如114%加成 - 输入114')
            self.lineList[1].setPlaceholderText('若单人游戏请输入0')
            self.labelTextCrate(labelStr)
        elif text == "5v5 Live":
            self.noticeInfo(3)
            #self.labelCreate(0)
            self.addSwitchButton(0, "输/赢","精简模式",True,0)
            self.radioButton2.setChecked(True)
        elif text == "组曲Live":
            self.noticeInfo(4)

        elif text == "对邦Live":
            self.noticeInfo(5)
            #self.labelCreate(0)
            self.addSwitchButton(1, "精简模式",None,False,1)
            self.radioButton.setChecked(True)
        else:
            self.noticeInfo(6)
            #self.labelCreate(0)
        self.label_5.clear()
        self.label_4.setText(self.info)
        self.getInputType()

    def labelTextCrate(self,list):

        for index, item in enumerate(list):
            self.labelList[index].setText(QCoreApplication.translate("CalInterface", item, None))

    def labelCreate(self, num):
        for i in range(num):
            self.lineList.append(LineEdit(self.gridLayoutWidget_3))
            self.lineList[i].setObjectName(f"lineEdit_spLive_{i}")
            self.gridLayout_3.addWidget(self.lineList[i], i, 1, 1, 1)

            self.labelList.append(BodyLabel(self.gridLayoutWidget_3))
            self.labelList[i].setObjectName(f"label_splive_{i}")

            self.gridLayout_3.addWidget(self.labelList[i], i, 0, 1, 1)

    def addSwitchButton(self,idx,text1,text2,flag,text_choose):

        if flag:
            self.label_swtbtn1 = BodyLabel(self.gridLayoutWidget_3)
            self.label_swtbtn1.setObjectName(f"label_btn_{idx}")
            self.gridLayout_3.addWidget(self.label_swtbtn1, idx, 0, 1, 1)
            self.label_swtbtn1.setText(QCoreApplication.translate("CalInterface", text1, None))

            self.label_swtbtn2 = BodyLabel(self.gridLayoutWidget_3)
            self.label_swtbtn2.setObjectName(f"label_btn_{idx+1}")
            self.gridLayout_3.addWidget(self.label_swtbtn2, idx+1, 0, 1, 1)
            self.label_swtbtn2.setText(QCoreApplication.translate("CalInterface", text2, None))

            self.radioButton1 = SwitchButton(self.gridLayoutWidget_3)
            self.radioButton2 = SwitchButton(self.gridLayoutWidget_3)

            self.radioButton1.checkedChanged.connect(self.onCheckedChanged_winloss)
            self.radioButton2.checkedChanged.connect(self.onCheckedChanged_2)

            self.radioButton1.setObjectName(u"radioButton1")
            self.gridLayout_3.addWidget(self.radioButton1, idx, 1, 1, 1)
            self.radioButton1.setText(QCoreApplication.translate("CalInterface", "", None))

            self.radioButton2.setObjectName(u"radioButton2")
            self.gridLayout_3.addWidget(self.radioButton2, idx+1, 1, 1, 1)
            self.radioButton2.setText(QCoreApplication.translate("CalInterface", "", None))
        else:

            self.label_swtbtn = BodyLabel(self.gridLayoutWidget_3)
            self.label_swtbtn.setObjectName(f"label_btn_{idx}")
            self.gridLayout_3.addWidget(self.label_swtbtn, idx, 0, 1, 1)
            self.label_swtbtn.setText(QCoreApplication.translate("CalInterface", text1, None))

            self.radioButton = SwitchButton(self.gridLayoutWidget_3)

            if text_choose == 1:
                self.radioButton.checkedChanged.connect(self.onCheckedChanged)
            elif text_choose == 2:
                self.radioButton.checkedChanged.connect(self.onCheckedChanged_winloss)
            else:
                self.radioButton.checkedChanged.connect(self.onCheckedChanged_yesno)

            self.radioButton.setObjectName(u"radioButton")
            self.gridLayout_3.addWidget(self.radioButton, idx, 1, 1, 1)
            self.radioButton.setText(QCoreApplication.translate("CalInterface", "", None))

    # def onCheckedChanged_test(self, isChecked: bool, on, off, button):
    #     text = on if isChecked else off
    #     button.setText(text)

    def onCheckedChanged(self, isChecked: bool):
        text = "开" if isChecked else "关"
        self.radioButton.setText(text)

    def onCheckedChanged_2(self, isChecked: bool):
        text = "开" if isChecked else "关"
        self.radioButton2.setText(text)

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

