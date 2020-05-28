import configparser
import cx_Oracle as orac
import pandas as pd
import os
import xlrd
#py2.7.14old server may be utf-8' codec can't decode byte 0x8b in position 2:
#localmachine is no problem
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def main(filepath):
    cf = configparser.ConfigParser()
    cf.read(filepath, encoding='utf-8-sig')
    db_cfg = cf.items(section='db_config')
    db_dict = {i[0]: i[1] for i in db_cfg}
    user = db_dict['user']
    password = db_dict['pwd']
    connect = db_dict['connect']
    tablename = cf.get(section='sql', option='table_name')
    file_name = cf.get(section='file', option='file_name')
    #content = xlrd.open_workbook(filename=file_name, encoding_override='gbk')
    df = pd.read_excel(file_name, nrows=1)
    #data = df.head()  # 默认读取前5行的数据
    print(len(df))
    #print("获取到所有的值:\n{0}".format(data))  # 格式化输出
    # try:
    #     dbcon = orac.connect(user, password, connect)
    #     #do somthing
    # except Exception as e:
    #     dbcon.rollback()
    # finally:
    #     dbcon.close()


main('config.ini')