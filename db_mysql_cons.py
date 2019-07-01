"""
mysql数据库脚本配置
Created on 2018/05/14
@author: yudong chou
@contact: 33836858@qq.com
"""
import pymysql.cursors


def connection():
    con = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DB,
        charset=CHARSET,
        port=PORT,
        cursorclass=pymysql.cursors.DictCursor
    )
    return con


HOST = 'localhost'
USER = 'root'
PASSWORD = 'gigi117zyd'
DB = 'db_finance'
CHARSET = 'utf8mb4'
PORT = 3306

"""
日志记录
"""

DEL_HIS_T_LOGGER = ' delete from t_logger where operation = \'update\' ' \
                    'and lrrq< date_format(now(),\'%Y-%m-%d\')'

ISR_T_LOGGER = 'insert into `db_finance`.`t_logger` (`code`,`operation`,`description`,' \
               '`content`,`lrrq`,`ywlx`) values (%s,%s,%s,%s,%s,%s)'
###################################################################################################################

"""
处理股票列表
"""
DEL_T_CHN_STOCK_LIST = 'delete from `t_chn_stock_list`'

ISR_T_CHN_STOCK_LIST = 'insert into `t_chn_stock_list` (`code`,`name`,`industry`,`area`,`pe`,`outstanding`,`totals`,'\
              '`totalAssets`,`liquidAssets`,`fixedAssets`,`reserved`,`reservedPerShare`,`esp`,`bvps`,`pb`,'\
              '`timeToMarket`,`undp`,`perundp`,`rev`,`profit`,`gpr`,`npr`,`holders`)' \
              ' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '

QUE_T_CHN_STOCK_CODE_UPDATE_LIST = 'select `code` from `t_chn_stock_list` t where t.`code` not in ( ' \
                            'select `code`  from `t_logger` lo where  ' \
                            '1=1 and lo.`operation` = \'update\' ' \
                            'and lo.`description` in ( \'OK\',\'ED\') and ywlx=\'stock\'' \
                            ' and lrrq = date_format(now(),\'%Y-%m-%d\') )' \
                            ' order by `code`'

"""
处理股票交易
"""
DEL_T_CHN_STOCK_TRADES = 'delete from `t_chn_stock_trade` where code=%s and  datetime>= %s and datetime <= %s '

ISR_T_CHN_STOCK_TRADES = 'insert into `db_finance`.`t_chn_stock_trade` (`datetime`,`code`,`open`,' \
                        '`close`,   `high`,`low`,`vol`,`amount`,`tor`,`vr`,`ma5`,`ma10`,`ma20`,`ma60`)' \
                         ' values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

#########################################################################################################
"""
处理指数列表
"""
DEL_T_CHN_INDEX_LIST = 'delete from `t_chn_index_list`'

ISR_T_CHN_INDEX_LIST = 'insert into `t_chn_index_list` (`code`,`name`,`change`,' \
                       '`open`,`preclose`,`close`,`high`,`low`,`volume`,`amount`)' \
                       'values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
