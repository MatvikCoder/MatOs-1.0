import time
import random
import sys
#Сама система
ram1 = '16 GB'
hdd = '1 TB'
print('loading OS...')
time.sleep(10);
print('Welcome to MatOS!')
while True:
    command = input('Введите команду: ')
    if command == 'help' :
        print('calculator - открыть калькулятор, help - все команды ОС, reset - выключение ОС, devs - разроботчики ОС, SYSinfo - Системная Информация, Pcinfo - Информация о компьютере');
    if command == 'calculator' :
        print(eval(input()));
    if command == 'reset' :
        sys.exit();
    if command == 'SYSinfo' :
        print('MatOS 1.0');
    if command == 'devs' :
        print('Разработчики:Колтунов Матвей. Всё:(');
    if command == 'PCinfo':
        print('ram: ' + ram1 + 'HDD Storage: ' + hdd + 'Intel CORE i5, NVIDIA Geforce GTX 1650.')
    
            
