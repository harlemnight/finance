import configparser
import cx_Oracle as orac
import pandas as pd
import xlsxwriter as xlw
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def main(filepath):
    cf = configparser.ConfigParser()
    cf.read(filepath, encoding='utf-8-sig') #chinese
    db_cfg = cf.items(section='db_config')
    db_dict = {i[0]: i[1] for i in db_cfg}
    user = db_dict['user']
    password = db_dict['pwd']
    connect = db_dict['connect']
    commit_row = db_dict['commit_row']
    db_type = db_dict['db_type']
    table_name = cf.get(section='sql', option='table_name')
    table_cols = cf.get(section='sql', option='table_cols')
    export_sql = cf.get(section='sql', option='export_sql')
    table_cols_comment = cf.get(section='sql', option='table_cols_comment')
    file_name = cf.get(section='file', option='file_name')
    xls_max_row = cf.get(section='sql', option='xls_max_row')
    sql = export_sql
    tab_col = []
    data = []
    if db_type == 'oracle':
        try:
            db_con = orac.connect(user, password, connect)
            rs = db_con.cursor()
            print('data is loading')
            rs.execute(sql)
            data = rs.fetchall()
            tab_col = [str(i[0]) for i in rs.description]
        except Exception as e:
            db_con.rollback()
            print(e)
        finally:
            db_con.commit()
            rs.close()
            db_con.close()
    elif db_type == 'mysql':
        print(1)
    else:
        print(2)
    print('data is writeing to file')
    num,n ,tabcomment,xlsx_row= 0,1,[],0
    if len(table_cols_comment) == 0:
        tabcomment = tab_col
    else:
        tabcomment = table_cols_comment.strip(',').split(',')
    if len(xls_max_row) == 0:
        xlsx_row = 1048575
    else:
        xlsx_row = xls_max_row
    workbook = xlw.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    worksheet.write_row('A1', tabcomment)
    sheet_row = 2
    for i in range(len(data)):
        row_num = i+1
        worksheet.write_row('A'+str(sheet_row), data[i])
        if int(row_num) % int(xlsx_row) == 0:
            worksheet = workbook.add_worksheet()
            worksheet.write_row('A1', tabcomment)
            sheet_row = 2
        else:
            sheet_row += 1
        if row_num % int(commit_row) == 0:
            print('writed ' + str(row_num))
    print('writed all the file is flushing')
    workbook.close()
    # pandas 性能太慢 skip follow
    # if len(table_cols_name) == 0:
    #     fm = pd.DataFrame(data)
    # else:
    #     fm = pd.DataFrame(data, columns=table_cols_name.strip(',').split(','))
    # fm.to_excel(file_name, index=False, encoding='utf-8')
    print('app end')


main('config.ini')