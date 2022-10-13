import termcolor as colored

input_string = input("Enter anything you want to be placed to the file: ")

inp_str = input_string.split()

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    for word in inp_str:
        f.write(word+'\n')

f.close()