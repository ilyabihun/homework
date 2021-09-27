print('Welcome')
while True:
    x = float(input('Enter number'))
    symbol = input('Enter symbol')
    y = float(input('Enter number'))
    if symbol == '+':
        z = x + y
    elif symbol == '-':
        z = x - y
    elif symbol == '*':
        z = x * y
    elif symbol == '/':
        if y == 0:
            print('division by zero, try again')
            continue
        else:
            z = x / y
    else:
        print('Incorrect entry')
        continue
    symbol2 = input('Enter symbol')
    if symbol2 == '=':
        print(z)
        last_operation = (input('1.Try again\n 2.End'))
        if last_operation == '1':
            continue
        elif last_operation == '2':
            break
        else:
            print('Error')
            break
    elif symbol2== '+':
        '''тут я не понял как сохранить z с учетом continue и пожтому код незавершенный'''
    else:
        continue
