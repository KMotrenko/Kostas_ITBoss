import termcolor as colored

input_name = input("Enter name: ")
input_age = input("Enter age: ")
input_profession = input("Enter profession: ")

person_dict = {"Name": input_name, "Age": input_age, "Profession": input_profession}

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    for key, value in person_dict.items(): 
        f.write('%s: %s\n' % (key, value))

f.close()