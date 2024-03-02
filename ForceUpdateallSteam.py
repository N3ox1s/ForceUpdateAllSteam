
import os

here = os.path.dirname(os.path.abspath(__file__))

#path = input("Enter Path to steamapps:")
if os.path.isfile(here + "\path.txt") is False:
    f = open("path.txt", "w")
    f.write(input("Enter Path to steamapps:"))
    f.close()

f = open(here + "\path.txt", "r")
path = f.read()
f.close()

print("searching in " + path)

def run_replace():
    for filename in os.listdir(path):
        if filename.startswith("appmanifest_"):
            with open(path + "/" + filename, "r") as file:
                content = file.read()
                with open(path + "/" + filename, "w") as f:
                    f.write(content.replace('\t"AutoUpdateBehavior"\t\t"0"\n', '\t"AutoUpdateBehavior"\t\t"2"\n'))

run_replace()
print("Done")
print("Press Enter to exit ...")
input()
