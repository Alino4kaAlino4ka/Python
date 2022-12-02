# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


with open("test.txt", 'w', encoding='utf-8') as f:
    lst = '# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'
    f.write(lst)

with open("test.txt", 'r', encoding='utf-8') as fd:
    x = fd.read()


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


if __name__ == '__main__':
    print(x)
    my_text = del_some_words(x)
    print(my_text)

