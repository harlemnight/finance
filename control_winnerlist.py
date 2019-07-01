"""
龙虎榜
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import crawl_service as crawl
import db_mysql_cons as cn


def update_stock_winner(datetime):
    """
    获取每日龙虎榜列表
    :return:
    """
    stocks = crawl.get_stock_winner(datetime)
    if stocks is None:
        return -1
    #print(stocks.columns.values.tolist())
    param_list1 = (datetime,)
    params_list2 = []
    for i in stocks.index:
        data = (datetime,) + tuple(stocks.iloc[i].values.astype(str),)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_WINER, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_WINER, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新龙虎榜列表事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新龙虎榜列表连接关闭')

