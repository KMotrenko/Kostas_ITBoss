import termcolor as colored

year1 = input("Enter year of birth: ")
city1 = input("Enter city of birth: ")
nat1 = input("Enter nationality: ")
gender1 = input("Enter gender: ")

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    f.write(year1 + "     " + city1 + "     " + nat1 + "     " + gender1)

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='r') as f1:
    this_dict = {"Year": year1, "City": city1, "Nationality": nat1, "Gender": gender1}
    print(this_dict)


print("\nFile successfully edited!\n")

f.close()
