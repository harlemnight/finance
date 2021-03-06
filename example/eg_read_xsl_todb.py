import configparser
import cx_Oracle as orac
import pandas as pd
import os
import numpy as np
import xlrd
#py2.7.14old server may be utf-8' codec can't decode byte 0x8b in position 2:
#localmachine is no problem
#https://blog.csdn.net/wsp_1138886114/article/details/88721075
#https://www.jb51.net/article/128548.htm
#https://www.cnblogs.com/kerrycode/p/11665926.html
#https://www.cnblogs.com/hzhida/archive/2012/08/13/2636735.html
#https://www.cnblogs.com/isme-zjh/p/11579432.html
#https://www.cnblogs.com/chenhuabin/p/12689163.html
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
    db_type = db_dict['db_type']
    table_name = cf.get(section='sql', option='table_name')
    table_cols = cf.get(section='sql', option='table_cols')
    file_name = cf.get(section='file', option='file_name')
    #content = xlrd.open_workbook(filename=file_name, encoding_override='gbk')
    print('reading ' + file_name)
    df = pd.read_excel(file_name, dtype=str, keep_default_na=False)
    #, keep_default_na=False
    #如果一个excel同列有数字和字符串，处理时有问题需，为方便统一转换为str
    print('end ' + file_name)
    df.fillna('', inplace=True)  #当前panda的版本好像无效
    param_list = []
    sql = 'insert into ' + table_name + ' values( ' + ",".join(':'+str(i+1) for i in range(int(table_cols))) + ')'
    #insert into sj_ztsj.t_imp_qsswxx values( :1,:2,:3,:4,:5,:6,:7,:8)
    print(sql)
    if db_type == 'oracle':
        try:
            db_con = orac.connect(user, password, connect)
            rs = db_con.cursor()
            for i in range(len(df)):
                # par = []
                # for j in range(len(df.loc[i])):
                #     if str(df.loc[i][j]) == 'nan':
                #         df.loc[i][j] = ''
                #     par.append(df.loc[i][j])
                # param_list.append(par)
                param_list.append(df.loc[i])
                if (i+1) % int(commit_row) == 0:
                    rs.executemany(sql, param_list)
                    db_con.commit()
                    param_list = []
                    print('commit '+commit_row+' rows')
            rs.executemany(sql, param_list)
            db_con.commit()
            print('commit last rows')
        except Exception as e:
            db_con.rollback()
            print(e)
        finally:
            db_con.commit()
            rs.close()
            db_con.close()
    elif db_type == 'mysql':
        print(1)
    else:
        print(2)
    print('app end')


main('config.ini')
