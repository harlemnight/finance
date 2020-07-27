"""
行情交易数据
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import crawl_service as crawl
import db_mysql_cons as cn




def init_stock_list():
    """
    抓取所有上市股票并初始化股票代码记录
    :return:
    """
    stocks = crawl.get_all_stock_list()
    params_list = []
    for i in stocks.index:
        data = (str(i),) + tuple(stocks.loc[str(i)].values[0:].astype(str),)
        params_list.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_LIST)
        cur.executemany(cn.ISR_T_CHN_STOCK_LIST, params_list)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('初始化股票代码事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('初始化股票代码连接关闭')


def get_update_stock_code_list():
    """
    从记录中获取要更新的所有股票代码
    :return:
    """
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.QUE_T_CHN_STOCK_CODE_UPDATE_LIST)
        res = cur.fetchall()
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('获取要更新股票代码事务处理失败', e)
        return []
    finally:
        cur.close()
        con.close()
        print('获取要更新股票代码连接关闭')


def update_stock_data(code, start, end):
    """
    根据股票代码列表抓取历史交易数据并记录
    :param code:
    :param start:
    :param end:
    :return:
    """
    trades = crawl.get_stock_by_code(code, start, end)
    if trades is None:
        return -1
    param_list1 = (code,) + (start + ' 00:00:00',) + (end + ' 00:00:00',)
    le = len(trades.index)
    param_list2 = []
    for i in trades.index:
        # 才上市数据只有一条的情况
        if le < 2:
            data = (str(i),) + tuple(trades.loc[str(i)].values[0:].astype(str), )
        else:
            data = (str(i),) + tuple(trades.loc[str(i)].values[0:].astype(str)[0],)
        param_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_TRADES, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_TRADES, param_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新个股行情事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新个股行情连接关闭')

##########################################################################################


def init_index_list():
    """
    初始化指数列表并记录
    :param code:
    :param start:
    :param end:
    :return:
    """
    idxs = crawl.get_all_index_list()
    params_list = []
    for i in idxs.index:
        data = tuple(idxs.iloc[i].values.astype(str),)
        params_list.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_INDEX_LIST)
        cur.executemany(cn.ISR_T_CHN_INDEX_LIST, params_list)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('初始化指数列表事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('初始化指数列表连接关闭')


def get_update_index_code_list():
    """
    从记录中获取所有指数代码
    :return:
    """
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.QUE_T_CHN_INDEX_CODE_UPDATE_LIST)
        res = cur.fetchall()
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('获取所有指数代码事务处理失败', e)
        return []
    finally:
        cur.close()
        con.close()
        print('获取所有指数代码连接关闭')


def update_index_data(code, start, end):
    """
    更新指数数据并记录
    :param code:
    :param start:
    :param end:
    :return:
    """
    indexs = crawl.get_index_by_code(code, start, end)
    if indexs is None:
        return -1
    le = len(indexs.index)
    param_list1 = (code,) + (start + ' 00:00:00',) + (end + ' 00:00:00',)
    param_list2 = []
    for i in indexs.index:
        # 才上市数据只有一条的情况
        if le < 2:
            data = (str(i),) + tuple(indexs.loc[str(i)].values[0:].astype(str), )
        else:
            data = (str(i),) + tuple(indexs.loc[str(i)].values[0:].astype(str)[0], )
        param_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_INDEX_TRADES, param_list1)
        cur.executemany(cn.ISR_T_CHN_INDEX_TRADES, param_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新指数行情事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新指数行情连接关闭')
