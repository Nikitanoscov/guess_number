from random import randint

number = randint(1,100)

print('Угадайте число от 1 до 100.')

stop_porgram = False

while not stop_porgram:
    you_number = int(input('Введите число: '))
    if you_number > number:
        print('Ваше число больше. Попробуйте снова.')
    
    if you_number < number:
        print('Ваше число меньше. Попробуйте снова.')
    
    if you_number == number:
        stop_porgram = True


print('Поздравляем у вас хорошая интуиция.')
