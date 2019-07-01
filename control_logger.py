"""
业务日志
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import db_mysql_cons as cn


def logger(code, operat, descrpt, content, lrrq, ywlx):
    try:
        con = cn.connection()
        cur = con.cursor()
        param = (code,) + (operat,) + (descrpt,) + (content,) + (lrrq,) + (ywlx,)
        cur.execute(cn.ISR_T_LOGGER, param)
        con.commit()
        return 1
    except Exception:
        con.rollback()
        return -1
    finally:
        cur.close()
        con.close()


def clean_his_logger():
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_HIS_T_LOGGER)
        con.commit()
        return 1
    except Exception:
        con.rollback()
        return -1
    finally:
        cur.close()
        con.close()
##########################################################################################
