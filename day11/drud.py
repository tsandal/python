import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1807',
    charset='utf8'
)
cursor = conn.cursor()

#insert_dep1 = 'INSERT INTO departments VALUES(%s, %s)'
#hr = (1, 'hr')
#other_deps = [(2, '运维部'), (3, '开发部'), (4, '测试部')]
#cursor.execute(insert_dep1, hr)
#cursor.executemany(insert_dep1, other_deps)
#emps = [gw, hl, zs, zj, ws, zy, py, zzy, ll, bsf, xej]
#cursor.executemany(insert_emp, emps)
#query1='SELECT * FROM departments ORDER BY dep_id'
#cursor.execute(query1)
#cursor.scroll(2,mode='absolute')
#result=cursor.fetchone()
#print(result)
#print('-'*30)
#cursor.scroll(-2)
#result1=cursor.fetchone()
#print(result1)
query3='''SELECT e.emp_name,d.dep_name FROM employees AS e JOIN departments AS d ON e.dep_id=d.dep_id'''
cursor.execute(query3)
result=cursor.fetchall()
print(result)

cursor.close()
conn.close()
