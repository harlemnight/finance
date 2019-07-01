"""
财务数据 ,限售股解禁,基金持股
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import crawl_service as crawl
import db_mysql_cons as cn


def update_stock_report(report, nd, jd):
    """
    获取业绩报告（主表)
    :return:
    """
    if report == 'report':
        stocks = crawl.get_stock_report(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_REPORT
        sql2 = cn.ISR_T_CHN_STOCK_REPORT
    elif report == 'profit':
        stocks = crawl.get_stock_profit(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_PROFIT
        sql2 = cn.ISR_T_CHN_STOCK_PROFIT
    elif report == 'operation':
        stocks = crawl.get_stock_operation(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_OPERATION
        sql2 = cn.ISR_T_CHN_STOCK_OPERATION
    elif report == 'growth':
        stocks = crawl.get_stock_growth(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_GROWTH
        sql2 = cn.ISR_T_CHN_STOCK_GROWTH
    elif report == 'debtpaying':
        stocks = crawl.get_stock_debtpaying(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_DEBTPAYING
        sql2 = cn.ISR_T_CHN_STOCK_DEBTPAYING
    else:
        stocks = crawl.get_stock_cashflow(nd, jd)
        sql1 = cn.DEL_T_CHN_STOCK_CASHFLOW
        sql2 = cn.ISR_T_CHN_STOCK_CASHFLOW
    if stocks is None:
        return -1
    params_list2 = []
    param_list1 = (nd,) + (jd,)
    for i in stocks.index:
        data = (nd,) + (jd,) + tuple(stocks.iloc[i].values.astype(str),)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(sql1, param_list1)
        cur.executemany(sql2, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新', report, '事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新', report, '连接关闭')


def update_stock_forecast(nd, jd):
    """
    获取业绩预告
    :return:
    """
    stocks = crawl.get_stock_forecast(nd, jd)
    print(stocks)
    if stocks is None:
        return -1
    params_list2 = []
    param_list1 = (nd,) + (jd,)
    for i in stocks.index:
        data = (nd,) + (jd,) + tuple(stocks.iloc[i].values.astype(str),)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_FORECAST, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_FORECAST, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新业绩预告事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新业绩预告连接关闭')


def update_stock_xsgjj(nd, yf):
    """
    获取限售股解禁
    :return:
    """
    stocks = crawl.get_stock_xsgjj(nd, yf)
    if stocks is None:
        return -1
    params_list2 = []
    param_list1 = (nd,) + (yf,)
    for i in stocks.index:
        data = (nd,) + (yf,) + tuple(stocks.iloc[i].values.astype(str),)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_XSGJJ, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_XSGJJ, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新业限售股解禁事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新限售股解禁连接关闭')


def update_stock_jjcg(nd, jd):
    """
    获取基金持股
    :return:
    """
    stocks = crawl.get_stock_jjcg(nd, jd)
    if stocks is None:
        return -1
    params_list2 = []
    param_list1 = (nd,) + (jd,)
    for i in stocks.index:
        data = (nd,) + (jd,) + tuple(stocks.iloc[i].values.astype(str),)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_JJCG, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_JJCG, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新基金持股事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新基金持股连接关闭')

