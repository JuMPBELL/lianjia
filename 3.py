import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import  xlrd
import xlwt

# 当天被投入使用的公共自行车的数量，并计算公共自行车平均使用频率。
df = pd.read_excel('第1天.xls')
num = len(df)
sum = df.drop_duplicates(subset='车号SN',inplace=False)['车号SN']

book_1 = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book_1.add_sheet('3.1',cell_overwrite_ok=True)
sheet.write(0,0,'当天投入公共自行车数量')
sheet.write(1,0,len(sum))
sheet.write(0,1,'当天公共自行车平均使用频率')
sheet.write(1,1,int(num/len(sum)))
book_1.save('3.1.xls')

# 统计对同一站点的用车时长的分布情况。
book_2 = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book_2.add_sheet('3.2',cell_overwrite_ok=True)

bike_no = df['车号SN']
send_station = df['借出车站号']
return_station = df['还车车站号']
use_time = df['用车时间']
return_station_array = np.array(return_station)
use_time_array = np.array(use_time)
bike_no_array = np.array(bike_no)
a = 0
b = 0
time_list=[]
time_sum=0
time_5 = time_10 = time_20 = time_40 = time_60 = time_60_more = 0
for i in send_station:
    if return_station_array[a] == i and use_time_array[a] != 0:
        if use_time_array[a] <= 5:
            time_5 = time_5 + 1
        if use_time_array[a] > 5 and use_time_array[a] <= 10:
            time_10 = time_10 + 1
        if use_time_array[a] > 10 and use_time_array[a] <= 20:
            time_20 = time_20 + 1
        if use_time_array[a] > 20 and use_time_array[a] <= 40:
            time_40 = time_40 + 1
        if use_time_array[a] > 40 and use_time_array[a] <= 60:
            time_60 = time_60 + 1
        if use_time_array[a] > 60:
            time_60_more = time_60_more + 1
        time_list.append(use_time_array[a])
        time_sum = time_sum + use_time_array[a]
        b = b + 1
    a = a + 1

sheet.write(0,0,'骑行时间5分钟以下')
sheet.write(1,0,time_5)
sheet.write(0,1,'骑行时间5分钟以上10分钟以下')
sheet.write(1,1,time_10)
sheet.write(0,2,'骑行时间10分钟以上20分钟以下')
sheet.write(1,2,time_20)
sheet.write(0,3,'骑行时间20分钟以上40分以下')
sheet.write(1,3,time_40)
sheet.write(0,4,'骑行时间40分钟以上60分钟以下')
sheet.write(1,4,time_60)
sheet.write(0,5,'骑行时间60分钟以上')
sheet.write(1,5,time_60_more)
sheet.write(0,6,'平均用车时长')
sheet.write(1,6,time_sum/b)
book_2.save('3_2.xls')

# print('借还同一站点最长用车时长：',max(time_list),'借还同一站点最短用车时长：',min(time_list),'平均用车时长：',time_sum/b)
# print('骑行时间5分钟以下：',time_5,'骑行时间5分钟以上10分钟以下：',time_10,'骑行时间10分钟以上20分钟以下：',time_20)
# print('骑行时间20分钟以上40分以下：',time_40,'骑行时间40分钟以上60分钟以下：',time_60,'骑行时间60分钟以上：',time_60_more)

plt_date = [time_5,time_10,time_20,time_40,time_60,time_60_more]
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(range(6),plt_date,align='center',color='steelblue',alpha=0.8)
plt.ylabel('用车数量')
plt.title('借还同一站点用车情况')
plt.xticks(range(6),['<5分钟','5-10分钟','10-20分钟','20-40分钟','40-60分钟','>60分钟'])
plt.ylim([100,900])
for x,y in enumerate(plt_date):
    plt.text(x, y + 100, '%s' % round(y, 1), ha='center')
plt.show()