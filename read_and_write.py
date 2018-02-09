from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you don't want that , hit (^c)")
print(f"If you want that, hit RETURN")

input("?")

print("Openning the file ...")
# r for read , w for write ,a for append
# r+ w+ a+ for both read and write
target =  open(filename, 'w')

print("Truncating the file. Goodbye!" )
#target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#target.seek(0)
#target.write("TEST CK\n")
print("And finally, we close it.")
target.close()
