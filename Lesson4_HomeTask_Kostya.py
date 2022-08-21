from termcolor import colored

TaskNumber = ''

while TaskNumber != 0:
    
    TaskNumber = int(input('\nChoose the Task you want to check: \n\nPress 3 for String Length'''
    '''\nPress 4 for Pyramid of Digits \nPress 5 for Odd or Even '''
    '''\nPress 6 for Secret Language \nPress 7 for Sieve of Eratosthenes '''
    '''\nPress 8 for Circular buffer \nPress 0 to EXIT: '''))

    if TaskNumber < 3 or TaskNumber > 8:
        print(colored('\nThank you! Bye!\n', 'red'))

    # Task 3. String Length
    
    if TaskNumber == 3:
        print('\nYou picked Task 3. String Length\n')

        your_string = input ('Enter any string: ')
        res = 0

        for i in your_string:
            res += 1
        
        if res == 1:
            print (f"\nThere's {res} symbol in your row!\n")

        else:
            print (f"\nThere're {res} symbols in your row!\n")

        print (colored(f"Simple check using len function: {len(your_string)} symbols!", 'yellow'))

    # Task 4. Pyramid of Digits
    
    if TaskNumber == 4:
        print('\nYou picked Task 4. Pyramid of Digits\n')

        print(colored('But I have no idea how to do it!\n', 'red'))

        rows = 4
        number = 0

        for i in range(1, 5):
            for spaces in range(1, i+1):
                print(" " * (rows-1), number, end = " ")
                number += 1
                rows -= 1
            print()


    # Task 5. Odd or Even
    
    if TaskNumber == 5:
        print('\nYou picked Task 5. Odd or Even\n')

        num_list = [3, 67, -56, 87, 63, 96, 101, 45, 66, 76, 53, 12, -11, 34]

        odd_count = 0
        even_count = 0

        for element in num_list:
            if element % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        print (colored(f"The count of even numbers is {even_count}", 'green'))
        print (colored(f"\nThe count of odd numbers is {odd_count}", 'magenta'))

    if TaskNumber >= 6 and  TaskNumber <= 8:

        print(colored("\nI have no idea how to do this task! It's too difficult!\n", 'red'))
