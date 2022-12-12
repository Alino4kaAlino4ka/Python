
import  model 
import view

def menu():
    while True:
        user_choise = view.type_nums()
        if user_choise == '1':
            a, b = complex_nums()        
        elif user_choise == '2':
            a, b = int_nums()
        elif  user_choise == 'q':
            print('До свидания')
            break
        oper = view.get_operation()
        model.init(a, b)
        if oper == '+':
            result = model.summ()
        elif oper == '-':
            result = model.sub()
        elif oper == '*':
            result = model.mult()
        elif oper == '/':
            result = model.div()

        view.view_data(result, "resul")


def complex_nums():
    value_a = view.get_complex_value()
    value_b = view.get_complex_value()
    return value_a, value_b

def int_nums():
    value_a = view.get_value()
    value_b = view.get_value()
    return value_a, value_b




    