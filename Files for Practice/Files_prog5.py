import termcolor as colored

num1 = input("Enter your number divided with spaces: ")

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    f.write(num1)

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='r') as f1:
    line1 = f1.readline().strip()
    line = line1.split()
    print(line)


print("\nFile successfully edited!\n")

f.close()
f1.close()