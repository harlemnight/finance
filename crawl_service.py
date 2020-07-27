"""
通过开源tushare接口从网络抓取证券数据
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import tushare as ts


def get_all_stock_list():
    """
        获取沪深上市公司上一个交易日基本情况
    """
    return ts.get_stock_basics()


def get_stock_by_code(code, start, end):
    """
        根据股票代码获取该股票历史行情
    """
    con = ts.get_apis()
    try:
        res = ts.bar(code,
                     conn=con,
                     freq='D',
                     start_date=start,
                     end_date=end,
                     ma=[5, 10, 20, 60],
                     factors=['vr', 'tor'],
                     retry_count=2)
        return res
    except Exception as e:
        print('抓取失败个股行情', e)
        return None
    finally:
        ts.close_apis(con)


def get_all_index_list():
    """
        获取沪深指数上一个交易日基本情况
    """
    return ts.get_index()


def get_index_by_code(code, start, end):
    """
        获取指数历史行情
    """
    con = ts.get_apis()
    try:
        res = ts.bar(code,
                     conn=con,
                     freq='D',
                     start_date=start,
                     end_date=end,
                     asset='INDEX',
                     ma=[5, 10, 20, 60],
                     factors=['vr', 'tor'],
                     retry_count=2)
        return res
    except Exception as e:
        print('抓取指数行情失败', e)
        return None
    finally:
        ts.close_apis(con)


def get_stock_concept():
    """
        获取股票概念
    """
    return ts.get_concept_classified()


def get_stock_hs300():
    """
        获取沪深300成份及权重
    """
    return ts.get_hs300s()


def get_stock_sz50():
    """
        获取上证50成份股
    """
    return ts.get_sz50s()


def get_stock_zz500():
    """
        获取中证500成份股
    """
    return ts.get_zz500s()


def get_stock_report(nd, jd):
    """
        获取业绩报告（主表）
    """
    try:
        res = ts.get_report_data(nd, jd)
        return res
    except:
        return None


def get_stock_profit(nd, jd):
    """
        获取盈利能力
    """
    try:
        res = ts.get_profit_data(nd, jd)
        return res
    except:
        return None

def get_stock_operation(nd, jd):
    """
        获取营运能力
    """
    try:
        res = ts.get_operation_data(nd, jd)
        return res
    except:
        return None


def get_stock_growth(nd, jd):
    """
        获取成长能力
    """
    try:
        res = ts.get_growth_data(nd, jd)
        return res
    except:
        return None


def get_stock_debtpaying(nd, jd):
    """
        获取偿债能力
    """
    try:
        res = ts.get_debtpaying_data(nd, jd)
        return res
    except:
        return None


def get_stock_cashflow(nd, jd):
    """
        获取现金流量
    """
    try:
        res = ts.get_cashflow_data(nd, jd)
        return res
    except:
        return None


def get_stock_forecast(nd, jd):
    """
        获取业绩预告
    """
    try:
        res = ts.forecast_data(nd, jd)
        return res
    except:
        return None


def get_stock_xsgjj(nd, yf):
    """
        获取限售股解禁
    """
    try:
        res = ts.xsg_data(nd, yf)
        return res
    except:
        return None


def get_stock_jjcg(nd, jd):
    """
        获取基金持股
    """
    try:
        res = ts.fund_holdings(nd, jd)
        return res
    except:
        return None


def get_stock_winner(datetime):
    """
        获取每日龙虎榜列表
    """
    try:
        res = ts.top_list(datetime)
        return res
    except:
        return None


def main():
    print('bac')

if __name__ == '__main__':
    #maoyan_example()
    print(get_all_index_list())
    # start = '2019-06-24'
    # end = '2019-07-12'
    # code = '600460'
    # print(get_stock_by_code(code, start, end))
