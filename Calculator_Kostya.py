from termcolor import colored

number_1 = float (input ("Enter first number: "))
operator = str (input ("\nEnter operation: "))
number_2 = float (input ("\nEnter second number: "))
result = 0

def calc_add (number_1, number_2):
    return number_1 + number_2
def calc_sub (number_1, number_2):
    return number_1 - number_2
def calc_mult (number_1, number_2):
    return number_1 * number_2
def calc_div (number_1, number_2):
    return number_1 / number_2
def calc_square (number_1, number_2):
    return number_1 ** number_2
def calc_floordiv (number_1, number_2):
    return number_1 // number_2
def calc_modulo (number_1, number_2):
    return number_1 % number_2

if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**" or operator == "//" or operator == "%":

    if operator == "+":
        result = calc_add (number_1, number_2)

    elif operator == "-":
        result = calc_sub (number_1, number_2)

    elif operator == "*":
        result = calc_mult (number_1, number_2)

    elif operator == "/":
        if number_2 == 0:
            print (colored("\nNumber 2 can't be 0!", 'red'))
        result = calc_div (number_1, number_2)

    elif operator == "**":
        if number_2 != 2:
            print (colored("\nThat's not square function!", 'red'))
        else:
            result = calc_square (number_1, number_2)

    elif operator == "//":
        if number_2 == 0:
            print (colored("\nNumber 2 can't be 0!", 'red'))
        result = calc_floordiv (number_1, number_2)

    elif operator == "%":
        if number_2 == 0:
            print (colored("\nNumber 2 can't be 0!", "red"))
        result = calc_modulo (number_1, number_2)

    print (colored(f"\n{number_1} {operator} {number_2} = {result}", 'cyan'))

else:
    print (colored(f"\nThere's no such operator '{operator}'! You need to be careful!", 'red'))

print (colored ("\nDone\n", 'magenta'))