获取指数列表
"""
QUE_T_CHN_INDEX_CODE_UPDATE_LIST = 'select `code` from `t_chn_index_list` t where t.`code` not in ( ' \
                            'select `code`  from `t_logger` lo where  ' \
                            '1=1 and lo.`operation` = \'update\' ' \
                            'and lo.`description` in ( \'OK\',\'ED\') and ywlx=\'index\'' \
                            'and lrrq = date_format(now(),\'%Y-%m-%d\') )' \
                            ' order by `code`'


"""
处理指数数据
"""
DEL_T_CHN_INDEX_TRADES = 'delete from `t_chn_index_trade` where code=%s and  datetime>= %s and datetime <= %s '

ISR_T_CHN_INDEX_TRADES = 'insert into `db_finance`.`t_chn_index_trade` (`datetime`,`code`,`open`,' \
                        '`close`,`high`,`low`,`vol`,`amount`,`ma5`,`ma10`,`ma20`,`ma60`)' \
                         ' values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

#########################################################################################################
"""
概念
"""
DEL_T_CHN_STOCK_CONCEPT = 'delete from `t_chn_stock_concept`'

ISR_T_CHN_STOCK_CONCEPT = 'insert into `t_chn_stock_concept` (`code`,`name`,`c_name`)' \
                            'values (%s,%s,%s)'

"""
股指成分分类
"""
DEL_T_CHN_STOCK_PCA = 'delete from `t_chn_stock_pca` where c_name = %s'

ISR_T_CHN_STOCK_PCA = 'insert into `t_chn_stock_pca` (`date`,`code`,`name`,`weight`,`c_name`)' \
                       'values (%s,%s,%s,%s,%s)'


"""
财务报表 业绩报告
"""
DEL_T_CHN_STOCK_REPORT = 'delete from `t_chn_stock_report` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_REPORT = 'insert into `t_chn_stock_report` (`nd`,`jd`,`code`,`name`,`eps`,`eps_yoy`,' \
                         '`bvps`,`roe`,`epcf`,`net_profits`,`profits_yoy`,`distrib`,`report_date`)' \
                         ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
财务报表 盈利能力
"""
DEL_T_CHN_STOCK_PROFIT = 'delete from `t_chn_stock_profit` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_PROFIT = 'insert into `t_chn_stock_profit` (`nd`,`jd`,`code`,`name`,`roe`,' \
                         '`net_profit_ratio`,`gross_profit_rate`,`net_profits`,`esp`,' \
                         '`business_income`,`bips`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
财务报表 营运能力
"""
DEL_T_CHN_STOCK_OPERATION = 'delete from `t_chn_stock_operation` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_OPERATION = 'insert into `t_chn_stock_operation` (`nd`,`jd`,`code`,`name`,`arturnover`,' \
                         '`arturndays`,`inventory_turnover`,`inventory_days`,`currentasset_turnover`,' \
                         '`currentasset_days`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

"""
财务报表 成长能力
"""
DEL_T_CHN_STOCK_GROWTH = 'delete from `t_chn_stock_growth` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_GROWTH = 'insert into `t_chn_stock_growth` (`nd`,`jd`,`code`,`name`,`mbrg`,' \
                         '`nprg`,`nav`,`targ`,`epsg`,' \
                         '`seg`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
财务报表 偿债能力
"""
DEL_T_CHN_STOCK_DEBTPAYING = 'delete from `t_chn_stock_debtpaying` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_DEBTPAYING = 'insert into `t_chn_stock_debtpaying` (`nd`,`jd`,`code`,`name`,`currentratio`,' \
                         '`quickratio`,`cashratio`,`icratio`,`sheqratio`,' \
                         '`adratio`)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
财务报表 现金流量
"""
DEL_T_CHN_STOCK_CASHFLOW = 'delete from `t_chn_stock_cashflow` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_CASHFLOW = 'insert into `t_chn_stock_cashflow` (`nd`,`jd`,`code`,`name`,`cf_sales`,' \
                         '`rateofreturn`,`cf_nm`,`cf_liabilities`,`cashflowratio`' \
                         ')values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'


"""
财务报表 业绩预告
"""
DEL_T_CHN_STOCK_FORECAST = 'delete from `t_chn_stock_forecast` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_FORECAST = 'insert into `t_chn_stock_forecast` (`nd`,`jd`,`code`,`name`,`type`,' \
                         '`report_date`,`pre_eps`,`range`' \
                         ')values(%s,%s,%s,%s,%s,%s,%s,%s)'

#####################################################################################
"""
 限售股解禁
"""
DEL_T_CHN_STOCK_XSGJJ = 'delete from `t_chn_stock_XSGJJ` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_XSGJJ = 'insert into `t_chn_stock_XSGJJ` (`nd`,`jd`,`code`,`name`,`date`,' \
                         '`count`,`ratio`' \
                         ')values(%s,%s,%s,%s,%s,%s,%s)'


"""
 基金持股
"""
DEL_T_CHN_STOCK_JJCG = 'delete from `t_chn_stock_jjcg` where nd = %s and jd = %s'

ISR_T_CHN_STOCK_JJCG = 'insert into `t_chn_stock_jjcg` (`nd`,`jd`,`code`,`name`,`date`,' \
                         '`nums`,`nlast`,`count`,`clast`,`amount`,`ratio`' \
                         ')values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


####################################################################################
"""
龙虎榜
"""

DEL_T_CHN_STOCK_WINER = 'delete from `t_chn_stock_winer` where datetime = %s '

ISR_T_CHN_STOCK_WINER = 'insert into `t_chn_stock_winer` (`datetime`,`code`,`name`,`pchange`,' \
                         '`amount`,`buy`,`sell`,`reason`,`bratio`,`sratio`,`date`' \
                         ')values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


