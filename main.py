import Django


def summ(a,b):
    return a+b

def sub_nums(a,b):
    return a-b


def mul_nums(a,b):
    return a*b

def div_nums(a,b):
    return a/b

def main():
    num1 = int(input("Введите 1ое число: "))
    num2 = int(input("Введите 2ое число: "))
    oper = input("Укажите действие: ")
    if oper == '+':
        print(summ(num1, num2))
    elif oper == '-':
        print(sub_nums(num1, num2))
    elif oper == '*':
        print(mul_nums(num1, num2))
    elif oper == '/':
        print(div_nums(num1, num2))



if __name__ == '__main__':
    main()

