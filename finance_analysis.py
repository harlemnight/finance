"""
更新股票数据入口 数据都是基本根据
日期，季度，月份等时间
先删除后在插入
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import control_trade as ctrl
import control_logger as log
import control_classify as ify
import control_report as rpt
import control_winnerlist as win
import datetime as date
import mpl_finance as mpl


def main_7day():
    """
    行情
    :return:
    """
    start = '2019-06-24'
    end = '2019-07-12'

    # from datetime import datetime
    # start_date = datetime(2004, 4, 5).date()
    log.clean_his_logger()
    update_all_stock_trade(start)  # 个股
    update_all_index_trade(start)  # 指数
    update_stock_winner(start, end)  # 龙虎榜



def main_sometime():
    """
    分类数据
    :return:
    """
    update_stock_concept()  # 概念
    update_stock_pca()     # hs300 sz50 zz500
    today = date.date.today()
    today_year = today.strftime("%Y")
    q_year = int(today_year)-1
    m_year = int(today_year)+1
    t_year = int(today_year)
    update_stock_report(q_year, m_year)  # 财报
    update_stock_forecast(q_year, m_year)  # 业绩预告
    update_stock_jjcg(t_year, m_year)  # 基金持股
    update_stock_xsgjj(t_year, m_year)  # 限售股解禁


def update_all_stock_trade(start):
    """
    更新个股
    调用频率 每周调用1次 或者每天1次
    :param start:
    :return:
    """
    today = date.date.today()
    ctrl.init_stock_list()
    codes = ctrl.get_update_stock_code_list()
    end = today.strftime("%Y-%m-%d")
    for code in codes:
        count = ctrl.update_stock_data(code['code'], start, end)
        print(code['code'])
        if count > 0:
            log.logger(code['code'], 'update', 'OK', '历史行情', end, 'stock')
        elif count == 0:
            log.logger(code['code'], 'update', 'ED', '历史行情', end, 'stock')
        else:
            log.logger(code['code'], 'update', 'FA', '历史行情', end, 'stock')


def update_all_index_trade(start):
    """
    更新指数
    调用频率 每周调用1次 或者每天1次
    :param start:
    :return:
    """
    today = date.date.today()
    ctrl.init_index_list()
    codes = ctrl.get_update_index_code_list()
    end = today.strftime("%Y-%m-%d")
    for code in codes:
        count = ctrl.update_index_data(code['code'], start, end)
        print(code['code'])
        if count > 0:
            log.logger(code['code'], 'update', 'OK', '历史行情', end, 'index')
        elif count == 0:
            log.logger(code['code'], 'update', 'ED', '历史行情', end, 'index')
        else:
            log.logger(code['code'], 'update', 'FA', '历史行情', end, 'index')


def update_stock_concept():
    """
    更新个股概念  用于分类
    调用频率 偶尔
    :return:
    """
    res = ify.update_stock_concept()
    print(res)


def update_stock_pca():
    """
    更新沪深指数成分股 用于分类
    调用频率 偶尔
    :return:
    """
    res = ify.update_stock_pca('hs300')
    print(res)
    res = ify.update_stock_pca('sz50')
    print(res)
    res = ify.update_stock_pca('zz500')
    print(res)


def update_stock_report(start, end):
    """
    更新财报
    调用频率 每季度
    :param start:
    :param end:
    :return:
    """
    pts = ['report', 'profit', 'operation', 'growth', 'debtpaying', 'cashflow']
    for o in pts:
        for i in range(start, end):
            for j in range(1, 5):
                res = rpt.update_stock_report(o, i, j)
                print(res)


def update_stock_forecast(start, end):
    """
    更新业绩预告
    调用频率 每季度
    :param start:
    :param end:
    :return:
    """
    for i in range(start, end):
        for j in range(1, 5):
            res = rpt.update_stock_forecast(i, j)
            print(res)


def update_stock_xsgjj(start, end):
    """
    更新限售股接近
    调用频率 每季度
    :param start:
    :param end:
    :return:
    """
    for i in range(start, end):
        for j in range(1, 13):
            res = rpt.update_stock_xsgjj(i, j)
            print(res)


def update_stock_jjcg(start, end):
    """
    更新基金持股
    调用频率 每季度
    :param start:
    :param end:
    :return:
    """
    for i in range(start, end):
        for j in range(1, 5):
            res = rpt.update_stock_jjcg(i, j)
            print(res)


def update_stock_winner(start_day, end_day):
    start = date.datetime.strptime(start_day,  "%Y-%m-%d")
    end = date.datetime.strptime(end_day,  "%Y-%m-%d")+date.timedelta(days=1)
    while True:
        if start.strftime("%Y-%m-%d") == end.strftime("%Y-%m-%d"):
            break
        else:
            print(start.strftime("%Y-%m-%d"))
            win.update_stock_winner(start.strftime("%Y-%m-%d"))
            start = start + date.timedelta(days=1)


main_7day()
#main_sometime()
