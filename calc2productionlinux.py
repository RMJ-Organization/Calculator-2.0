print('Source code is online at https://github.com/RMJ-Organization/Calculator-2.0')

print('')
print('')

def version():
    print('Calculator 2.0 v1.0.4')

def stop():
    quit()
    
def calculate():
    version()
    print('Please do not enter two calculation types as it bugs the application')
    cd = input('What type of calculation do you want to preform today? * , / , +, -, square, inequality is all we accept: ')
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
    elif 'inequality' in cd:
        inequality()
    else:
        invalid() 
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
        exit()

def cal():
    version()
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
        invalid()
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
        exit()
        
def inequality():
    method = input("What is the inequality sign? > or < ? ")
    if ">" in method:
        num1 = int(input("What is the first parameter you put? ( THIS NUM > NEXT NUM ): "))
        num2 = int(input("What is the first parameter you put? ( LAST NUM > THIS NUM ): "))
        ans = num1 > num2
        print(f"The answer to {num1} > {num2} is {ans}.")
        print("")
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
        if 'y' in num3:
            calculate()
        elif 'Y' in num3:
            calculate()
        else:
            exit()
    elif "<" in method:
        num1 = int(input("What is the first parameter you put? ( THIS NUM < NEXT NUM ): "))
        num2 = int(input("What is the first parameter you put? ( LAST NUM < THIS NUM ): "))
        ans = num1 < num2
        print(f"The answer to {num1} < {num2} is {ans}.")
        print("")
        num3 = input('Do you want to calculate another number, press Y if you do so. If you want to exit the application, press any other key: ')
        print('')
        print('-----------------------------------------------------------------------------------------------------------------')
        print('')
        if 'y' in num3:
            calculate()
        elif 'Y' in num3:
            calculate()
        else:
            exit()
    else:
        invalid()
        
def invalid():
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
        

calculate() 
