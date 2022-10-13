from re import S
from termcolor import colored

while True:
    elem = input(colored("\nEnter any number for elements quantity or 'q' to Exit: ", 'magenta'))

    if elem == 'q':
            break
    elem = int(elem)
    ratio = int(input(colored("\nEnter any number for ratio: ", 'magenta')))

    print(colored(f"\nFor entered elements quantity {elem} and provided ratio {ratio}, progression would be:", 'green'))
    prev = 1
    curr = 1
    for i in range(1, elem+1):
        print(curr)
        curr = prev * ratio
        prev = curr


print(colored("\nThank you for using this program\n", 'cyan'))