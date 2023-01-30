names = {"1111" : "1234" , "2222" : "9191" , "3333" : "8585" , "4444" : "6969"} #names are numbers of card in real life / numbers are passwords
Profile = ["1111" , "sepehr" , "1234" , "263" , "1000" , "2222" , "Amir", "9191", "263", "5000"]
Bill_List = {"1234" : "50" , "4321" : "60" , "2394" : "20"}
LIST=[]

def withdrawal(assest, Assest_index):
    while True:
        mablagh = input("enter amount: (to go back enter -1)")
        if mablagh == "-1":
            return()
        elif mablagh.isdigit():
            if int(mablagh) > 200:
                print("you can't withdrawal more than 200$")
                continue
            mablagh = int(mablagh)
            assest = int(assest)
            x = mablagh % 10
            if x == 0 :
                if mablagh > assest:
                    print("mojodi kafi nist")
                    continue
                elif 0 < mablagh <= assest :
                    print("pool khodra bardarid")
                    newbalance = assest - mablagh
                    print(f"new balance : {newbalance}\n")
                    Profile[Assest_index] = str(newbalance)
                    assest = Profile[Assest_index]
                    a = input("1.Exit\n2.Return to menu\n")
                    if a.isdigit():
                        if a == "1":
                            print("be salamat :)"); quit()
                        elif a == "2":
                            return assest
                else:
                    print("enter correct amount")
                    continue
            else:
                print("enter correct amount")
                continue
        else:
            print("enter correct value")

def KartBeKart(assest, Assest_index):
    while True:
        secondcard = input("who do you want send to, enter its number: ( to go back enter 1)")
        if secondcard.isdigit():
            if names.get(secondcard):
                x = Profile.index(secondcard)
                owner_index2 = x + 1; Assest_index2 = x + 4
                owner2 = Profile[owner_index2]; assest2 = Profile[Assest_index2]
                while True:
                    INPUT = input(f"name : {owner2}\nto continue enter 'yes' | to change number enter 'no'\n(to go back enter 2 | to Exit enter 1)\n ")
                    if INPUT.isdigit():
                        if INPUT == "1":
                            print("be salamat :)"); quit()
                        elif INPUT == "2":
                            return
                        else:
                            print("enter corrrect value")
                            continue
                    elif INPUT == "no":
                        break
                    elif INPUT == "yes":
                        while True:
                            mablagh = input("enter amount: (to go back enter 2 | to Exit enter 1)")
                            if mablagh.isdigit():
                                if mablagh == "1":
                                    quit()
                                elif mablagh == "2":
                                    break
                                mablagh = int(mablagh)
                                assest = int(assest)
                                assest2 = int(assest2)
                                if mablagh > assest:
                                    print("mojodi kafi nist")
                                    continue
                                elif 0 < mablagh <= assest :
                                    newbalance = assest - mablagh           #card which sent
                                    print(f"new balance : {newbalance}\n")
                                    Profile[Assest_index] = str(newbalance)
                                    assest = Profile[Assest_index]
                                    assest2 = assest2 + mablagh             #card which recived
                                    Profile[Assest_index2] = str(assest2)
                                    print("successfully done")
                                    a = input("1.Exit\n2.Return to menu\n")
                                    if a.isdigit():
                                        if a == "1":
                                            print("be salamat :)"); quit()
                                        elif a == "2":
                                            return(assest)
                            else:
                                print("enter corrrect value")
                                continue
                        continue
                    else:
                        print("enter correct value")
                        continue
                continue
            elif secondcard == "1":
                return
            else:
                print("the entered card number doesn't exist")
                continue
        else:
            print("enter correct value")
            continue
def Bill(assest, Assest_index):
    while True:
        number_of_bill = input("Enter the number of bill : (Enter '1' to Exit)")
        if number_of_bill.isdigit():
            if Bill_List[number_of_bill]:
                print(f"your bill : {Bill_List[number_of_bill]} ")
                while True:
                    INPUT = input("1.Confirm\n2.change the number of bill\n3.go back\n4.Exit")
                    if INPUT.isdigit():
                        if INPUT == "1":
                            Bill = int(Bill_List[number_of_bill])
                            assest = int(assest)
                            if Bill > assest :
                                print("mojodi kafi nist")
                                continue
                            else:
                                newbalance = assest - Bill
                                Profile[Assest_index] = str(newbalance)
                                assest = Profile[Assest_index]
                                a = input("1.Exit\n2.Return to menu\n")
                                if a.isdigit():
                                    if a == "1":
                                        print("be salamat :)"); quit()
                                    elif a == "2":
                                        return assest
                        if INPUT == "2":
                            break
                        if INPUT == "3":
                            return
                        if INPUT == "4":
                            quit()
                    else:
                        continue
                continue
#def Admin():

def User():
    while True:
        insert = input("insert your card: (to Exit enter 1) ")
        if insert.isdigit():
            if insert == "1":
                print("be salamat :)"); quit()
            elif names[insert]:
                password = input("enter your password: (to Exit enter 1) ")
                if password.isdigit():
                    if insert == "1":
                        print("be salamat :)"); quit()
                    elif names[insert] == password :
                        x = Profile.index(insert)
                        owner_index = x + 1; passs_index = x + 2; cvv2_index = x + 3; Assest_index = x + 4
                        owner = Profile[owner_index]; passs = Profile[passs_index]; cvv2 = Profile[cvv2_index]; assest = Profile[Assest_index]
                        while True:
                            print(f"Welcome {owner}")
                            print("1.bardasht vajh\n2.integal vajh\n3.pardakht gabz + kharid sharzh\n4.mojodi\n5.Exit\n6.reenter card")
                            INPUT = input()
                            if INPUT.isdigit():
                                if INPUT == "1" :
                                    withdrawal(assest, Assest_index)
                                    assest = Profile[Assest_index]
                                    continue
                                if INPUT == "2" :
                                    KartBeKart(assest, Assest_index)
                                    assest = Profile[Assest_index]
                                    continue
                                if INPUT == "3" :
                                    Bill(assest, Assest_index)
                                if INPUT == "4":
                                    input(f"mojodi ghabele bardasht : {assest}\nPress Enter to continue")
                                if INPUT == "5":
                                    print("be salamat :)"); quit()
                                if INPUT == "6":
                                    break
                            else:
                              print("enter correct value")
                        continue
                    else:
                        print("wrong password")
                        continue
                else:
                    print("enter correct value")
                    continue
        else:
            print("enter correct value")

while True:
    Entrance = input("1.Admin\n2.User\n3.Exit\n")
    if Entrance.isdigit():
        if Entrance == "3":
            quit()
        if Entrance == "2":
            User()
        if Entrance == "1":
            Admin()
    print("Enter correct value")