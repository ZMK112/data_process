import os
import re
import sqlite3
import pandas as pd
import datetime
# import pysnooper
from constant import  const
import  sql_lite as sl


'''
数据匹配正则表达式,总共包括五个部分 Business Reject Event、Order Report Event、Order Insert Event、Trade report Event、FundTrsf Report Event
正则表达式的匹配格式：(?P<字段名>字段名\[(.*?)\])，最终生成与字段数据对应的数组
'''

'''
函数说明：
read_path：函数用于文件路径的解析，默认只解析读取一级或二级目录下的文件
sub_value：用于字典类型中value数据的读取，string类型数据直接跳过
decide_header：提取数据类型名称，并输出对应的数据类型在全局数组match_pattern、match_header中的位置
match：对于数据内容的正则表达式的匹配
create_csv：将数据生成dataframe类型数据，并插入到csv文件中，因为数据可能会很大，所以只能单个数组插入，to_csv功能不再单独分割
open_file:判断路径类型，调用create_csv函数，生成数据的csv文件
'''

'''
 对于包含二级目录的文件路径处理（如果存在二级目录则生成文件路径数组）
 对于多个log数据文件保存在对应的文件夹，读取目录下的所有文件
'''
def read_path(rootdir):
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    files = []
    for i in range(0, len(list)):
        if list[i][0] == '.':
            pass
        else:
            path = os.path.join(rootdir, list[i])
            if os.path.isfile(path):
                files.append(path)
            else:
                for level in os.walk(path):
                    if (level[const.FILE_DEPTH]):  # 文件的二级目录，如果需要多级目录可以在此处修改
                        for j in level[const.FILE_DEPTH]:
                            if (j[0] == '.'):
                                pass
                            else:
                                second_level = os.path.join(path, j)
                                if os.path.isfile(second_level):
                                    files.append(second_level)
                                else:
                                    pass
    return files

'''
判断数据段的表头：对数据块名进行正则匹配，输出header数组对应位置编号，如果没有找到
则输出None；
找出当前解析的数据块对应的数据类型
'''
def decide_header(str):  # 匹配数据块类型
    res = re.search(const.DATA_HEADER, str)
    if res == None:
        return
    else:
        string = res.group()
        head = string[4:len(string)]
        if head in const.DATA_PART:
            # print(const.DATA_PART.index(head))
            return const.DATA_PART.index(head)
        else:
            pass

'''
正则表达式的匹配并与对应字段生成dict字典，最终输出包含实际数据的数组values
第一列是对应于数据类型type，后续列为数据内容，实际的数据内容匹配在这部分完成
'''
def match(pattern, strs,index): #参数：正则表达式，解析内容，数据类型（对于数据类型数组中的位置）
    values = []
    values.append(str(index))
    for i in pattern:
        res = re.search(i, strs)
        if res == None:  # 如果没有成功的进行正则匹配，则直接退出
            return
        else:
            tmp = res.group()
            value = re.findall(r'\[(.*?)\]', tmp)
            if(len(value)):
                string=''.join(value)
                values.append(string)
            else:
                values.append(tmp[0:8]+tmp[9:11]+tmp[12:14]+tmp[15:])
                # values.append(tmp)
                # print(tmp,tmp[0:8]+tmp[9:11]+tmp[12:14]+tmp[15:])

    return values


'''
将数据块处理好的数据，生成dict，并生成dataframe格式，生成csv文件
'''
def create_data(file):

    i=0 #计算处理数据个数
    # starttime = datetime.datetime.now() #测试函数运行时间
    dicts = []
    with open(file, "rb") as f:
        for line in f:
            strs = str(line)
            index = decide_header(strs)
            if (index != None):
                pattern = const.MATCH_PATTERN[index]
                match_dic = match(pattern, strs,index)
                dicts.append(match_dic)
                # data.append(pd.DataFrame(dicts, columns=const.MATCH_HEADER[index]))
            else:
                pass
            #显示数据处理进度，可以删掉
            i=i+1
            print("次数",i)

    data = pd.DataFrame(dicts)
    return data
    # date.to_csv(to_file, header=None, mode='a')
    # endtime = datetime.datetime.now()  #获取运行时间
    # print("运行时间",(endtime - starttime).seconds)#显示最终运行时间

'''
将dataframe数据类型插入csv文件中
'''
def insert_csv(data,to_file):
    if (data is not None):
        data.to_csv(to_file, header=None, mode='a',index=0)

'''
将dataframe数据类型插入数据库
'''
def insert_sql(data,id):
    sl.to_sql(data, id)


def data_process(data,id):
    datas = data[data[0] == str(id)].dropna(axis=1, how='all')
    if (len(datas)):
        datas.columns = const.MATCH_HEADER[id]
        datas = datas.apply(pd.to_numeric, errors='ignore')
        # tmp['date']=tmp['date'].astype('int')
        # print(datas.dtypes, "adasdasdasd", datas['date'])
        return datas
    else:
        return

# 读取文件路径，并调用creat_csv函数
# @pysnooper.snoop()
def data_to_csv(file,to_file):
    if (os.path.isdir(file)):  # 判断是否是路径还
        files = read_path(file)
        for file in files:
            data = create_data(file)
            for i in const.DATA_PART:
                id = const.DATA_PART.index(i)
                datas = data_process(data,id)
                insert_csv(datas,to_file)
    else:
        print("创建csv文件失败！")
        return

def data_to_sql(file):
    if (os.path.isdir(file)):  # 判断是否是路径还
        files = read_path(file)
        for file in files:
            data = create_data(file)
            for i in const.DATA_PART:
                id = const.DATA_PART.index(i)
                datas = data_process(data,id)
                insert_sql(datas,id)
    else:
        print("插入数据库失败！")
        return

# def open_file(file, to_file):
#     if (os.path.isdir(file)):  # 判断是否是路径还
#         files = read_path(file)
#         for file in files:
#             data = create_data(file)
#             for i in const.DATA_PART:
#                 id = const.DATA_PART.index(i)
#                 datas = data_process(data,id)
#                 insert_sql(datas,id)
#     else:
#         pass

'''
data_to_sql()或者data_to_csv()两部分函数
分别将数据导入数据库和csv文件
'''
if __name__ == "__main__":
    data_to_csv(const.FILE, const.TO_FILE)
    # data_to_sql(const.FILE)














