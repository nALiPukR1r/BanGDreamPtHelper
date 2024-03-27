import config

def exceptionHandling(EXP_NUMER):
    if EXP_NUMER == config.VALUE_TYPE_ERROR:
        print("【ERROR : 输入的数据类型有误，请检查输入！】")
        #messagebox.showerror
    elif EXP_NUMER == config.BOOL_ERROR:
        print("【ERROR : 输入的数据类型有误，请检查输入！】")
        # messagebox.showerror
    elif EXP_NUMER == config.VALUE_CP_ERROR:
        print("【ERROR : 输入的CP数量有误，请检查输入！】")
        # messagebox.showerror
    elif EXP_NUMER == config.VALUE_SONG_ERROR:
        print("【ERROR : 输入的歌曲数量有误，请检查输入！】")
        # messagebox.showerror
    else:
        print("【ERROR : 发生不明错误！】")
        # messagebox.showerror
    return False, config.ERROR


def intCheck(var):
    #print(var)
    for item in var:
        if item < '0' or item > '9':
            return config.VALUE_TYPE_ERROR

    return config.CORRECT

def boolChcek(var):

    if len(var) != 1:
        return config.BOOL_ERROR
    elif var == "Y" or var == 'y':
        return True
    elif var == "N" or var == 'n':
        return False
    else:
        return config.BOOL_ERROR

def cpCheck(var):
    if var % 200 == 0:
        return config.CORRECT
    else:
        return config.VALUE_CP_ERROR

def songNumCheck(var):
    if var < 1 or var > 3:
        return config.VALUE_SONG_ERROR
    else:
        return config.CORRECT

#计算出的分数可能超过了最大值或者最小值，修正
def scoreCheck(var, min,max):
    if var < min :
        return config.SCORE_TOO_SMALL
    elif var > max:
        return config.SCORE_TOO_LARGE
    else:
        return config.CORRECT