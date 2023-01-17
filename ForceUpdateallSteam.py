import os

# Path to steamapps
path = "D:/games/Steam/steamapps/"


#path = input("Enter Path to steamapps:")
if os.path.isfile('./path.txt') is False:
    f = open("path.txt", "w")
    f.write(input("Enter Path to steamapps:"))
    f.close()

f = open("path.txt", "r")
path = f.read()
f.close()


def replace():
    for filename in os.listdir(path):
        if filename.startswith("appmanifest_"):
            with open(path + filename, "r") as file:
                content = file.read()
                with open(path + filename, "w") as f:
                    f.write(content.replace('\t"AutoUpdateBehavior"\t\t"0"\n', '\t"AutoUpdateBehavior"\t\t"2"\n'))


print("Done")
print("Press Enter to continue ...")
input()
