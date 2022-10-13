from re import S
from termcolor import colored

while True:
    num = input(colored("\nEnter any number or 'q' to Exit: ", 'magenta'))

    if num == 'q':
            break
    
    print(colored(f"\nEntered number {int(num)} of meters would be {int(num)*1e+9} nanometers", 'green'))
    print(colored(f"Entered number {int(num)} of meters would be {int(num)*1e+6} micrometers", 'green'))
    print(colored(f"Entered number {int(num)} of meters would be {int(num)*1e+2} centimeters", 'green'))

print(colored("\nThank you for using this program", 'cyan'))