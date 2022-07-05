print('Welcome in calc')
print('type first number')
first = int(input())
print('type second number')
second = int(input())

print('You typed: first', first, ' and second:', second)
while 1 == 1:
    print('What do you want to calc')
    choice = int(input())
# 1 - addition, 2 subtraction 3 multiplying 4 dividing 5 powering 6 modulo
    if choice == 1:
        print('Addition ', first, '+', second, '=', (first+second))
    elif choice == 2:
        print('Subtraction ', first, '-', second, '=', (first-second))
    elif choice == 3:
        print('Multiplying ', first, '*', second, '=', (first * second))
    elif choice == 4:
        print('Dividing ', first, '/', second, '=', (first / second))
    elif choice == 5:
        print('Powering ', first, 'to power', second, '=', (first ** second))
    elif choice == 6:
        print('Modulo ', first, '%', second, '=', (first % second))

    print('You wand to continue?')
    shouldContinue = int(input())

    if shouldContinue == 0:
        print("Bye")
        break
    else:
        continue


