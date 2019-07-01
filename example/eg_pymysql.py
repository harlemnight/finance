# pymysql.Connect()参数说明
# host(str):      MySQL服务器地址
# port(int):      MySQL服务器端口号
# user(str):      用户名
# passwd(str):    密码
# db(str):        数据库名称
# charset(str):   连接编码
#
# connection对象支持的方法
# cursor()        使用该连接创建并返回游标
# commit()        提交当前事务
# rollback()      回滚当前事务
# close()         关闭连接
#
# cursor对象支持的方法
# execute(op)     执行一个数据库的查询命令
# fetchone()      取得结果集的下一行
# fetchmany(size) 获取结果集的下几行
# fetchall()      获取结果集中的所有行
# rowcount()      返回数据条数或影响行数
# close()         关闭游标对象
import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='gigi117zyd',
                             db='db_finance',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

        data = [('webmaster@python.org', 'very-secret',)]
        print(type(data))
        print(type(data[0]))
        print(data)
        cursor.executemany(sql , data )
        print('成功插入', cursor.rowcount, '条数据')
        connection.commit()
        #多条数据
        data = [('yes@python.org', 'very-secret',),('yes@python.org', 'very-secret',)]
        print(type(data))
        print(data)

        cursor.executemany(sql, data)
        print('成功插入', cursor.rowcount, '条数据')

        # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()
        sql = "delete from `users`  WHERE `id`=%s"
        print('删除id是：',cursor.lastrowid)
        cursor.execute(sql, (cursor.lastrowid,))

        connection.commit()
        # Read a single record
        sql = "SELECT `id`, `password` `bb` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        #result = cursor.fetchone()
        # result = cursor.fetchmany(3)

        for row in cursor.fetchall():
            # 注意int类型需要使用str函数转义
            print("id:%s" % row)
        #print(result)

        # 游标设置为字典类型
        cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
        r = cursor.execute("call p1()")
        connection.commit()
except Exception as e:
    connection.rollback()  #
    print('事务处理失败', e)
finally:
    cursor.close()
    connection.close()
    print('连接关闭')
    #
    # data = cursor.fetchall()
    # try:
    #     result = dict(data)
    # except:
    #     msg = 'SELECT query must have exactly two columns'
    #     raise AssertionError(msg)