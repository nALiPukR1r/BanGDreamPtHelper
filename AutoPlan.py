import math

import config
from ParaInput import Para
from MatchLive import MatchLive
from MissionLive import MissionLive
from CpLive import CpLive
from MedleyLive import MedleyLive
from TeamLive import TeamLive
from ExLive import ExLive

class autoPlan():
    __liveType = None
    __ptNeed = 0
    __usrScoreMax = 0
    __usrScoreAvg = 0
    __ptPerGame = 0
    __usrPara = None
    __finalStep_1 = None
    __finalStep_2 = None
    __fireList = []

    __avgStep = None

    def __init__(self, para, avg,type,upRate = 0,isCP = False,songNum = 3, isMatch = False,isWin = False, ranking = 5,supportband = 0):
        self.__usrPara = para
        self.__usrScoreAvg = avg
        self.__liveType = type
        self.__ptNeed = para.getTarget() - para.getCurrent()
        self.songNum = songNum
        self.isWin = isWin
        self.ranking = ranking
        self.upRate = upRate
        self.isCP = isCP
        self.supportband = supportband
        self.isMatch = isMatch

    def auto(self):
        self.__fireList = []
        liveClass = self.typeClassConstruct(self.__usrPara,True)
        if self.__liveType == config.TYPE_MEDLEY_LIVE:
            liveClass.setFlag(True)

        if self.isCP:
            liveClass.setIsCp(True)
            liveClass.setCP(200)

        self.__ptPerGame = liveClass.scoreToPt_Single(self.__usrScoreAvg,1)

        flag = True

        gameNum = self.__ptNeed / self.__ptPerGame
        if gameNum < 0 :
            self.__fireList.append("暂无推荐路径!")
            return self.__fireList
        if gameNum == int(gameNum) and gameNum > 0:
            str = liveClass.scoreInterval(self.__usrScoreAvg)
            flag = False
            if self.__liveType == config.TYPE_MEDLEY_LIVE:
                stepList = self.gameTimesMedley(int(gameNum))
                for fire, times in stepList.items():
                    self.splitGameTextMedley(fire, times,str)
            else:
                if self.isCP:
                    stepList = self.gameTimes_CP(int(gameNum))
                else:
                    stepList = self.gameTimes(int(gameNum))
                for fire, times in stepList.items():
                    self.splitGameText(fire,times,str)

        gameNum = math.floor(gameNum)
        ptLeft = self.__ptNeed - gameNum * self.__ptPerGame
        if flag:
            p = Para(ptLeft, 0)
            if self.__liveType == config.TYPE_MEDLEY_LIVE:
                liveClass.setFlag(False)
            liveClass.setPara(p)
            liveClass.setUpRate(0)
            if self.isCP:
                liveClass.setIsCp(False)
            if liveClass.ScoreCal():
                str = liveClass.scoreInterval(self.__usrScoreAvg)
                flag = False
                if self.__liveType == config.TYPE_MEDLEY_LIVE:
                    stepList = self.gameTimesMedley(gameNum)
                    for fire, times in stepList.items():
                        self.splitGameTextMedley(fire, times,str)
                else:
                    if self.isCP:
                        stepList = self.gameTimes_CP(int(gameNum))
                    else:
                        stepList = self.gameTimes(int(gameNum))
                    for fire, times in stepList.items():
                        self.splitGameText(fire, times, str)
                self.__finalStep_1 = liveClass.getPlan()

        if flag:
            if gameNum != 0:
                gameNum -= 1
                ptLeft += self.__ptPerGame

            p = Para(ptLeft,0)
            liveClass.setPara(p)
            liveClass.setUpRate(0)
            if liveClass.ScoreCal():
                flag = False
                str = liveClass.scoreInterval(self.__usrScoreAvg)
                if self.__liveType == config.TYPE_MEDLEY_LIVE:
                    stepList = self.gameTimesMedley(gameNum)
                    for fire, times in stepList.items():
                        self.splitGameTextMedley(fire, times, str)
                else:
                    if self.isCP:
                        stepList = self.gameTimes_CP(int(gameNum))
                    else:
                        stepList = self.gameTimes(int(gameNum))
                    for fire, times in stepList.items():
                        self.splitGameText(fire, times, str)
                self.__finalStep_1 = liveClass.getPlan()

            ptLeftSmall = liveClass.getPtMin()
            ptLeftLarge = ptLeft - ptLeftSmall
            print(ptLeftLarge)
            print(ptLeftSmall)

            step = 1
            while flag:
                p = Para(ptLeftLarge,0)
                liveClass.setPara(p)
                liveClass.setUpRate(0)
                if liveClass.ScoreCal():
                    flag = False
                    str = liveClass.scoreInterval(self.__usrScoreAvg)
                    if self.__liveType == config.TYPE_MEDLEY_LIVE:
                        stepList = self.gameTimesMedley(gameNum)
                        for fire, times in stepList.items():
                            self.splitGameTextMedley(fire, times,str)
                    else:
                        if self.isCP:
                            stepList = self.gameTimes_CP(int(gameNum))
                        else:
                            stepList = self.gameTimes(int(gameNum))
                        for fire, times in stepList.items():
                            self.splitGameText(fire, times, str)
                    self.__finalStep_1 = liveClass.getPlan()
                    p = Para(ptLeftSmall,0)
                    liveClass.setPara(p)
                    liveClass.ScoreCal()
                    self.__finalStep_2 = liveClass.getPlan()

                ptLeftLarge -= 1
                ptLeftSmall += 1

                if ptLeftLarge <= 0 or step >= config.STEP_MAX:
                    break
        if flag:
            self.__fireList.append("暂无推荐路径!")
        else:
            self.__fireList.reverse()
            self.__fireList.insert(0,f"每次游戏可以获得的PT：{self.__ptPerGame}")
            self.__fireList.insert(1,f"目标PT = {self.__usrPara.getTarget()}, 目前PT = {self.__usrPara.getCurrent()}, 所需PT = {self.__ptNeed}")
            self.__fireList.insert(2,f"期望分数 = {self.__usrScoreAvg}")
            self.__fireList.insert(3,"推荐方案：")
            if self.__finalStep_1 != None:
                self.__fireList.append(self.__finalStep_1)
            if self.__finalStep_2 != None:
                self.__fireList.append(self.__finalStep_2)
        # print(self.__finalStep)
        # for index,item in enumerate(self.__fireList):
        #     print(item)
        return self.__fireList

    def typeClassConstruct(self, para, auto):
        if self.__liveType == config.TYPE_MISSION_LIVE:
            return MissionLive(para,self.upRate,0,self.supportband,auto)
        elif self.__liveType == config.TYPE_CP_LIVE:
            return CpLive(para,self.upRate,0,False,auto)
        elif self.__liveType == config.TYPE_EX_LIVE:
            return ExLive(para,self.upRate,0,auto)
        elif self.__liveType == config.TYPE_TEAM_LIVE:
            return TeamLive(para,self.isWin,True,auto,self.ranking - 1)
        elif self.__liveType == config.TYPE_MEDLEY_LIVE:
            return MedleyLive(para,auto,self.songNum)
        elif self.__liveType == config.TYPE_MATCH_LIVE:
            return MatchLive(para,True,auto,self.isMatch,self.ranking - 1)

    def gameTimes(self, times):

        fire = {0:1,1:5,2:10,3:15}
        temp = {0:0,1:0,2:0,3:0}
        i = 3
        while times != 0:
            x = times // fire.get(i)
            times -= x * fire.get(i)
            temp[i] = x
            i -= 1

        return temp

    def gameTimes_CP(self,times):
        cprate = [1,2,4]
        i = 2
        temp = {200: 0, 400: 0, 800: 0}
        while times != 0:
            x = times // cprate[i]
            times -= x * cprate[i]
            temp[cprate[i]*200] = x
            i -= 1
        return temp


    def gameTimesMedley(self, times):

        fire = {
        0:1,
        1:5,
        2:10,
        3:15,
        4:20,
        5:25,
        6:30,
        7:35,
        8:40,
        9:45
    }
        temp = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        i = 9
        while times != 0:
            x = times // fire.get(i)
            times -= x * fire.get(i)
            temp[i] = x
            i -= 1

        return temp

    def splitGameText(self,fire,times,str):
        if times != 0:
            if self.__liveType == config.TYPE_MISSION_LIVE:
                self.__fireList.append(
                    f"需要进行{times}次游戏," + str + f",消耗的火为{fire},加成倍率为{self.upRate}%,可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")
            elif self.__liveType == config.TYPE_CP_LIVE:
                if self.isCP:
                    self.__fireList.append(
                        f"需要进行{times}次游戏," + str + f",CP消耗为{fire}可获得PT = {self.__ptPerGame * fire // 200 * times}.")
                else:
                    self.__fireList.append(
                        f"需要进行{times}次游戏," + str + f",消耗的火为{fire},加成倍率为{self.upRate}%,可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")
            elif self.__liveType == config.TYPE_EX_LIVE:
                self.__fireList.append(
                    f"需要进行{times}次游戏," + str + f",消耗的火为{fire},加成倍率为{self.upRate}%,可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")
            elif self.__liveType == config.TYPE_TEAM_LIVE:
                str1 = "胜利" if self.isWin else "失败"
                self.__fireList.append(
                    f"需要进行{times}次游戏," + str + f",消耗的火为{fire},队伍成绩为{str1},队内排名为{self.ranking},可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")
            elif self.__liveType == config.TYPE_MATCH_LIVE:
                if self.isMatch:
                    self.__fireList.append(
                        f"需要进行{times}次游戏," + str + f",消耗的火为{fire},需要为第{self.ranking}名,游戏类型为 - 对邦,可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")
                else:
                    self.__fireList.append(
                        f"需要进行{times}次游戏," + str + f",消耗的火为{fire},游戏类型为 - 自由,可获得PT = {self.__ptPerGame * config.fire[fire] * times}.")

    def splitGameTextMedley(self,fire,times,str1):
        str3 = f",可获得PT = {self.__ptPerGame * config.fireMedley[fire] * times}"
        str2 = f",完成的曲数为{self.songNum}"+str3
        if fire == 0 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 1 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏," + str1 + f"消耗的火为{fire}" + str2)
        elif fire == 2 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏," + str1 + f"消耗的火为{fire}" + str2)
        elif fire == 3 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏," + str1 + f"消耗的火为{fire}" + str2)
        elif fire == 4 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 5 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 6 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 7 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 8 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)
        elif fire == 9 and times != 0:
            self.__fireList.append(f"需要进行{times}次游戏,"+str1+f"消耗的火为{fire}"+str2)


# p = Para(9999,0)
# ap = autoPlan(p,2500000,config.TYPE_MISSION_LIVE,100,False,3,False,5,282000)
# ap.auto()