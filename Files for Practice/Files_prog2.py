import termcolor as colored

input_string = input("Enter any string you want to be placed to the file: ")

inp_str = set(input_string)

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    for symbol in inp_str:
        f.write(symbol+'\n')

f.close()