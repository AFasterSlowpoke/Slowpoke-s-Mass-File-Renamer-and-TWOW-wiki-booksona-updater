# ------------------------------
# importing modules
# ------------------------------
import os

# ------------------------------
# sub programs
# ------------------------------
def rename(original_name,new_name):
    for i in range(len(keys)):
        key = original_name[i]
        value = new_name[i]
        if os.path.exists(key) == True:
            os.rename(key, value)
            print("file renamed")
        else:
            print("file doesnt exist lol!!!")

# ------------------------------
# main program
# ------------------------------

keys = ["00001.png","00002.png","00003.png","00004.png"]
values = ["Bababnas.png","eggfucker1.png","nickel.png","Exampley.png"]

print(keys)
print(values)

options = ["normal","reverse"]
choice = ""

while choice.lower() not in options:
    choice = input("normal or reverse?")

choice = choice.lower()
if choice == "normal":
    rename(keys,values)
else:
    rename(values,keys)
