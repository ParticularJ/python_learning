from sys import argv

script, first, second, third = argv
a = input("the first you want to write ...")
b = input("the second ..,")
c  = input("teh third you ...")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is :", third)
print("{} {} {}".format(a,b,c))