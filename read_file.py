from sys import argv

script, filename = argv

print(f"I will read {filename} from {script}")

txt = open(filename)

print(txt.read())