import json
import os

TYPE_MISSION_LIVE = 1
TYPE_CP_LIVE = 2
TYPE_EX_LIVE = 3
TYPE_TEAM_LIVE = 4
TYPE_MEDLEY_LIVE = 5
TYPE_MATCH_LIVE = 6
TYPE_NONE = -1

TYPE_LIVE_LIST = {
    "任务Live" : TYPE_MISSION_LIVE,
    "CP Live" : TYPE_CP_LIVE,
    "EX Live" : TYPE_EX_LIVE,
    "5v5 Live" : TYPE_TEAM_LIVE,
    "组曲Live" : TYPE_MEDLEY_LIVE,
    "对邦Live" : TYPE_MATCH_LIVE,
    "请选择活动类型": TYPE_NONE
}



current_directory = os.getcwd()
CONFIG_PATH = "config\config.json"
#print(CONFIG_PATH)
with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
    config_data = json.load(file)

SCORE_MISSION_MAX = config_data["UserSetting"]["SCORE_MISSION_MAX"]
SCORE_EX_MAX = config_data["UserSetting"]["SCORE_EX_MAX"]
SCORE_CP_MAX = config_data["UserSetting"]["SCORE_CP_MAX"]
SCORE_MATCH_MAX = config_data["UserSetting"]["SCORE_MATCH_MAX"]
SCORE_TEAM_MAX = config_data["UserSetting"]["SCORE_TEAM_MAX"]
SCORE_MEDLEY_MAX = config_data["UserSetting"]["SCORE_MEDLEY_MAX"]
SCORE_MIN_MEDLEY = config_data["UserSetting"]["SCORE_MIN_MEDLEY"]
STEP_MAX = config_data["UserSetting"]["STEP_MAX"]
UP_RATE_MAX = config_data["UserSetting"]["UP_RATE_MAX"]
SCORE_MIN = config_data["UserSetting"]["SCORE_MIN"]
SCORE_MIN_DEATH = config_data["UserSetting"]["SCORE_MIN_DEATH"]

NUM_OF_CP = (200,400,800)

CORRECT = 1
VALUE_TYPE_ERROR = 100
BOOL_ERROR = 101
VALUE_CP_ERROR = 102
VALUE_SONG_ERROR = 103
SCORE_TOO_LARGE = 104
SCORE_TOO_SMALL = 105
ERROR = -1

fireMedley = {
    0: 1,
    1: 5,
    2: 10,
    3: 15,
    4: 20,
    5: 25,
    6: 30,
    7: 35,
    8: 40,
    9: 45
}
fire = {
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

temp = {200: 0, 400: 0, 800: 0}

UP_RATE = "UP_RATE"
OTHERS_SCORE = "OTHERS_SCORE"
SUPPORT_BAND = "SUPPORT_BAND"
USR_AVG_SCORE = "USR_AVG_SCORE"

notice_mission = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。\n其他人分数：指在协力演出中，其他人获得的总分。若采用自由演出控分，则该处输入0。\n支援乐队综合力：指在乐队编成界面中，显示“支援乐队综合力”的大小。\n注意，改变队伍编成以改变加成倍率时，支援乐队综合力也大概率会产生变化，请及时关注。\n任务LIVE中，理论上单次最低获取120PT（支援乐队为0，无法实现），注意合理规划剩余PT。"
notice_cp = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。\n其他人分数：指在协力演出中，其他人获得的总分。若采用自由演出或挑战演出控分，则该处输入0。\n挑战LIVE按键：选择是否通过挑战LIVE控分。\nCP LIVE中，挑战LIVE单次最低获取3272PT，非挑战LIVE单次最低获取70PT，注意合理规划剩余PT。"
notice_ex = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。\n其他人分数：指在协力演出中，其他人获得的总分。若采用自由演出控分，则该处输入0。\nEX LIVE单次最低获取130PT，注意合理规划剩余PT。"
notice_team = "输赢按键：指定在5v5中己方队伍的输赢。\n精简模式按键：控制队内排名相关计算。若开启，则只计算队内排名为第一名和第五名的方案；若关闭，则计算所有队内排名的方案。\n5v5 LIVE单次最低获取100PT，注意合理规划剩余PT。"
notice_match = "精简模式按键：控制排名相关计算。\n若开启，则只计算排名为第一名和第五名的方案；若关闭，则计算所有排名的方案。\n对邦LIVE单次最低获取100PT，注意合理规划剩余PT。"
notice_medley = "在该模式中，需要完成的歌曲数量将会自动计算，无法指定。\n组曲LIVE单次最低获取31PT，注意合理规划剩余PT。"
notice_cal = "~欢迎使用邦邦控分机~\n本模式适用于距离目标PT较近、预计单次游戏能够达到目标时使用。\n在该模式中，控分助手将给出本次游戏中需要控制的详细数据，包括控分范围、使用火的数量以及其他信息。\n当控分助手所有方案均判断为“数值过大”时，建议移步自动规划，计算多次游戏方案；\n当控分助手显示“目标PT数不可达”时，可以修改加成倍率等右侧信息进行尝试。\n若点击开始计算后，界面无任何变化，请检查输入是否完整、合法。"

notice_auto = "本模式适用于距离目标分数较远、预计单次游戏不能达到目标时使用。\n在该模式中，控分助手将给出进行游戏的次数和每一次游戏的详细数据（包括控分范围、使用火的数量等），全部完成后即可达到目标PT。\n自动规划中，“平均分数”为能够打到的大致分数，给出的方案将会按照此分数\n若点击开始计算后，界面无任何变化，请检查输入是否完整、合法。"
notice_mission_auto = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。\n在给出的方案中，除最后1~2次游戏以外，都按照该加成进行。\n支援乐队综合力：指在乐队编成界面中，显示“支援乐队综合力”的大小。\n注意，改变队伍编成以改变加成倍率时，支援乐队综合力也大概率会产生变化，请及时关注。"
notice_cp_auto = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。在给出的方案中，大部分都按照该加成进行。\n挑战LIVE按键：选择是否通过挑战LIVE控分。在给出的方案中，大部分都按照该模式进行。"
notice_ex_auto = "加成倍率：指在乐队编成界面中，右侧“活动加成”的总数值，最小为0%，最大为425%。在给出的方案中，大部分都按照该加成进行。"
notice_team_auto = "队伍内排名：指定在队伍内的排名。在给出的方案中，大部分都按照该结果进行。\n输赢按键：指定在5v5中己方队伍的输赢。在给出的方案中，大部分都按照该结果进行。"
notice_medley_auto = "【注意：组曲LIVE中的平均分数，指的是多首总分。】\n\n歌曲数量：指定每次要打的歌曲数量。在给出的方案中，大部分都按照该数量进行。"
notice_match_auto = "队伍内排名：指定在队伍内的排名。在给出的方案中，大部分都按照该结果进行。\n自由对邦按钮：选择优先完成方式，不代表只会使用该模式。"

HELP = "设置中可以自定义不同活动的最高分\n除了组曲，其他活动默认最大分数为300w，最大加成倍率默认为4.25(425%)\n【注意：组曲LIVE中的最高分数，指的是单局平均分数，不是多首总分。】\n多人游戏一般可以做到最低0分，组曲则默认最低为18500"