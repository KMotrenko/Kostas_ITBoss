from termcolor import colored

TaskNumber = ''

while TaskNumber != 0:
    
    TaskNumber = int(input('\nChoose the Task you want to check: \n\nPress 2 for Leap Year'''
    '''\nPress 3 for Factorial \nPress 4 for Simple Number '''
    '''\nPress 5 for Digits Summary \nPress 6 for Correct Finish '''
    '''\nPress 7 for Binary System \nPress 0 to EXIT: '''))

    if TaskNumber < 2 or TaskNumber > 7:
        print(colored('\nYou entered incorrect number. You need to be careful!', 'red'))

    if TaskNumber == 2:
        
        ## Task 2: Leap Year
        print('\nYou picked Task 1: Leap Year\n')
        year = int(input ('Enter year not more than 3000: '))

        if (year % 100 == 0) and (year % 400 == 0):
            print("\nIt's a Lip Year!\n")
        
        elif (year % 4 == 0) and (year % 100 != 0):
            print("\nIt's a Lip Year!\n")

        else: print("It's not a Lip Year!\n")

        print(colored("Task 2 is finished! Thank you!\n", 'magenta'))

    if TaskNumber == 3:

        ## Task 3: Factorial
        print('\nYou picked Task 3: Factorial\n')

        number = int(input('Enter any number, but not very big: '))
        factorial = 1
        
        for i in range(1,number+1):
            factorial = factorial * i
        
        print (colored(f"\nThe factorial of {number} is : {factorial}\n", "yellow"))
        print ("Task 3 is finished! Thank you!\n")


    if TaskNumber == 4:
        
        ## Task 4: Simple Number
        print('\nYou picked Task 4: Simple Number\n')

        number = int(input("Enter any number to check if it's Prime or not: "))

        if number > 1:
            for i in range (2, number):
                if (number % i) == 0:
                    print (f"\nNumber {number} is not Prime number!\n")
                    break
            else:
                print (f"\nNumber {number} is Prime number!\n")
        
        else: print (f"\nNumber {number} is not Prime number!\n")
        print (colored("Task 4 is finished! Thank you!\n", 'magenta'))


    if TaskNumber == 5:
        
        ## Task 5: Digits Summary
        print('\nYou picked Task 5: Digits Summary\n')

        number = abs(int(input("Enter any number for calculation: ")))
        summary = 0

        while number > 0:
            digit = number % 10
            if number != 0:
                summary = summary + digit
            number = number // 10
        
        print (colored(f"\nFor your number Summary is {summary}\n", "yellow"))

        print (colored("Task 5 is finished! Thank you!\n", 'magenta'))
            


    if TaskNumber == 6:
        
        ## Task 6: Correct Finish
        print ('\nYou picked Task 6: Correct Finish\n')

        number = abs(int(input("Enter any number to see correct word finish: ")))

        if number <= 0:
            print (colored("\nThe quantity of Ukrainians is always more than 0!\n", 'yellow'))

        elif number == 1:
            print (f"\n---{number} українець has killed {number} orc!---\n")

        elif (number % 10) == 1 and (number % 100) != 11 and number != 1:
            print (f"\n---{number} українець have killed {number} orcs!---\n")

        elif 2 <= (number % 10) <= 4 and (number % 100 < 10 or number % 100 > 20) :
            print (f"\n---{number} українця have killed {number} orcs!---\n")

        else:
            print (f"\n---{number} українців have killed {number} orcs!---\n")

        print (colored("Task 6 is finished! Thank you!\n", 'magenta'))



    if TaskNumber == 7:
        
        ## Task 7: Binary System
        print ('\nYou picked Task 7: Binary System\n')

        version = int(input("Type 1 to convert from Decimal to Binary or 2 to convert from Binary to Decimal: "))

        if version == 1:
            print ("\nYou've chosen Decimal-to-Binary version!\n")

            number = abs(int(input("Enter any number you need to be converted to Binary: ")))
            binary = ''
        
            if number == 0: print ("\nYou need to pick another number!")
            
            while number > 0:
                binary = str(number % 2) + binary
                number = number // 2
            
            print (f"\nYour number in Binary format will be: {binary}")

        if version == 2:
            print ("\nYou've chosen Binary-to-Decimal version!\n")

            number = input("Enter any number you need to be converted to Decimal: ")
            decimal = 0
            
            for i in number:
                decimal= decimal * 2 + int (i)

            print (f"\nYour number in Decimal format will be: {decimal}")
        
        print (colored("\nTask 7 is finished! Thank you!", 'magenta'))
else:
    print (colored("\nThank you for using my program!\n", 'red'))