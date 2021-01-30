import random

password_chars = "abXYZ123cdefGHJKgijkmnostwxyzABCDEFLMN678PQRSTW459pqr0"
all_password_chars =  "abXYZ123cdefGHJKgijkmn+?_&=!ostwxMN678PQRSTW459pqr0:,;.*$-%yzABCDEFL{}/"
loop = True



def generate(length, no_symbol):
    password = ""
    if(no_symbol):
        for x in range(int(length)):
            password += password_chars[random.randint(0,len(password_chars)-1)]
    else:
        for x in range(int(length)):
            password += all_password_chars[random.randint(0,len(all_password_chars)-1)]
    return password



while(loop):
    user_input = input("to creat a new password type 'password' to end type 'end': ")
    if(user_input == 'end'):
        loop = False
    elif(user_input == 'password'):
        user_input = input("type 'symbol' to get a password with symbols; type 'no' to get a password without symbolse; type 'back' to go back: ")
        if(user_input == 'symbol'):
            user_input = input("type password length: ")
            print(generate(user_input,False))
        elif(user_input == 'no'):
            user_input = input("type password length: ")
            print(generate(user_input,True))
        elif(user_input == 'back'):
            pass
        else:
            print("input was exepted")
    else:
        print("input was exepted")