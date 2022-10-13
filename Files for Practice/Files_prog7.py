import termcolor as colored

str1 = input("Enter any string: ")

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    f.write(str1)

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='r') as f1:
    line1 = f1.readline().strip()

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f2:
    f2.write(str1 + '\n')
    f2.write(line1.lower() + '\n')
    f2.write(line1.upper() + '\n')

print("\nFile successfully edited!\n")

f.close()
f1.close()
f2.close()