This program was made for the TWOW Miraheze wiki, to quickly rename booksona images from numbers to their usernames, and to update the "List of EWOW Contestants Beginning with" quickly. If you aren't a TWOW wiki editor, this likely won't be much use to you, but you can fork it to suit your use if you know how to!

Made 100% with Python but GitHub doesn't show that for some reason.

Instructions:
1. Download the ZIP file on Github, and once it is installed, unzip the file.
2. If you did not install Python, install a version of Python that is version 3.12 or higher. During installation, make sure to select "Add Python to PATH" to make installing modules/libraries easier.
3. In the command prompt, type "pip install pyperclip" and "pip install os" to install the modules. If you didn't add Python to PATH, this will be more complicated.
4. I'd recommend opening rename.py in IDLE and running it to see if it works correctly.
5. Download the EWOW booksonas folder at https://mega.nz/file/9NtkDaAD#Zugp1jTybYblTLdEygWoE71SyXsxUcPmcIzeiQaiJfc and unzip the booksona folder.
6. Open the contestant names file and find what booksonas you want to rename. For example, if I wanted to rename all contestants beginning with A, it would be line 220 (a) to line 1228 (Aùțũmņ).
7. In explorer, shift-click on the file 00219.png then scroll down and shift-click on the file 01227.png (the numbers have to be offsetted by -1, as the files start with 00000.png) and copy them into my file renamer folder. Then, delete the old files that were there.
8. Copy all the contestant names you want to convert, and put them in https://arraythis.com/ . Make sure to select "Yes" to numbers in quotes, and copy the "[ javascript ] var array_name = [ python ] list_name =" output.
9. Right-click on "oh fuck i forgot to suffix png", click "More options" (on windows 11), and click "Edit with IDLE". Replace "the_list" with the output from arraythis. (Example: the_list = ["your","output","here"])
10. Save the file and run the script. If it works correctly, it will have copied the output to your clipboard.
11. Right-click on "rename", click "More options" (on windows 11), and click "Edit with IDLE". Replace "values" with the output copied from "oh fuck i forgot to suffix png". (Example: values = ["your.png","output.png","here.png"])
12. Run "list maker", and input the start and end numbers (e.g. 219 and 1227). This will copy a list of the non-converted booksona image names to your clipboard.
13. Edit "rename" again, and replace "keys" with the output copied from "list maker". (Example: keys = ["00001.png","00002.png","00003.png","00004.png"])
14. Run "rename" and type in "normal". If Python runs into a username with invalid characters \ / < > : ? * " | and/or runs into a duplicate name (e.g. "Exampley" and "EXamPLeY"), it will run into an error. Simply rename the offending value in values, and run the script again.
15. Upload all of the converted name images at https://twow.miraheze.org/wiki/Special:BatchUpload . It can only upload up to 25 images at a time, so upload the booksona images at 25-image batches.
16. Now click edit source on the EWOW contestant list you want to update (e.g https://twow.miraheze.org/wiki/List_of_EWOW_Contestants_Beginning_with_A ) and click edit source. Select the first |- all the way to the closing |} and copy it.
17. Open "placeholder killer" in IDLE and paste the wikitable. Make sure the first |- is on the very first line of the string "wikitable" (wikitable = """|- ). Now run the script. It will copy the output to your clipboard.
18. Go back onto the wiki page and paste in the output. It will remove the first |- for some reason, so make sure to add it back. Preview the page before publishing changes so you don't break anything!
19. hopefully everything worked! if it didn't, then ask for help in the TWOW wiki Discord or DM me on Discord (afasterslowpoke).
