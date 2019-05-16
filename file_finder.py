import os

name = input('enter the name of your file  :  ')
path_of = input('enter the place or path of folder in which you want to search  :  ')

listing = os.walk(path_of)

if len(list(listing)) != 0:
    found_file = False
    for path_is,folder,file_name in listing:
        if name in file_name:
            found_file=True
            print(os.path.join(path_is,name))
        if not found_file:
            print('your file is not in this folder')

else:
    print('this folder does not exist')