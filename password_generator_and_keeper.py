import random
from csv import DictWriter

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_of_pass = int(input('enter the length of password : '))
pass_list = random.sample(s,len_of_pass)
password = ''.join(pass_list)
print(password)

choice = input('do you want to save this password y / n')

database = {}

if choice == 'y' or choice == 'Y':
    acount_number = input('enter your acount : ')
    with open('acount_saver.txt','a',newline='') as f:
        # print(f"{acount_number} : {password} ",file=f)
        print('',file=f)
        csv_writing = DictWriter(f,fieldnames=['acount name','password'])
        csv_writing.writeheader()
        csv_writing.writerows([
            {'acount name':acount_number , 'password':password},
        ])


    

