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
    cf.read(filepath, encoding='utf-8-sig') #chinese
    db_cfg = cf.items(section='db_config')
    db_dict = {i[0]: i[1] for i in db_cfg}
    user = db_dict['user']
    password = db_dict['pwd']
    connect = db_dict['connect']
    commit_row = db_dict['commit_row']
    tablename = cf.get(section='sql', option='table_name')
    file_name = cf.get(section='file', option='file_name')
    #content = xlrd.open_workbook(filename=file_name, encoding_override='gbk')
    df = pd.read_excel(file_name)
    #data = df.head()  # 默认读取前5行的数据
    try:
        dbcon = orac.connect(user, password, connect)
        rs = dbcon.cursor()
        sql = 'insert into '.table_name;
        for i in range(len(df)):
            rs.execute(sql % (df.ix[i, 0], df.ix[i, 1], df.ix[i, 2], df.ix[i, 3]))
        if i % 10000 == 0:
            dbcon.commit()

    except Exception as e:
        dbcon.rollback()
    finally:
        dbcon.commit()
        rs.close()
        dbcon.close()


main('config.ini')