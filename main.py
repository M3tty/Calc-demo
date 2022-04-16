def summ(a,b):
    return a+b


def main():
    num1 = int(input("Введите 1ое число: "))
    num2 = int(input("Введите 2ое число: "))
    oper = input("Укажите действие: ")
    if oper == '+':
        print(summ(num1, num2))



if __name__ == '__main__':
    main()

