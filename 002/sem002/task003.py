# 3.Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

m_str = "мама мыла раму"
n_str = "ма"
res = 0
for i in m_str:
    if i == n_str:
        res+=1
# print(res) 
print(m_str.count(n_str))
