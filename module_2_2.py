first = input('Введите первое число')
print('Первое число',first)
second = input('Введите второе число')
print('Второе число',second)
third = input('Введите третье число')
print('Третье число',third)

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)