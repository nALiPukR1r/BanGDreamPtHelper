import math
from ParaInput import Para
import config
from DataValidation import scoreCheck

class ExLive():
    # 基础得分
    __basicScore = 130
    # 本人分数基数
    __baseNum = 26000
    # 他人得分基数
    __baseNumOthers = 260000
    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = ""

    # 加成倍率
    __upRate = 1.0
    # 其他人分数
    __othersScore = 0
    # 单人/协力最低pt获取
    __ptMin = int((__basicScore + config.SCORE_MIN_DEATH // __baseNum + 0) * 1 * 1)

    # 用户输入的参数（Para类）
    __usrPara = None

    def __init__(self, Para: Para, upRate, othersScore,auto = False):
        self.__upRate += upRate / 100
        self.__upRate = round(self.__upRate, 2)
        self.__othersScore = othersScore
        self.__usrPara = Para
        self.__autoPlan = auto

    def ScoreCal(self):
        result_list = []

        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()

        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            result_list.append(f"所需Pt为{ptNeed},低于最低Pt = {self.__ptMin},故无法达成！")
            return result_list

        othersNum = self.__othersScore // self.__baseNumOthers

        index = 1
        flag = True

        for fire, fireRate in self.__usrPara.getFire().items():
            rangeLower = (ptNeed // fireRate )
            rangeUpper = rangeLower + 1

            # 这里的uprate是1.0以上的
            # 一把计算就是构造时赋值，而自动计算在最后两段会调用set方法重新赋值
            uprate = self.__upRate
            while uprate < config.UP_RATE_MAX :
                scoreLower = (rangeLower) / uprate - othersNum - self.__basicScore
                scoreLower = math.ceil(scoreLower)

                scoreUpper = (rangeUpper) / uprate - othersNum - self.__basicScore
                scoreUpper = math.ceil(scoreUpper - 1)
                scoreFinal = scoreLower * self.__baseNum
                if scoreLower == scoreUpper and self.doubleCheck(scoreFinal,ptNeed,uprate,fireRate):

                    if scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_EX_MAX) == config.SCORE_TOO_LARGE:
                        result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 25999},使用火的数量为{fire}"+
                                           f",加成倍率为{int((uprate)*100)-100}%,该分数初步判断为数值过大，建议尝试其他配置.")
                    elif scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_EX_MAX) == config.SCORE_TOO_SMALL:
                        pass
                    else:
                        flag = False
                        result_list.append(
                            f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 25999},使用火的数量为{fire},加成倍率为{int((uprate)*100)-100}%.")
                        if self.__autoPlan:
                            self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 25999},使用火的数量为{fire},加成倍率为{int((uprate)*100)-100}%,可获得PT = {self.ptGet(scoreFinal,uprate,fireRate)}."
                            return True

                    index = index + 1

                if not self.__autoPlan:
                    break
                uprate += 0.1
                uprate = round(uprate, 1)

        if flag and not self.__autoPlan:
            result_list.append(f"目标Pt数不可达！")
        elif flag and self.__autoPlan:
            return False

        return result_list

    def setUpRate(self,upRate):
        self.__upRate = upRate / 100 + 1.0

    def scoreToPt_Single(self, score, fireRate):
        return int(math.floor((score // self.__baseNum + self.__basicScore + 0)* self.__upRate) * fireRate)

    def getPtMin(self):
        return self.__ptMin

    def getBaseFree(self):
        return self.__baseNum

    def getPlan(self):
        return self.__plan

    def scoreInterval(self,score):
        temp = score / self.__baseNum
        floor = math.floor(temp)
        up = math.floor(temp+1)

        scoreLower = floor * self.__baseNum
        scoreUpper = up * self.__baseNum
        return f"分数区间为{scoreLower}~{scoreUpper-1}"

    def setPara(self,para):
        self.__usrPara = para
    def ptGet(self,score,uprate,fireRate):
        return math.floor((score // self.__baseNum + self.__basicScore) * uprate) * fireRate
    def doubleCheck(self,score,ptNeed,uprate,fireRate):
        #print(f"{ptNeed},{math.floor((score // self.__baseTeamNum + self.__basicTeamScore) * uprate )* fireRate}")
        return ptNeed == math.floor((score // self.__baseNum + self.__basicScore) * uprate) * fireRate


# p = Para(3000000,2998615)
# el = ExLive(p,70,0)
# el.ScoreCal()