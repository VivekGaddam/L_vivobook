# import sqlite3
# connect=sqlite3.connect('Mydb')
# cursor=connect.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS student(
#                Roll INT PRIMARY KEY,
#                Name VARCHAr(50)
#                );
# ''')
# cursor.execute('''SECLECT AVG(Salary) from employee where department''')
# record=[
#     (12,'vivek'),
#     (88,'kushi')
# ]
# cursor.execute('INSERT INTO student values (?,',record)
# connect.commit()
# connect.close()


import matplotlib.pyplot as plt
fig, a = plt.subplots(1, 4)
a[0].bar(x=['a','b','c'], height=[1, 2, 3])
a[1].bar(x=['a','b','c'], height=[2, 4, 3])
a[2]=plt.plot([1,2,3,4],[1,2,3,4])
a[3].hist([10,20,30])
plt.show()