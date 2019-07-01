import configparser
import cx_Oracle as orac
import pandas as pd
import os
#py2.7.14old server may be utf-8' codec can't decode byte 0x8b in position 2:
#localmachine is no problem
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def exportoExcel(usename, password,orcl,querysql):
    try:
        dbcon = orac.connect(usename, password, orcl)
        res = pd.read_sql(querysql, dbcon)
        return res
    except Exception as e:
        dbcon.rollback()
    finally:
        dbcon.close()


def main(filepath):
    cf = configparser.ConfigParser()
    cf.read(filepath)
    dbcfg = cf.items(section='config')
    dbdict = {i[0]: i[1] for i in dbcfg}
    writer = pd.ExcelWriter('out.xlsx')
    user = dbdict['user']
    pwd = dbdict['pwd']
    orcl = dbdict['orcl']
    exesql = cf.get(section='sql',option='exesql')
    rest = exportoExcel(user,pwd,orcl,exesql)
    rest.to_excel(writer, 'sheet1')
    writer.save()

main('config.ini')