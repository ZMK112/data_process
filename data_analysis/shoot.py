import os
import pandas as pd
from constant import  const
import  data_process as dp
import time,datetime

'''
生成对应的五个csv文件，文件名如：数据块名称+csv
'''
def data_to_csv(file,to_file):
    if (os.path.isdir(file)):  # 判断是否是路径还
        files = dp.read_path(file)
        for file in files:
            data = dp.create_data(file)
            for i in const.DATA_PART:
                to_files = to_file + i +'.csv'
                print(to_files)
                id = const.DATA_PART.index(i)
                datas = dp.data_process(data,id)
                dp.insert_csv(datas,to_files)
    else:
        print("创建csv文件失败！")
        return

'''
str：数据块名
输出：对应数组中的index
'''
def to_index(str):
    return const.DATA_PART.index(str)

'''
对于ordReqOrigSendTime字段进行时间转换
对于ordReqOrigSendTime：时间格式是从1970开始的秒数
'''
def get_time(times):
    timeArray = time.localtime(times)
    data_time = int(timeArray[3]*1e7+timeArray[4]*1e5+timeArray[5]*1e3)
    return data_time


'''读取指定数据类型的csv文件,data_name为指定数据类型
   输出：对应的数据dataframe
'''
def order_process(to_file,data_name):
    to_files = to_file + data_name + '.csv'
    index = const.DATA_PART.index(data_name)
    data = pd.DataFrame(pd.read_csv(to_files, engine='python', error_bad_lines=False,
                                    names=const.MATCH_HEADER[index]))
    data.drop_duplicates(keep='first', inplace=True)

    return data

'''对于 orfer insert数据进行处理
处理条件：
1、时间限制：9点30分又10秒之间
2、其他时间段订单数量少于100份

输出符合要求的inser数据的dataframe类型数据

函数参数：
inserts ： order insert的dataframe类型数据
feild： 时间字段，此处是ordTime
time：限制时间
'''
def data_insert(inserts,filed,time):
    inserts_data = pd.DataFrame()
    tmp = inserts[['clSeqNo', 'invAcctId']].groupby('invAcctId').count()
    inserts = inserts[inserts[filed]<time]
    tmps = inserts[['clSeqNo', 'invAcctId']].groupby('invAcctId').count()
    indexs = list(tmps.index)

    for i in indexs:
        if(tmp.loc[i]['clSeqNo']-tmps.loc[i]['clSeqNo'])<100:   #对于其他时间段订单数量少于100份
            inserts_data = inserts_data.append(tmps.loc[i])
        else:
            pass

    inserts_data['clSeqNo'] = inserts_data['clSeqNo'].astype(int) #将float数据类型转换为int数据类型
    return inserts_data

'''
处理reject的废单数据
处理条件：时间限制：9点30分又10秒之间
输出符合要求的eject数据的dataframe类型数据
'''
def data_reject(reject,filed,time):
    reject[filed] = reject[filed].map(lambda x: get_time(x))
    reject = reject[reject[filed]<time]
    rejects = reject[['origClSeqNo', 'invAcctId']].groupby('invAcctId').count()
    return rejects


'''shoot_analysis：判断打版用户

   获取经过初步条件处理的dataframe类型数据，对于数据进行条件判断
   判断条件：废单量和废单量均要大于10
   输出：符合条件的用户账户号
'''
def shoot_analysis(times,time_requirement):
    insert_data = order_process(const.CSV_PATH,'Order Insert Event')
    reject_data = order_process(const.CSV_PATH,'Business Reject Event')

    insert_data = data_insert(insert_data,'ordTime',time_requirement)
    reject = data_reject(reject_data,'ordReqOrigSendTime',time_requirement)

    indexs = list(insert_data[insert_data['clSeqNo']>=times].index)  #条件大于10的订单数目
    indexs_reject = reject[reject['origClSeqNo']>=times].index

    # 同时满足废单条件和订单条件
    for i in indexs:
        if i not in indexs_reject:
            indexs.remove(i)

    print(indexs)
    return  indexs


'''long_analysis：判断长线用户
参数：
filed：时间字段
start-time：限制起始时间
end-time：限制结束时间

输出符合条件的用户账户号list
'''

def long_analysis(filed,start_time,end_time,rate):
    inserts_data = pd.DataFrame()
    inserts = order_process(const.CSV_PATH, 'Order Insert Event')
    tmp = inserts[['clSeqNo', 'invAcctId']].groupby('invAcctId').count()

    # print(inserts[filed])
    # 对于数据起始时间和结束时间进行提取
    inserts = inserts[inserts[filed]<=end_time]
    inserts = inserts[inserts[filed]>=start_time]
    tmps = inserts[['clSeqNo', 'invAcctId']].groupby('invAcctId').count()
    indexs = list(tmps.index)

    for i in indexs:
        if(tmps.loc[i]['clSeqNo']/tmp.loc[i]['clSeqNo'])>=rate:   #限制时间段内的订单数量占据总订单数的85%
            inserts_data = inserts_data.append(tmps.loc[i])
        else:
            pass

    ins = inserts_data.index
    print(ins)
    return ins



if __name__ == "__main__":
    # 函数调用方式
    # data_to_csv(const.FILE, const.CSV_PATH )
    # shoot_analysis(10,const.TIME_LIMIT)
    long_analysis('ordTime',const.START_TIME,const.END_TIME,const.RATE)
