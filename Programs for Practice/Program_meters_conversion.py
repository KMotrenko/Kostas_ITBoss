from re import S
from termcolor import colored

while True:
    num = input(colored("\nEnter any number or 'q' to Exit: ", 'magenta'))

    if num == 'q':
            break
    
    sum_ariph = int((2*1 + 1*(int(num) - 1))*int(num) / 2)
    print(colored(f"\nFor entered last number {int(num)} of ariphmetic progression, Sum would be: {int(sum_ariph)}", 'green'))
    

print(colored("\nThank you for using this program\n", 'cyan'))