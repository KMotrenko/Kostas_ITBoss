from re import S
from termcolor import colored

while True:
    temp1 = input(colored("\nEnter number and 'K', 'F' or 'C' divided with space or 'q' to Exit: ", 'magenta'))

    if temp1 == 'q':
            break
    temp2 = temp1.split()
    if temp2[1] == "C":
       print(colored(f"\nFor entered temperature {temp1}:\n-> in Fahrenheit it would be {float(temp2[0])*1.8+32}\n-> in Kelvin it would be {float(temp2[0])+float(273.15)}", 'green')) 
    if temp2[1] == "K":
       print(colored(f"\nFor entered temperature {temp1}:\n-> in Fahrenheit it would be {(float(temp2[0])-273.15)*1.8+32}\n-> in Celsius it would be {float(temp2[0])-float(273.15)}", 'green'))
    if temp2[1] == "F":
       print(colored(f"\nFor entered temperature {temp1}:\n-> in Celsius it would be {(float(temp2[0])-32)*0.555}\n-> in Kelvin it would be {(float(temp2[0])-32)*0.555+float(273.15)}", 'green'))

print(colored("\nThank you for using this program\n", 'cyan'))