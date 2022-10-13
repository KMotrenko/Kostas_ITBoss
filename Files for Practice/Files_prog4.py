import termcolor as colored

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

num = num1 + num2 + num3

with open("D:\Python related lessons\Files for Practice\one_file.txt", mode='w') as f:
    f.write(num[0] + num[1] + num[2] +'\n')
    f.write(num[0] + num[2] + num[1] +'\n')
    f.write(num[1] + num[2] + num[0] +'\n')
    f.write(num[1] + num[0] + num[2] +'\n')
    f.write(num[2] + num[0] + num[1] +'\n')
    f.write(num[2] + num[1] + num[0] +'\n')

print("\nFile successfully created!\n")

f.close()