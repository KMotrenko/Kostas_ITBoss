from re import S
from termcolor import colored

while True:
    power = input(colored("\nEnter any number or 'q' to Exit: ", 'magenta'))

    if power == 'q':
            break
    for elem in range(1, 11):
        print(f"{elem} in {power} = {elem**int(power)}")


print(colored("\nThank you for using this program", 'cyan'))
