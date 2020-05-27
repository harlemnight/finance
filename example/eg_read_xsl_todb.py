import configparser
import cx_Oracle as orac
import pandas as pd
import os
#py2.7.14old server may be utf-8' codec can't decode byte 0x8b in position 2:
#localmachine is no problem


def main(filepath):
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    cf = configparser.ConfigParser()
    cf.read(filepath)
    db_cfg = cf.items(section='db_config')
    db_dict = {i[0]: i[1] for i in db_cfg}
    user = db_dict['user']
    password = db_dict['pwd']
    connect = db_dict['connect']
    tablename = cf.get(section='sql', option='table_name')
    try:
        dbcon = orac.connect(user, password, connect)
        #do somthing
    except Exception as e:
        dbcon.rollback()
    finally:
        dbcon.close()

