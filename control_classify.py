"""
股票分类
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import crawl_service as crawl
import db_mysql_cons as cn


def update_stock_concept():
    """
    获取概念分类
    :return:
    """
    stocks = crawl.get_stock_concept()
    params_list = []
    for i in stocks.index:
        data = tuple(stocks.iloc[i].values.astype(str),)
        params_list.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_CONCEPT)
        cur.executemany(cn.ISR_T_CHN_STOCK_CONCEPT, params_list)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新股票概念事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新股票概念连接关闭')


def update_stock_pca(pca):
    """
    获取沪深300分类 上证50 中证500
    :return:
    """
    if pca == 'hs300':
        stocks = crawl.get_stock_hs300()
    elif pca == 'sz50':
        stocks = crawl.get_stock_sz50()
        stocks['weight'] = 0
    else:
        stocks = crawl.get_stock_zz500()
    param_list1 = (pca,)
    params_list2 = []
    for i in stocks.index:
        data = tuple(stocks.iloc[i].values.astype(str),) + (pca,)
        params_list2.append(data)
    try:
        con = cn.connection()
        cur = con.cursor()
        cur.execute(cn.DEL_T_CHN_STOCK_PCA, param_list1)
        cur.executemany(cn.ISR_T_CHN_STOCK_PCA, params_list2)
        res = cur.rowcount
        con.commit()
        return res
    except Exception as e:
        con.rollback()
        print('更新', pca, '事务处理失败', e)
        return -1
    finally:
        cur.close()
        con.close()
        print('更新', pca, '连接关闭')
