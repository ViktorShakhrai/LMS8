# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


# Простий калькулятор.
# Створіть функцію під назвою make_operation, яка приймає простий арифметичний оператор як перший параметр
# (щоб все було просто, нехай це буде лише «+», «-» або «*») і довільна кількість аргументів (лише числа) як другий параметр.
# Потім поверніть суму або добуток всіх чисел у довільному параметрі. Наприклад:
# виклик make_operation(‘+’, 7, 7, 2) повинен повернути 16
# виклик make_operation(‘-’, 5, 5, -10, -20) повинен повернути 30
# виклик make_operation(‘*’, 7, 6) повинен повернути 42


def make_operation(symbol_operation, *args):
    digit_list = []
    for i in args:
        digit_list.append(i)

    if symbol_operation == "+" and len(symbol_operation) != 0:
        rez = digit_list.pop(0)
        for i in digit_list:
            rez += i
        return rez
    elif symbol_operation == '-' and len(symbol_operation) != 0:
        rez = digit_list.pop(0)
        for i in digit_list:
            rez -= i
        return rez
    else:
        rez = digit_list.pop(0)
        for i in digit_list:
            rez *= i
        return rez


assert make_operation("+", 7, 7, 2) == 16
assert make_operation("-", 5, 5, -10, -20) == 30
assert make_operation("*", 7, 6) == 42
