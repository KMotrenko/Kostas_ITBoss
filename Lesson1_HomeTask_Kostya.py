from termcolor import colored

TaskNumber = int(input('Choose the Task you want to check:\n\nPress 3 for Calculation Task,\nPress 5 for SelfPromotion,\nPress 6 for Herons Formula: '))

if TaskNumber != 3 and TaskNumber != 5 and TaskNumber != 6:
    print(colored('\nYou entered incorrect number. You need to be careful!', 'red'))

if TaskNumber == 3:
    
    ## Task 3: Calculations
    print('\nYou picked Task 3: Calculations\n')
    TaskVersion = input ('Choose Version of this Task: a , b or c: ')
    if TaskVersion == 'a':
        num_1 = 10
        num_2 = num_1 * 15.5
        num_3 = num_1 + num_2 * 0.5
        num_4 = 15 - num_3
        num_5 = 207.5 + abs(num_4)
        num_6 = num_5 / num_3
        print (f"\nIn this Version num_1 is {num_1} and Value in num_6 is {num_6}")

    if TaskVersion == 'b':
        anum_1 = 20
        anum_2 = anum_1 * 15.5
        anum_3 = anum_1 + anum_2 * 0.5
        anum_4 = 15 - anum_3
        anum_5 = 207.5 + abs(anum_4)
        anum_6 = anum_5 / anum_3
        print (f"\nIn this Version num_1 is {anum_1} and Value in anum_6 is {anum_6}")

    if TaskVersion == 'c':
        bnum_1 = 32
        bnum_2 = bnum_1 * 15.5
        bnum_3 = bnum_1 + bnum_2 * 0.5
        bnum_4 = 15 - bnum_3
        bnum_5 = 207.5 + abs(bnum_4)
        bnum_6 = bnum_5 / bnum_3
        print (f"\nIn this Version num_1 is {bnum_1} and Value in bnum_6 is {bnum_6}")

if TaskNumber == 5:

    ## Task 5: Selfpromotion
    print('\nYou picked Task 5: Selfpromotion\n')

    name = input ('Enter your name: ')
    city = input ('Enter the name of the city: ')
    colour = input ('Enter favourite colour: ')
    animal = input ('Enter favourite animal: ')
    friend = input ('Enter friends name: ')

    print(f'Hello! My name is {name}. I live in {city}. My favourite colour is {colour}. My favourite animal is {animal}. My friends name is {name}.\n')
    print(colored("Or you can see the same text in separate lines!\n", 'magenta'))
    print(f'Hello! My name is {name}.\nI live in {city}.\nMy favourite colour is {colour}.\nMy favourite animal is {animal}.\nMy friends name is {name}')

if TaskNumber == 6:

    ## Task 6: Heron's formula
    print("\nYou picked Task 6: Heron's formula\n")

    a = float(input('Enter first side length: '))
    b = float(input('Enter second side length: '))
    c = float(input('Enter third side length: '))
    if a < 0 or b < 0 or c < 0:
        print(colored("\nSides can't be less then zero!", 'red'))
    else:
        p = (a + b + c) / 2
        Area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

        print(f'\nThe Area of Triangle with provided sides is', Area)  

print(colored('\nHave a nice day, Olesya! Hope you like this program!', 'yellow'))