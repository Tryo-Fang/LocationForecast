import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.contrib.learn as learn


def getherofeture(path, sheet):
    d = pd.read_excel(path, sheet)
    return d


def getgamedata(path):
    d = pd.read_csv(path)

    d2 = d[d['time'] < 1800]
    d3 = d2[d2['hero'] == '小乔.png']
    # d2.to_csv('D:\gamedatatest.csv')

    return d3


def processdata(d):
    d['fore'] = None
    for index, row in d.iterrows():
        x = row['x'] // 500
        y = row['y'] // 500
        area = x * 10 + y
        row['group'] = area
        row['fore'] = judgearea(area)
        d.loc[index] = row
    # d=d.drop('hero',1)
    d.to_csv('D:\gamedataareaF.csv')
    return d


def addfeture(d):
    df = pd.read_csv('D:\gamedataarea.csv')  # 读取所有英雄数据
    d['location1'] = None
    d['angle1'] = None
    d['location2'] = None
    d['angle2'] = None
    d['location3'] = None
    d['angle3'] = None
    d['location4'] = None
    d['angle4'] = None
    d['location5'] = None
    d['angle5'] = None
    for index, row in d.iterrows():
        i = 0
        x = row['gameId']
        y = row['time']
        d1 = df[(df['gameId'] == x) & (df['time'] == y)]
        for index1, row1 in d1.iterrows():
            areahero=row1['group']
            angle=row1['angle']
            if i == 0:
                row['location1'] =areahero
                row['angle1'] = angle
            if i == 1:
                row['location2'] = areahero
                row['angle2'] = angle
            if i == 2:
                row['location3'] = areahero
                row['angle3'] = angle
            if i == 3:
                row['location4'] = areahero
                row['angle4'] = angle
            if i == 4:
                row['location5'] = areahero
                row['angle5'] = angle
            i=i+1

        d.loc[index] = row
    d.to_csv('D:\gamedataareaFinal.csv')

    return d


def judgearea(area):
    y = area // 10
    x = area % 10
    if x < y:
        if y < 10 - 3 * x:
            area = 1
        elif y < 10 - x / 3:
            area = 2
        else:
            area = 3
    else:
        if y < 10 / 3 - x / 3:
            area = 4
        elif y < 30 - 3 * x:
            area = 5
        else:
            area = 6
    return area


# table1 = getgamedata('D:\gamedataarea.csv')
# f = open('D:\gamedataarea.csv')
#df = pd.read_csv('D:\gamedataareaQ.csv')  # 读入数据
#processdata(df)
#d1=addfeture(df)
'''
df = pd.read_csv('D:\gamedataareaFinal.csv')  # 读入数据
area = df['group']
df.drop(labels=['group'], axis=1,inplace = True)
df.drop(labels=['se1'], axis=1,inplace = True)
df.drop(labels=['se'], axis=1,inplace = True)
df.insert(15, 'location', area)
df.to_csv('D:\gamedataareaFinalX.csv',index=0)
#print(df)
'''
#data = df.iloc[:, 3:17].values  # 取第3-7列
#print(data)
'''
thero=getherofeture('D:\work\developer\预测项目\全英雄基础属性.xlsx','2018.6.21')
print(thero[thero['name']=='小乔'])
'''
'''
f = open('D:\gamedataareaQ.csv')
df = pd.read_csv(f)  # 读入数据
data = df.groupby(['gameId']).mean() 
'''
f = open('D:\gamedataareaFinalX.csv')
df = pd.read_csv(f)  # 读入数据
d=df['location']
print(d)
d1=np.mean(d,axis=0)
print(d1)
d2=np.std(d,axis=0)
print(d2)
