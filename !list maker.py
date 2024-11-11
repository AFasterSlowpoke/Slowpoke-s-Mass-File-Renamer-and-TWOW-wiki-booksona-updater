# creates list

# ------------------------------
# importing modules
# ------------------------------
import pyperclip as pc

# ------------------------------
# sub programs
# ------------------------------
def number_to_filename(number):
    number = str(number)
    match len(number):
        case 1:
            number = "0000"+number+".png"
        case 2:
            number = "000"+number+".png"
        case 3:
            number = "00"+number+".png"
        case 4:
            number= "0"+number+".png"
        case 5:
            number = number+".png"
        case 6:
            number = "dumas cat.png"
    return number

# ------------------------------
# main program
# ------------------------------
the_list = []
start = int(input("input start number: "))
end = int(input("input end number: "))

for i in range(start, end+1):
    the_list.append(number_to_filename(i))
    print(i)
    
print(the_list)
pc.copy(the_list)
