import config

class Para:
    __liveType = None
    __target = 0
    __current = 0
    __fireRate = {
        0:1,
        1:5,
        2:10,
        3:15,
        4:16,
        5:20,
        6:24,
        7:28,
        8:32,
        9:36,
        10:40
    }
    #[1,5,10,15,20,25,30,35,40,45]
    __fireRateMedley = {
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

    def __init__(self,target,current):
        self.__target = target
        self.__current = current


    # def liveTypeCheck(self,live):
    #     try:
    #         index = self.__liveTypeList.index(live)
    #         return index
    #
    #     except ValueError:
    #         return -1  # 或者你可以返回None，表示元素不存在

    def MedleyFire(self,fire):
        if fire == 0:
            self.__fire = 1
        else:
            self.__fire = fire * 5

    def OtherLive(self,fire):
        if fire >= 0 and fire <= 10:
            if(fire == 10):
                self.__fire = 40
            else:
                self.__fire = self.__fireRate[fire]
        else:
            print("invalid fire num!")

    def getTarget(self):
        return self.__target

    def getCurrent(self):
        return self.__current

    def getFire(self):
        return self.__fireRate

    def getMedleyFire(self):
        return self.__fireRateMedley
