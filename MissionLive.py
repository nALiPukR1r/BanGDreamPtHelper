from ParaInput import Para
import math
import config
from DataValidation import scoreCheck

class MissionLive():

    #基础得分
    __basicScore = 120
    #本人分数基数
    __baseNum = 15000
    #他人得分基数
    __baseNumOthers = 150000
    #支援乐队综合力基数
    __baseNumSupport = 3000
    # 单人/协力最低pt获取
    __ptMin = 0

    #加成倍率
    __upRate = 1.0
    #其他人分数
    __othersScore = 0

    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = ""

    supportNum = 0

    #用户输入的参数（Para类）
    __usrPara = None

    def __init__(self,Para : Para,upRate,othersScore,supportBand,auto = False):
        self.__usrPara = Para
        self.__upRate += upRate / 100
        self.__upRate = round(self.__upRate,2)
        self.__othersScore = othersScore
        self.__autoPlan = auto
        self.supportNum = supportBand // self.__baseNumSupport
        self.__ptMin = ((self.__basicScore + config.SCORE_MIN_DEATH // self.__baseNum + 0) * 1
                        + self.supportNum)

    def ScoreCal(self):
        result_list = []
        othersNum = self.__othersScore // self.__baseNumOthers
        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()
        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            result_list.append(f"所需Pt = {ptNeed},低于可获取的最低Pt = {self.__ptMin},故无法达成！")
            return result_list


        index = 1
        flag = True
        for fire,fireRate in self.__usrPara.getFire().items():
            # 这里会决定第一个范围，即[取整，取整+1)
            rangeLower = (ptNeed // fireRate - self.supportNum)
            rangeUpper = rangeLower + 1

            #print(rangeLower,rangeUpper)
            uprate = self.__upRate
            while uprate < config.UP_RATE_MAX:
                #这里决定第二个范围
                scoreLower = (rangeLower) / self.__upRate - othersNum - self.__basicScore
                scoreLower = math.ceil(scoreLower)

                scoreUpper = (rangeUpper) / self.__upRate - othersNum - self.__basicScore
                scoreUpper = math.ceil(scoreUpper - 1)

                scoreFinal = scoreLower * self.__baseNum
                if scoreLower == scoreUpper and self.doubleCheck(scoreFinal,ptNeed,uprate,fireRate):
                    if scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_MISSION_MAX) == config.SCORE_TOO_LARGE:
                        s1 = f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 14999},使用火的数量为{fire}"
                        s2 = "该分数初步判断为数值过大，建议尝试其他配置(加成倍率)\n"
                        result_list.append(s1+s2)
                    elif scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_MISSION_MAX) == config.SCORE_TOO_SMALL:
                        #print("该分数初步判断为数值过小，建议尝试其他配置(加成倍率)\n")
                        pass
                    else:
                        result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 14999},使用火的数量为{fire}\n")
                        flag = False
                        if self.__autoPlan:
                            self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 14999},使用火的数量为{fire},加成倍率为{int((uprate)*100)-100}%,可获得PT = {self.ptGet(scoreFinal,uprate,fireRate)}"
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

    def ptGet(self, score, uprate, fireRate):
        # print(f"{ptNeed},{score},{uprate},{fireRate},{self.supportNum},{math.floor((score // self.__baseNum + self.__basicScore) * uprate )* fireRate}")
        return (math.floor((score // self.__baseNum + self.__basicScore) * uprate) + self.supportNum )* fireRate

    def scoreToPt_Single(self, score, fireRate):
        return int((math.floor((score // self.__baseNum + self.__basicScore + 0)* self.__upRate)+ self.supportNum) * fireRate)

    def getPtMin(self):
        return self.__ptMin

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

    def doubleCheck(self,score,ptNeed,uprate,fireRate):
        #print(f"{ptNeed},{score},{uprate},{fireRate},{self.supportNum},{math.floor((score // self.__baseNum + self.__basicScore) * uprate )* fireRate}")
        return ptNeed == (math.floor((score // self.__baseNum + self.__basicScore) * uprate) + self.supportNum) * fireRate

# p = Para(1413,1133)
# ml = MissionLive(p,0,0,282000)
# ml.ScoreCal()