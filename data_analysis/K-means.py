import os
import re
import sqlite3
import pandas as pd
import datetime
from constant import  const
import  sql_lite as sl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import  data_process as dp
from collections import Counter

'''文件路径，读取insert文件
'''
to_file='./csv/insert.csv'
dic=['a' for i in range(10000)]
keys=[]


def open_file(file,to_file):
    if (os.path.isdir(file)):  # 判断是否是路径还
        files = dp.read_path(file)
        for file in files:
            data = dp.create_data(file)
            data = dp.data_process(data,2)
            dp.insert_csv(data,to_file)
    else:
        print("csv文件生成失败！")
        return

def set_label(datas,j,label):
    indexs = datas[datas['clSeqNo'] == j].index
    strs = datas.loc[indexs, 'type']
    datas.loc[indexs, 'type'] = strs + '.' + str(label)
    print(j,indexs[0])
    # print(j, datas.loc[indexs, 'clSeqNo'])
    # for i in indexs:
    #     strs = datas.loc[i, 'type']
    #     datas.loc[i, 'type'] = strs + '.' + str(label)
    #     print(j,i,indexs,datas.loc[i, 'clSeqNo'])
        # print(strs,label,datas.loc[i, 'type'])
        # print(label,"type的值",str(datas.loc[indexs,'type']))
    # for ins in indexs:
    #     datas.loc[ins,'type'] = label
        # print("aadasd",datas.loc[ins]['type'],label)
        # datas.loc[ins]['type'] = datas.loc[ins]['type'].map(lambda x:label)
    #     print("a",datas.loc[ins]['type'],label)

def finds(datas):
    label = 3
    for data in datas.iterrows():
        date = data[1]['ordTime']
        tmp = datas[datas['ordTime']<=date+5000]
        tmp = tmp[tmp['ordTime']>=date]
        clSeqNos = tmp['clSeqNo'].unique()
        for j in clSeqNos:
            set_label(datas,j,label)
        label = label+1


def splite(datas,i):
    dicts = []
    for data in datas.iterrows():
        types = data[1]['type']
        dicts = dicts + types.split('.')

    statistic = Counter(dicts)
    modes = statistic.most_common(1)[0]
    mode_key = int(modes[0])
    dic[mode_key] = dic[mode_key] +'.'+ str(i)
    if mode_key not in keys:
        keys.append(mode_key)
    print(mode_key,keys)
    # dic[mode_key].append(i)
    # print(mode_key,i,dic[mode_key][0])
    # print("asd",statistic)
    # print(type(invAcctId))
    # mode_value = int(modes[1])

def tragedy():
    data = pd.DataFrame(pd.read_csv(to_file,engine='python',error_bad_lines=False,names=const.MATCH_HEADER[2]))
    data.drop_duplicates(keep='first', inplace=True)
    data = data[['type','invAcctId','securityId','ordTime','clSeqNo','bsType']]
    data['type'] = data['type'].astype(str)
    # print(data.dtypes)
    data.sort_values(by='ordTime', axis=0, ascending=True)
    securityIds = data['securityId'].unique()
    invAcctIds = data['invAcctId'].unique()

    index=0
    for i in securityIds:
        datas = data[data['securityId']==i]
        # data_buy = datas[datas['bsType']==0]
        data_sell = datas[datas['bsType']==1]
        finds(data_sell)
        print("处理次数",index,i)
        index = index + 1

    for i in invAcctIds:
        tmp_sell = data_sell[data_sell['invAcctId'] == i]
        splite(tmp_sell,i)

    # print(dic)
    # for i in invAcctIds:
    #     tmp_sell = data_sell[data_sell['invAcctId']==i]
    #     if(tmp_sell is not None):
    #         print(tmp_sell['type'].value_counts())

    # print(data_buy,"sdasdasd",data_sell)
    # data_security = data.groupby('securityId')
    # gr = data_security.groups
    # print(data['securityId'].unique())
    # # keys = list(gr.keys())
    # values = list(gr.values())

    # print(keys,values[0],"dasdasd",gr[300769],len(gr[300769]))
    # print(data.iloc[2]['ordReqOrigSendTime'])

if __name__ == "__main__":
    tragedy()
    # open_file(const.FILE,to_file)