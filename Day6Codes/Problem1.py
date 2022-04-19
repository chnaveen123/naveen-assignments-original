f = open("../data.txt", "w")

choice = "y"
nt = ""

while choice == "y":
    st = input("enter the content of the file :")

    nt = nt +" \n" + st

    choice = input("dou you want to continue Yes / No ")

f.write(nt)


f.close()