# contestant list updater

# import modules
import pyperclip as pc
import os

# sub programs
def remove_placeholders(table):
    return wikitable.replace("|[[File:Placeholder.webp|50x50px]]", "")

# main program
wikitable = """
|Unranked
|[[File:Bababnas.png|50x50px]]Bababnas
|10
|Bababnas
|-
|16,608th
|[[File:Placeholder.webp|50x50px]]Exampley
|0
|Example
|}"""

lines = remove_placeholders(wikitable).splitlines()

for i in range(0,len(lines)//5):
    print(lines[(i*5)+2])
    if lines[(i*5)+2][:2] != "|[":
        print("needs an image!")
        image = "|[[File:"+lines[(i*5)+2]+".png|50x50px]] "
        image = image.replace("_", " ")
        lines[(i*5)+2] = image+lines[(i*5)+2]
    else:
        print("already has image")

print(lines)

wikitable = """
{}
""".format("\n".join(lines[1:])) # i stole this from stack overflow lol

print(wikitable)

print(wikitable)
pc.copy(wikitable)
