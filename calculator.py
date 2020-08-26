print('Source code is online at https://github.com/RMJ-Organization/Calculator-2.0')

import os
os.system("title Calculator 2.0 by RMJ")

print('')
print('')



def calculate():
    print('Calculator 2.0 v1.0.2')
    print('Please do not enter two calculation types as it bugs the application')
    cd = input('What type of calculation do you want to preform today? * , / , +, -, square is all we accept: ')
    if 'square' in cd:
        numsquare = int(input('What Number are you squaring? '))
        ct = numsquare * numsquare
    elif '*' in cd:
        num1 = int(input('What number are you multiplying: '))
        num2 = int(input('What number are you multiplying to the other number: '))
        iden = ('*')
        ct = num1 * num2
    elif '/' in cd:
        num1 = int(input('What number are you dividing: '))
        num2 = int(input('What number are you dividing to the other number: '))
        iden = ('/')
        ct = num1 / num2
    elif '+' in cd:
        num1 = int(input('What number are you adding: '))
        num2 = int(input('What number are you adding to the other number: '))
        iden = ('+')
        ct = num1 + num2
    elif '-' in cd:
        num1 = int(input('What number are you subtracting: '))
        num2 = int(input('What number are you subtracting to the other number: '))
        iden = ('-')
        ct = num1 - num2
    else:
        print('Your requested calculation type was invalid.')
        num3 = input('Press y to calculate again or press any other key to exit: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
        if 'y' in num3:
            cal()
        elif 'Y' in num3:
            cal()
        else:
            stop() 
    if 'square' in cd:
        print(f'The question you requested was {numsquare} times {numsquare}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '*' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '/' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '+' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '-' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    if 'y' in num3:
        cal()
    elif 'Y' in num3:
        cal()
    else:
        stop()

def cal():
    print('Calculator 2.0 v1.0.2')
    print('Please do not enter two calculation types as it bugs the application')
    cd = input('What type of calculation do you want to preform today? * , / , +, -, square is all we accept: ')
    if 'square' in cd:
        numsquare = int(input('What Number are you squaring? '))
        ct = numsquare * numsquare
    elif '*' in cd:
        num1 = int(input('What number are you multiplying: '))
        num2 = int(input('What number are you multiplying to the other number: '))
        iden = ('*')
        ct = num1 * num2
    elif '/' in cd:
        num1 = int(input('What number are you dividing: '))
        num2 = int(input('What number are you dividing to the other number: '))
        iden = ('/')
        ct = num1 / num2
    elif '+' in cd:
        num1 = int(input('What number are you adding: '))
        num2 = int(input('What number are you adding to the other number: '))
        iden = ('+')
        ct = num1 + num2
    elif '-' in cd:
        num1 = int(input('What number are you subtracting: '))
        num2 = int(input('What number are you subtracting to the other number: '))
        iden = ('-')
        ct = num1 - num2
    else:
        print('Your requested calculation type was invalid.')
        num3 = input('Press y to calculate again or press any other key to exit: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
        if 'y' in num3:
            calculate()
        elif 'Y' in num3:
            calculate()
        else:
            stop()
    if 'square' in cd:
        print(f'The question you requested was {numsquare} times {numsquare}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '*' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '/' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '+' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    elif '-' in cd:
        print(f'Your question was {num1} {iden} {num2}.')
        print(f'The answer is   {ct}    !')
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
    if 'y' in num3:
        calculate()
    elif 'Y' in num3:
        calculate()
    else:
        stop()

calculate() 
 
def stop(): 
    print('Stopping Application')
