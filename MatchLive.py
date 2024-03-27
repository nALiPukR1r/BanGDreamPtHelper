from ParaInput import Para
import math
import config
from DataValidation import scoreCheck

class MatchLive():

    # 本人分数基数
    __baseNum = 6500
    #对邦排名分数基数
    __rankingScore = [200,173,146,123,100]
    # 对邦自由可以获取pt
    # 自由基础分
    __basicSingleNum = 100
    # 自由分数基数
    __baseSingleNum = 9750
    # 因为自由和对邦都可以，展示的方案过多，默认开启精简方案
    # 开启后只显示：1.自由中的可行方案  2.对邦中可行且排名为1或5的的方案
    __easyMode = True
    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = None

    # 对邦下最低pt获取
    __ptMatchMin = __rankingScore[4] + config.SCORE_MIN_DEATH // __baseNum
    # 单人最低pt获取
    __ptMin = (__basicSingleNum + config.SCORE_MIN // __baseSingleNum )

    # 用户输入的参数（Para类）
    __usrPara = None

    def __init__(self,Para : Para,easyMode = True, auto = False, isMatch = False,ranking = 0):
        self.__easyMode = easyMode
        self.__usrPara = Para
        self.__autoPlan = auto
        # 优先对邦还是自由 --> false为自由
        self.isMatch = isMatch
        self.ranking = ranking

    def ScoreCal(self):
        self.result_list = []
        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()
        if self.__autoPlan:
            if self.isMatch:
                #print(True)
                flag = self.MatchCal(ptNeed, 1)
                if not flag:
                    flag = self.SingleCal(ptNeed, 1)
                if flag:
                    return True
                return False
            else:
                flag = self.SingleCal(ptNeed, 1)
                if not flag:
                    flag = self.MatchCal(ptNeed, 1)
                if flag:
                    return True
                return False

        index = 1
        # 两种方式可能都行
        index = self.SingleCal(ptNeed, index)
        self.MatchCal(ptNeed, index)
        return self.result_list

    def SingleCal(self,ptNeed,index):

        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            self.result_list.append(f"所需Pt为{ptNeed},低于自由打歌最低Pt = {self.__ptMin},故无法达成！")
            return self.result_list

        tag = True
        for fire, fireRate in self.__usrPara.getFire().items():
            score = ptNeed / fireRate - self.__basicSingleNum
            flag, temp = self.isAvailable(score, ptNeed, 0,fireRate)

            if flag:
                scoreFinal = int(temp * self.__baseSingleNum)

                if scoreCheck(scoreFinal,config.SCORE_MIN,config.SCORE_MATCH_MAX) == config.SCORE_TOO_LARGE:
                    if self.__easyMode:
                        continue
                    elif self.__autoPlan:
                        continue
                    else:
                        self.result_list.append(f"方案{index}的分数范围(自由)：{scoreFinal}~{scoreFinal + 449},"
                                                +f"使用火的数量为{fire}"+",该分数初步判断为数值过大，建议尝试其他配置\n")
                elif scoreCheck(scoreFinal,config.SCORE_MIN_DEATH,config.SCORE_MATCH_MAX) == config.SCORE_TOO_SMALL:
                    continue
                else:
                    if self.__autoPlan:
                        self.__plan = f"需要进行1次游戏,分数范围(自由)：{scoreFinal}~{scoreFinal + 449},使用火的数量为{fire},类型 - 自由,可获得PT = {self.ptGet_single(scoreFinal,fireRate)}"
                        return True
                    tag = False
                    self.result_list.append(f"方案{index}的分数范围(自由)：{scoreFinal}~{scoreFinal + 449},使用火的数量为{fire}")
                index = index  + 1

        if tag and not self.__autoPlan:
            self.result_list.append("自由打歌下，目标Pt数不可达！")
        elif tag and self.__autoPlan:
            return False

        return index

    def MatchCal(self,ptNeed,index):

        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            self.result_list.append(f"所需Pt为{ptNeed},低于对邦最低Pt = {self.__ptMatchMin},故无法达成！")
            return

        flag = True
        for fire, fireRate in self.__usrPara.getFire().items():
            # 在这里可以尝试不同的排名
            i = 1
            for item in self.__rankingScore:
                if self.__easyMode and i != 1 and i != 5:
                    i = i + 1
                    continue

                if self.__autoPlan and i != self.ranking:
                    i += 1
                    continue

                score = ptNeed / fireRate - item
                tag, temp = self.isAvailable(score, ptNeed, item,fireRate)
                if tag:
                    scoreFinal = int(temp * self.__baseNum)
                    str = f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 6499},需要为第{i}名,使用火的数量为{fire},类型 - 对邦."
                    if scoreCheck(scoreFinal, config.SCORE_MIN_DEATH,config.SCORE_MATCH_MAX) == config.SCORE_TOO_LARGE:
                        if self.__easyMode:
                            continue
                        elif self.__autoPlan:
                            continue
                        # print(str)
                        # print("该分数初步判断为数值过大，建议尝试其他配置\n")
                    elif scoreCheck(scoreFinal, config.SCORE_MIN_DEATH,config.SCORE_MATCH_MAX) == config.SCORE_TOO_SMALL:
                        continue
                    else:
                        if self.__autoPlan:
                            self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 6499},需要为第{i}名,使用火的数量为{fire},类型 - 对邦."
                            return True
                        flag = False
                        self.result_list.append(str)
                    index = index + 1

                i = i + 1
        if flag and not self.__autoPlan:
            self.result_list.append("对邦游戏下，目标Pt数不可达！")
        elif flag and self.__autoPlan:
            return False

    def isAvailable(self,score,ptNeed,rankingScore,fireRate):

        if score == int(score):
            return True,score
        elif ptNeed == (math.floor(score) + rankingScore) * fireRate:
            return True,math.floor(score)
        elif ptNeed == (math.ceil(score) + rankingScore) * fireRate:
            return True,math.ceil(score)

        return False,0
    def ptGet_Match(self,score, fireRate,ranking):
        return (score // self.__baseNum + self.__rankingScore[ranking]) * fireRate

    def ptGet_single(self,score, fireRate):
        return (score // self.__baseSingleNum + self.__basicSingleNum) * fireRate

    def scoreToPt_Single(self, score, fireRate):
        if self.isMatch:
            return (score // self.__baseNum + self.__rankingScore[self.ranking]) * fireRate
        else:
            return (score // self.__baseSingleNum + self.__basicSingleNum) * fireRate

    def getPtMin(self):
        return self.__ptMin

    def getBaseFree(self):
        return self.__baseSingleNum

    def getPlan(self):
        return self.__plan

    def scoreInterval(self,score):
        temp = score / self.__baseSingleNum
        floor = math.floor(temp)
        up = math.floor(temp+1)

        scoreLower = floor * self.__baseSingleNum
        scoreUpper = up * self.__baseSingleNum
        return f"分数区间为{scoreLower}~{scoreUpper-1}"

    def setPara(self,para):
        self.__usrPara = para

    def setUpRate(self,up):
        pass


# p = Para(19600,0)
# mtl = MatchLive(p)
# mtl.ScoreCal()