import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
import os
import subprocess

def draw(df, wait_time):
    fig1 = plt.figure(1)
    plt.ylabel('MEAN_SATS')
    plt.xlabel('MJD')
    plt.plot(df['MJD'],df['MEAN_SATS'],'-',color='b')
    plt.draw()
    plt.pause(wait_time-2)# 图片展示的秒数：比预设时间短2秒
    plt.close(fig1)

if __name__ == '__main__': 
    exe_file_path = input("请输入待处理exe的绝对路径：")
    csv_file = input("请输入生成DAT文件名：")
    wait_time = float(input("请输入程序运行周期（小时）："))
    wait_time = wait_time*3600
    
    while True:
        # if os.path.exists(csv_file):
        #     os.remove(csv_file)

        # 使用subprocess模块启动.exe文件
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"), "初始exe程序启动")
        subprocess.Popen(exe_file_path)
        time.sleep(5) #等待exe文件运行得到DAT文件

        # 读取CSV文件
        df = pd.read_csv(csv_file, header=0, index_col=0, skipinitialspace=True)
        print('正在处理文件:',csv_file)
        draw(df, wait_time)
        time.sleep(2)
