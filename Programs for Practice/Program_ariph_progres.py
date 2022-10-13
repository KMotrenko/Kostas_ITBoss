from re import S
from termcolor import colored

while True:
    num = input(colored("\nEnter any number or 'q' to Exit: ", 'magenta'))

    if num == 'q':
            break
    num = int(num)
    step = 1
    first_element = 1
    ariph_sum = num * (2 * first_element + step * (num - 1)) / 2

    print(colored(f"\nFor entered number {num}, Sum of ariphmetic progression would be: {ariph_sum}", 'green'))


print(colored("\nThank you for using this program\n", 'cyan'))