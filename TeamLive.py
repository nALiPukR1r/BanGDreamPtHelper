from ParaInput import Para
import math
import config
from DataValidation import scoreCheck

class TeamLive():
    #赢队125，输队0
    __bonusScore = 0
    # 本人分数基数
    __baseNum = 6500
    #团队贡献分数
    __teamContribute = [125,117,110,105,100]
    #额外分数（固定）
    __extraNum = 50
    # 5v5的方案过多，该选项为True则只展示最简单的（队伍贡献为第五和第一）的方案
    __easyMode = True
    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = None

    # 单人最低pt获取
    __ptMin = __bonusScore + __teamContribute[4] + config.SCORE_MIN_DEATH // __baseNum

    # 用户输入的参数（Para类）
    __usrPara = None

    def __init__(self,Para : Para,isWin, easyMode = True,auto = False, contri = 0):
        self.__easyMode = easyMode
        self.__usrPara = Para
        self.__autoPlan = auto
        if isWin:
            self.__bonusScore = 125
        self.contri = contri
        self.winloss = "胜利" if isWin else "失败"

    def ScoreCal(self):
        result_list = []
        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()
        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            result_list.append(f"所需Pt为{ptNeed},低于最低Pt = {self.__ptMin},故无法达成！")
            return result_list

        index = 1
        flag = True
        for fire, fireRate in self.__usrPara.getFire().items():

            score = ptNeed / fireRate - self.__extraNum
            #在这里可以尝试不同的队伍内贡献，对于输赢则optional（很难控制）
            i = 1
            for item in self.__teamContribute:

                if self.__easyMode and (i != 5 and i!=1):
                    i = i + 1
                    continue
                if self.__autoPlan and i != self.contri:
                    i += 1
                    continue
                #print(i)
                tag,temp = self.isAvailable(score - item - self.__bonusScore, ptNeed, item,fireRate)
                if tag:

                    scoreFinal = int(temp * self.__baseNum)
                    str = f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 6499},需要达成在队内为第{i}名,使用火的数量为{fire},队伍的成绩为{self.winloss}"
                    if scoreCheck(scoreFinal, config.SCORE_MIN_DEATH,config.SCORE_TEAM_MAX) == config.SCORE_TOO_LARGE:
                        result_list.append(str+",该分数初步判断为数值过大，建议尝试其他配置")
                    elif scoreCheck(scoreFinal, config.SCORE_MIN_DEATH,config.SCORE_TEAM_MAX) == config.SCORE_TOO_SMALL:
                        continue
                        # print(str + " --- 该分数初步判断为数值过小，建议尝试其他配置(降低火数/换更差的卡组)")
                    else:
                        if self.__autoPlan:
                            self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 6499},需要达成在队内为第{i}名,使用火的数量为{fire},队伍成绩为{self.winloss},可获得PT = {self.ptGet(scoreFinal,fireRate,i-1)}."
                        result_list.append(str)
                        flag = False
                    index = index + 1
                i = i + 1
        if flag and not self.__autoPlan:
            result_list.append("目标Pt数不可达！")
        elif flag and self.__autoPlan:
            return False
        elif not flag and self.__autoPlan:
            return True

        return result_list
    def ptGet(self,score,fireRate,ranking):
        return fireRate * (score // self.__baseNum + self.__extraNum +
                           self.__bonusScore + self.__teamContribute[ranking])
    def isAvailable(self,score,ptNeed,teamContri,fireRate):

        if score == int(score):
            return True,score
        elif ptNeed == (math.floor(score) + self.__extraNum + self.__bonusScore + teamContri) * fireRate:
            return True,math.floor(score)
        elif ptNeed == (math.ceil(score) + self.__extraNum + self.__bonusScore + teamContri) * fireRate:
            return True,math.ceil(score)

        return False,0

    def scoreToPt_Single(self, score, fireRate):
        return fireRate * (score // self.__baseNum + self.__extraNum +
                           self.__bonusScore + self.__teamContribute[self.contri])

    def scoreInterval(self,score):
        temp = score / self.__baseNum
        floor = math.floor(temp)
        up = math.ceil(temp)

        scoreLower = floor * self.__baseNum
        scoreUpper = up * self.__baseNum
        return f"分数区间为{scoreLower}~{scoreUpper-1}"

    def setPara(self,para):
        self.__usrPara = para
    def getPlan(self):
        return self.__plan
    def getPtMin(self):
        return self.__ptMin
    def setUpRate(self,up):
        pass

# p = Para(1145140,1140020)
# tl = TeamLive(p,False,True)
# tl.ScoreCal()