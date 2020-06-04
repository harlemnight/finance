import configparser
import cx_Oracle as orac
import pandas as pd
import os
import xlrd
#py2.7.14old server may be utf-8' codec can't decode byte 0x8b in position 2:
#localmachine is no problem


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
        sql = "insert into t_imp_qsswxx values( '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s')"
        print(len(df))
        for i in range(len(df)):
            print(i)
            print(df.loc[i][0])
            # rs.execute(sql % (df.loc[i, 0], df.loc[i, 1], df.loc[i, 2], df.loc[i, 3],
            #                   df.loc[i, 4], df.loc[i, 5], df.loc[i, 6], df.loc[i, 7]))
            #if i % commit_row == 0:
            dbcon.commit()
    except Exception as e:
        dbcon.rollback()
        print(e)
    finally:
        dbcon.commit()
        rs.close()
        dbcon.close()


main('config.ini')
