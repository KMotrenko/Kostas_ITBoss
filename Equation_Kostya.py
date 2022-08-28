from termcolor import colored

equation = input ("Enter an equation starting with x: ")
equation.split(" ")
number_1 = equation[2]
operator = equation[1]
number_2 = equation[4]
argument = 0

def calc_add (number_1, number_2):
    return number_1 + number_2
def calc_sub (number_1, number_2):
    return number_1 - number_2
def calc_mult (number_1, number_2):
    return number_1 * number_2
def calc_div (number_1, number_2):
    return number_1 / number_2
def calc_floordiv (number_1, number_2):
    return number_1 // number_2
def calc_modulo (number_1, number_2):
    return number_1 % number_2

if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":

    if operator == "+":
        argument = calc_sub (number_2, number_1)

    elif operator == "-":
        argument = calc_add (number_1, number_2)

    elif operator == "*":
        argument = calc_div (number_2, number_1)

    elif operator == "/":
        if number_1 == 0:
            print (colored("\nNumber 1 can't be 0!", 'red'))
        argument = calc_mult (number_1, number_2)

    elif operator == "**":
        if number_1 != 2:
            print (colored("\nThat's not square function!", 'red'))
        else:
            argument = number_2 ** 0.5


    print (colored(f"\nx: {argument}", 'cyan'))

else:
    print (colored(f"\nThere's no such operator '{operator}'! You need to be careful!", 'red'))

print (colored ("\nDone\n", 'magenta'))