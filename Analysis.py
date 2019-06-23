import numpy as np
import pandas as pd

from matplotlib import pyplot

df = pd.read_excel(r'test1.xls')
data = pd.DataFrame(df)
# print(str(int(data['price'].mean())) + '万')  #杭州市均价
# print(data.sort_values('price',ascending=False).head(10))  #杭州市售价最高前十
# print(data.sort_values('price').head(10))   #杭州市售价最低前十
region_dict = ['西湖','下城','江干','拱墅','上城','滨江','余杭','萧山','富阳','临安','下沙']

def get_data(region):
    print(region['region'].head(1) + "均价")
    print('\n')
    print(str(int(region['price'].mean())) + '万')
    print('\n')
    print(region['region'].head(1) + "最高价前十")
    print('\n')
    print(region.sort_values('price', ascending=False).head(10))
    print('\n')
    print(region['region'].head(1) + "最低价前十")
    print('\n')
    print(region.sort_values('price').head(10))

for i in region_dict:
    xihu_data = data[data.region == str(i)]
    print(get_data(xihu_data))
