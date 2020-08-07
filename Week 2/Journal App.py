accountsappusernames = {}
accountsapppasswords = {}
account1 = []
account2 = []
while True:
    login = input("do you want to log in or create account: ")
    if login == "login":
        username = input("enter your username: ")
        password = input("enter your passsword: ")
        if (username in accountsappusernames)  and (password in accountsapppasswords) :
            print("you have logged in")
            read = input("do you want to read entries or make: ")
            if read == "make":
                journal = input("enter your entry: ")
                if list(accountsappusernames).index(username) == 0 and list(accountsapppasswords).index(password) == 0:
                    account1.append(journal)
                else:
                    account2.append(journal)
            elif read == "read":
                if list(accountsappusernames).index(username) == 0 and list(accountsapppasswords).index(password) == 0:
                    for x in account1:
                        if x == '':
                            print("you have no entries")
                        else:
                            print(x)
                else:
                   for x in account2:
                        if x == '':
                            print("you have no entries")
                        else:
                            print(x)
            else:
                print("not an option")
        else:
            print("that is not correct \nyou are trying to break in!")
    elif login == "create":
        print("lets make your account")
        usernamec = input("enter your username: ")
        passwordc= input("enter your passsword: ")
        if usernamec in accountsappusernames or passwordc in accountsapppasswords:
            print("that account is taken")
        else:
            accountsappusernames[usernamec] = usernamec
            accountsapppasswords[passwordc] = passwordc
    elif login == "q":
        break
    else:
        print("that is not an option")
