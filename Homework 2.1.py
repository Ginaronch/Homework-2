print("Введите 4-значнное число:")
user_input = input()
int(user_input)
number1 = int(user_input)
print(number1 // 1000)
number2 = (number1 % 1000 // 100) #как я понял здесь можно было изспользовать divmod
number3 = (number1 % 100 // 10) #здесь также через divmod
number4 = (number1 % 10)
print(number2)
print(number3)
print(number4)

