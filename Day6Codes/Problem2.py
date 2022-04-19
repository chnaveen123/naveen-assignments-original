
import os

dir = os.getcwd()
print(f"dir :{dir}")

dir = "C:\Users\ nc67322\PycharmProjects\pythonProject\Day6"
os.chdir(dir)
print(os.getcwd())
print("-" * 40)

files = os.listdir()
# print(files)
lst = []
for file in files:
    if file.endswith(".py"):
        lst.append(file)

FL = open("C:\Users\nc67322\PycharmProjects\pythonProject\Day7\\data.txt", "w")
for file in lst:
    FL.write(file + " => " + str(os.path.getsize(file)) + "\n")
FL.close()