from ParaInput import Para
import math
import config
from DataValidation import scoreCheck

class CpLive():
    # 协力基础得分
    __basicTeamScore = 70
    # 单人清cp基数得分
    __basicSingleScore = 3250
    # 本人分数基数
    __baseTeamNum = 50000
    # 本人清cp分数基数
    __baseSingleNum = 450
    # 他人得分基数
    __baseNumOthers = 500000
    #打cp还是协力
    __isCP = False
    # 清CP最低pt获取(因为不能打0分，所以?)
    __ptCpMin = __basicSingleScore + config.SCORE_MIN // __baseSingleNum
    # 单人/协力最低pt获取
    __ptMin = (__basicTeamScore + config.SCORE_MIN_DEATH// __baseTeamNum + 0) * 1 * 1
    # CP倍率
    __cpRate = [1,2,4]
    # 自动规划时指定cp
    __autoCP = 200

    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = ""

    # 加成倍率
    __upRate = 1.0
    # 其他人分数
    __othersScore = 0

    # 用户输入的参数（Para类）
    __usrPara = None

    def __init__(self, Para : Para, upRate, othersScore, isCP : bool ,auto = False,autoCP = 200):
        self.__usrPara = Para
        self.__upRate += upRate / 100
        self.__upRate = round(self.__upRate,2)
        # print(self.__upRate)
        self.__othersScore = othersScore
        self.__isCP = isCP
        self.__autoCP = autoCP
        self.__autoPlan = auto


    def ScoreCal(self):
        self.result_list = []
        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()

        if self.__isCP:
            if ptNeed < self.__ptCpMin:
                if self.__autoPlan:
                    return False
                self.result_list.append(f"所需Pt为{ptNeed},低于CP消耗下的最低Pt = {self.__ptCpMin},故无法达成！")
                return self.result_list
            res = self.cpCal(ptNeed)
            if self.__autoPlan:
                return res
            else:
                return self.result_list
        else:
            if ptNeed < self.__ptMin:
                if self.__autoPlan:
                    return False
                self.result_list.append(f"所需Pt为{ptNeed},低于最低Pt = {self.__ptMin},故无法达成！")
                return self.result_list
            res = self.normalCal(ptNeed)
            if self.__autoPlan:
                return res
            else:
                return self.result_list

    def cpCal(self,ptNeed):
        tag = True

        if self.__autoPlan:
            cprate = self.__autoCP
            score = ptNeed / cprate - self.__basicSingleScore

            flag, temp = self.isAvailable(score, ptNeed, cprate)

            if flag:
                scoreFinal = int(temp * self.__baseSingleNum)

                if scoreCheck(scoreFinal, config.SCORE_MIN,config.SCORE_CP_MAX) == config.SCORE_TOO_LARGE:
                    self.result_list.append(
                        f"分数范围(清CP)：{scoreFinal}~{scoreFinal + 449},消耗的CP数为{cprate * 200}" +
                        ",该分数初步判断为数值过大，建议尝试其他配置")
                elif scoreCheck(scoreFinal, config.SCORE_MIN,config.SCORE_CP_MAX) == config.SCORE_TOO_SMALL:
                    pass
                else:
                    self.__plan = f"需要进行1次游戏,分数范围(清CP)：{scoreFinal}~{scoreFinal + 449},消耗的CP数为{cprate * 200},可获得PT = {self.ptGet(scoreFinal,0,0,cprate)}"
                    return True
            return False
        else:
            for cprate in self.__cpRate:
                score = ptNeed / cprate - self.__basicSingleScore

                flag, temp = self.isAvailable(score,ptNeed,cprate)

                if flag:
                    scoreFinal = int(temp * self.__baseSingleNum)

                    if scoreCheck(scoreFinal,config.SCORE_MIN,config.SCORE_CP_MAX) == config.SCORE_TOO_LARGE:
                        self.result_list.append(f"分数范围(清CP)：{scoreFinal}~{scoreFinal + 449},消耗的CP数为{cprate * 200}"+
                                                ",该分数初步判断为数值过大，建议尝试其他配置")
                    elif scoreCheck(scoreFinal,config.SCORE_MIN,config.SCORE_CP_MAX) == config.SCORE_TOO_SMALL:
                        continue
                    else:
                        tag = False
                        self.result_list.append(f"分数范围(清CP)：{scoreFinal}~{scoreFinal + 449},消耗的CP数为{cprate * 200}")
            if tag:
                self.result_list.append("目标Pt数不可达！")

            return self.result_list

    def normalCal(self,ptNeed):

        othersNum = self.__othersScore // self.__baseNumOthers

        index = 1
        flag = True
        for fire,fireRate in self.__usrPara.getFire().items():
            # 这里会决定第一个范围，即[取整，取整+1)
            rangeLower = ptNeed // fireRate
            rangeUpper = rangeLower + 1

            # print(rangeLower,rangeUpper)
            # 这里的uprate是1.0以上的
            # 一把计算就是构造时赋值，而自动计算在最后两段会调用set方法重新赋值
            uprate = self.__upRate
            while uprate < config.UP_RATE_MAX :
                # print(uprate)
                # 这里决定第二个范围
                scoreLower = (rangeLower) / uprate - othersNum - self.__basicTeamScore
                scoreLower = math.ceil(scoreLower)

                scoreUpper = (rangeUpper) / uprate - othersNum - self.__basicTeamScore
                scoreUpper = math.ceil(scoreUpper - 1)
                scoreFinal = scoreLower * self.__baseTeamNum
                if scoreLower == scoreUpper and self.doubleCheck(scoreFinal,ptNeed,uprate,fireRate):
                    if scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_CP_MAX) == config.SCORE_TOO_LARGE:
                        self.result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 49999},使用火的数量为{fire}"+
                                    f",加成倍率为{int((uprate)*100)-100}%,该分数初步判断为数值过大，建议尝试其他配置")
                    elif scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_CP_MAX) == config.SCORE_TOO_SMALL:
                        pass
                    else:
                        flag = False
                        if self.__autoPlan:
                            self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 49999},使用火的数量为{fire},加成倍率为{int((uprate)*100)- 100}%,可获得PT = {self.ptGet(scoreFinal,uprate,fireRate,0)}."
                            return True
                        self.result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 49999},使用火的数量为{fire},加成倍率为{int((uprate)*100)-100}%.")

                    index = index + 1
                if not self.__autoPlan:
                    break
                uprate += 0.1
                uprate = round(uprate,2)
                # print(uprate)

        if flag and not self.__autoPlan:
            self.result_list.append(f"目标Pt数不可达！")
            return self.result_list
        elif flag and self.__autoPlan:
            return False
    def ptGet(self, score, uprate, fireRate,cprate):
        if not self.__isCP:
            return math.floor((score // self.__baseTeamNum + self.__basicTeamScore) * uprate) * fireRate
        else:
            return (math.floor(score) + self.__basicSingleScore ) * cprate


    def isAvailable(self, score, ptNeed, cprate):

        if score == int(score):
            return True,score
        elif ptNeed == (math.floor(score) + self.__basicSingleScore ) * cprate:
            return True,math.floor(score)
        elif ptNeed == (math.ceil(score) + self.__basicSingleScore ) * cprate:
            return True,math.ceil(score)

        return False,0

    def setUpRate(self,upRate):
        self.__upRate = upRate / 100 + 1.0

    def setIsCp(self,isCP:bool):
        self.__isCP = isCP

    def scoreToPt_Single(self, score, fireRate):
        if self.__isCP:
            print(score)
            print(self.__autoCP)
            return int((score // self.__baseSingleNum+ self.__basicSingleScore + 0)* self.__autoCP)
        else:
            return int(math.floor((score // self.__baseTeamNum+ self.__basicTeamScore + 0)* self.__upRate) * fireRate)

    def getPtMin(self):
        return self.__ptMin

    # def getBaseFree(self):
    #     return self.__baseNum

    def getPlan(self):
        return self.__plan

    def setCP(self,cp):
        self.__autoCP = cp // 200

    def scoreInterval(self,score):
        if self.__isCP:
            temp = score / self.__baseSingleNum
            floor = math.floor(temp)
            up = math.floor(temp+1)

            scoreLower = floor * self.__baseSingleNum
            scoreUpper = up * self.__baseSingleNum
        else:
            temp = score / self.__baseTeamNum
            floor = math.floor(temp)
            up = math.floor(temp+1)

            scoreLower = floor * self.__baseTeamNum
            scoreUpper = up * self.__baseTeamNum
        return f"分数区间为{scoreLower}~{scoreUpper-1}"

    def setPara(self,para):
        self.__usrPara = para

    def doubleCheck(self,score,ptNeed,uprate,fireRate):
        #print(f"{ptNeed},{math.floor((score // self.__baseTeamNum + self.__basicTeamScore) * uprate )* fireRate}")
        return ptNeed == math.floor((score // self.__baseTeamNum + self.__basicTeamScore) * uprate) * fireRate

# p = Para(10881,0)
# cl = CpLive(p,10,170,False,0)
# cl.ScoreCal()