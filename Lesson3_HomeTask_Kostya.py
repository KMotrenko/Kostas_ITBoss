from termcolor import colored

TaskNumber = ''

while TaskNumber != 0:
    
    TaskNumber = int(input('\nChoose the Task you want to check: \n\nPress 1 for Squares'''
    '''\nPress 2 for List Digits Summary \nPress 3 for Average Value '''
    '''\nPress 4 for Similar Strings \nPress 0 to EXIT: '''))

    if TaskNumber < 1 or TaskNumber > 4:
        print(colored('\nThank you! Bye!\n', 'red'))


    # Task 1. Squares

    if TaskNumber == 1:

        squares = []
        n = 10
        i = 1

        while i <= n:
            squares.append(i**2)
            print(squares)
            i += 1

    # Task 2. Summary

    if TaskNumber == 2:

        num_list = [12, -13, 98, 56, 34, -7, -56]
        n = len(num_list)
        i = 0
        summary = 0

    #   print (f"\nSummary of all digits in the list is: {sum(num_list)}\n")
        
        while i < n:
    #       print(num_list[i])
            summary = summary + num_list[i]
            i += 1
        
        print (colored(f"\nSummary of all digits in the list is: {summary}\n", 'magenta'))
            
    # Task 3. Average Value

    if TaskNumber == 3:
        
        num_list = [12, -13, 98, 56, 34, -7, -56]
        n = len(num_list)
        i = 0
        summary = 0

        while i < n:
            summary = summary + num_list[i]
            i += 1

        average = summary / n

        print ("\nAverage Value for provided list is: ", round(average, 4))
        
    # Task 4. Same Strings
    
    if TaskNumber == 4:

        string_1 = 'What is a beautiful weather!'
        string_2 = 'whAt is A beautiful Weather'
        string_3 = 'Slava Ukraini!'
        string_4 = 'Geroyam Slava!'
        string_5 = 'what is YOUR NAME?'
        string_6 = "i don't know"

        if (string_1.count('a') + string_1.count('A')) == (string_2.count('a') + string_2.count('A')):
            print (f"\nQuantity of 'a' letters in Strings 1 and 2 is same!\n")
        else:
            print (f"\nQuantity of 'a' letters in Strings 1 and 2 is different!\n")

        if (string_3.count('a') + string_3.count('A')) == (string_4.count('a') + string_4.count('A')):
            print (f"\nQuantity of 'a' letters in Strings 3 and 4 is same!\n")
        else:
            print (f"\nQuantity of 'a' letters in Strings 3 and 4 is different!\n")

        if (string_5.count('a') + string_5.count('A')) == (string_6.count('a') + string_6.count('A')):
            print (f"\nQuantity of 'a' letters in Strings 5 and 6 is similar!\n")
        else:
            print (f"\nQuantity of 'a' letters in Strings 5 and 6 is different!\n")