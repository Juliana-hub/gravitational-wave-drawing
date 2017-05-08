import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile                                                   #SciPy是一种使用NumPy来做高等数学、信号处理、优化、统计和许多其它科学任务的语言扩展


rate_h, hstrain = wavfile.read(r"H1_Strain.wav","rb")       
rate_l, lstrain = wavfile.read(r"L1_Strain.wav","rb")                          #读取音频文件，赋值给速率rate和矩阵数据strain
reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()                   #reftime是时间序列，ref_H1是数据

htime_interval = 1/rate_h
ltime_interval = 1/rate_l                                                      #对速率求倒数得到波形的时间间隔

htime_len = hstrain.shape[0]/rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
ltime_len = lstrain.shape[0]/rate_l                                            #strain为矩阵，strain.shape[0]为矩阵第一维度的长度，即数据点的个数，除以rate得到函数在坐标轴上的总长度
ltime = np.arange(-ltime_len/2, ltime_len/2, htime_interval)                   #创建以原点为中点的时间序列
                 


fig = plt.figure(figsize=(12, 6))                                              #创建一个大小为12*6的空间

plth = fig.add_subplot(221)                                                    #将空间划分为2*2块，取第一块空间作图
plth.plot(htime, hstrain, 'y')                                                 #以htime为横坐标，hstrain为纵坐标作图，颜色选择黄色
plth.set_xlabel('Time(seconds)')                                               #横坐标
plth.set_ylabel('H1 Strain')                                                   #纵坐标
plth.set_title('H1 Strain')                                                    #标题

plth = fig.add_subplot(222)                                                    
plth.plot(ltime, lstrain, 'g')                                                 
plth.set_xlabel('Time(seconds)')                                               
plth.set_ylabel('L1 Strain')                                                   
plth.set_title('L1 Strain')                                                       

plth = fig.add_subplot(223)                                                    
plth.plot(reftime, ref_H1)                                                 
plth.set_xlabel('Time(seconds)')                                               
plth.set_ylabel('Template Strain')                                                   
plth.set_title('Template')                                                       

fig.tight_layout()                                                             #自动调整图像外部边缘

plt.savefig("Gravitational_Waves_Original.png")                                #保存为png格式
plt.show()                                                                     
plt.close(fig)                                                                 