
import sqlite3
import data_process as dp
from constant import  const

def to_sql(data,id):
    if (data is not None):
        conn = sqlite3.connect(const.DB_NAME)     # 建立连接，如果不存在将会创建
        print ("Open database successfully")
        datas = data.drop(['type'], axis=1)
        datas.to_sql(const.SQL_TABLE[id],con=conn,if_exists='append',index=False)

    # data.drop(['type'], axis=1, inplace=True)
    # cursor = conn.cursor()
    # cursor.execute('select * from promotion')
    # print(cursor.execute('select * from promotion'))
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)
    # dp.open_file(const.FILE, const.TO_FILE)