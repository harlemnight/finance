t = 'this is a string object'
a = t.count('a',8,9)
b = t.encode('GBK')
c = b.decode('UTF-8')
print(b)
print(c)

series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'01/18/2014 14:00:00', 120, '3rd'
"""
print(series)
import re
dt = re.compile("'[0-9/:\s]+'")
res = dt.findall(series)
print(res)


from datetime import datetime
pydt = datetime.strptime(res[0].replace("'","") ,'%m/%d/%Y %H:%M:%S' )
print(pydt)
print(type(pydt))