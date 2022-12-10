# Задача: Создать информационную систему, позволяющую работать с сотрудниками некой
# компании \ студентами вуза \ учениками школы.
# Иванов Петр инженер з/п премия
# 1 добавление сотрудника
# 2 посмотреть всех сотрудников
# 3 найти сотрудника по фамилии
# 4 найти по должности
# 5 изменить зарплату
# 6 общий фонд з/п
import json
import csv
import sqlite3
# s1 = ['Иванов Петр', 'инженер', 55555, 33333]
staff = [{'id': 1,
          'name': 'Петр',
          'last_name': 'Иванов',
          'position': 'инженер',
          'salary': 55555,
          'bonus': 33333},
         {'id':2,
          'name': 'Петр',
          'last_name': 'Петров',
          'position': 'инженер',
          'salary': 55555,
          'bonus': 33333},
         ]

# x = json.dumps(staff, indent=2)
# print(x)
# # d = open('file.txt', 'w', encoding='utf-8')
# # d.close()
# with open('staff.json', 'w', encoding='utf-8') as fd:
#     # fd.write(json.dumps(staff, indent=2))
#     json.dump(staff, fd, indent=2)
#
# with open('staff.json', 'r', encoding='utf-8') as fd:
#     res = json.load(fd)
#
# print(res)
# # encoding='cp1251'
# with open('staff.csv', 'w', encoding='utf-8') as fd:
#     csv_file = csv.writer(fd)
#     # csv_file.writerows(staff)
#     for i in staff:
#         csv_file.writerow(i.values())
#
# with open('staff.csv', 'r', encoding='utf-8') as fd:
#     csv_res = csv.reader(fd)
#     for i in csv_res:
#         print(i)

con = sqlite3.connect('my.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS staff(id, name, last_name, position, salary, bonus);')
cur.execute('INSERT INTO staff (id, name, last_name, position, salary, bonus) VALUES (1, "Иван", "Петров", "инженер", 50000, 30000);')
cur.execute('INSERT INTO staff (id, name, last_name, position, salary, bonus) VALUES (2, "Иван", "Иванов", "инженер", 50000, 30000);')
res_all = cur.execute('SELECT * FROM staff;')
res = res_all.fetchall()
print(res)
# salary_all = cur.execute('SELECT salary, bonus FROM staff WHERE id = 1;')
salary_all = cur.execute('SELECT salary, bonus FROM staff;')
print(salary_all)
# print(salary_all.fetchone())
# print(salary_all.fetchone())
# print(salary_all.fetchmany(2))
print(salary_all.fetchall())
con.close()
# DBeaver Community https://dbeaver.io/
# sqlite studio https://sqlitestudio.pl/