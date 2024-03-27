from ParaInput import Para
import math
import config
from DataValidation import scoreCheck

class MedleyLive():
    # 基础得分
    __basicScore = [30,65,100]
    # 本人分数基数
    __baseNum = 18500
    #歌曲数目
    __songNum = 0
    # 自动规划路径时不做中途输出
    __autoPlan = False
    # 为了自动规划获取详细方案准备的
    __plan = ""
    flag = True

    # 单人最低pt获取
    __ptMin = __basicScore[0]  + config.SCORE_MIN_MEDLEY // __baseNum

    # 用户输入的参数（Para类）
    __usrPara = None

    def __init__(self,Para : Para,auto = False,songNum = 3):
        self.__usrPara = Para
        self.__autoPlan = auto
        self.__songNum = songNum

    def ScoreCal(self):
        result_list = []

        ptNeed = self.__usrPara.getTarget() - self.__usrPara.getCurrent()
        if ptNeed < self.__ptMin:
            if self.__autoPlan:
                return False
            result_list.append(f"所需Pt为{ptNeed},低于最低Pt = {self.__ptMin},故无法达成！")
            return result_list
        index = 1
        tag = True

        if self.__autoPlan and self.flag:
            basic = self.__basicScore[self.__songNum - 1]
            for fire, fireRate in self.__usrPara.getMedleyFire().items():
                score = ptNeed / fireRate - basic
                flag = False
                if score == int(score):
                    flag = True
                elif ptNeed == (math.floor(score) + basic) * fireRate:
                    flag = True
                elif ptNeed == (math.ceil(score) + basic) * fireRate:
                    flag = True

                if flag:
                    scoreFinal = int(score*self.__baseNum)
                    if scoreCheck(scoreFinal,config.SCORE_MIN_MEDLEY,config.SCORE_MEDLEY_MAX * self.__songNum) == config.SCORE_TOO_LARGE:
                        # result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 18499},使用火的数量为{fire}"+
                        #                    f",完成歌曲数为{song+1},该分数初步判断为数值过大，建议尝试其他配置")
                        continue
                    elif scoreCheck(scoreFinal,config.SCORE_MIN_MEDLEY,config.SCORE_MEDLEY_MAX) == config.SCORE_TOO_SMALL:
                        continue
                    else:
                        self.__plan = f"分数范围：{scoreFinal}~{scoreFinal + 18499},使用火的数量为{fire},完成歌曲数为{self.__songNum},可获得PT = {self.ptGet(scoreFinal,fireRate,self.__songNum)}"
                        return True
        else:
            for song,basic in enumerate(self.__basicScore):
            #basic = self.__basicScore[self.__songNum - 1]
                for fire, fireRate in self.__usrPara.getMedleyFire().items():
                    score = ptNeed / fireRate - basic
                    flag = False
                    if score == int(score):
                        flag = True
                    elif ptNeed == (math.floor(score) + basic) * fireRate:
                        flag = True
                    elif ptNeed == (math.ceil(score) + basic) * fireRate:
                        flag = True

                    if flag:
                        scoreFinal = int(score*self.__baseNum)
                        if scoreCheck(scoreFinal,config.SCORE_MIN_MEDLEY,config.SCORE_MEDLEY_MAX * (song+1)) == config.SCORE_TOO_LARGE:
                            # result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 18499},使用火的数量为{fire}"+
                            #                    f",完成歌曲数为{song+1},该分数初步判断为数值过大，建议尝试其他配置")

                            continue
                        elif scoreCheck(scoreFinal,config.SCORE_MIN_MEDLEY,config.SCORE_MEDLEY_MAX) == config.SCORE_TOO_SMALL:
                            continue
                        else:
                            if self.__autoPlan:
                                self.__plan = f"需要进行1次游戏,分数范围：{scoreFinal}~{scoreFinal + 18499},使用火的数量为{fire},完成歌曲数为{song+1},可获得PT = {self.ptGet(scoreFinal,fireRate,song+1)}"
                                return True
                            result_list.append(f"方案{index}的分数范围：{scoreFinal}~{scoreFinal + 18499},使用火的数量为{fire},完成歌曲数为{song+1}")
                            tag = False

                            index = index + 1

        if tag and not self.__autoPlan:
            result_list.append(f"目标Pt数不可达！")
        elif tag and self.__autoPlan:
            return False

        return result_list

    def scoreToPt_Single(self, score, fireRate):
        return (score // self.__baseNum + self.__basicScore[self.__songNum - 1]) * fireRate

    def ptGet(self,score,fireRate,song):
        return (score // self.__baseNum + self.__basicScore[song - 1]) * fireRate

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

    def setUpRate(self,up):
        pass
    def setFlag(self,flag):
        self.flag = flag

# p = Para(15000000,14999570)
# mdl = MedleyLive(p,1)
# mdl.ScoreCal()