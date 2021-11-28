from module1 import*

Capitals={"Russia":"Moscow","Ukraine":"Kiev","Estonia":"Tallinn", "Latvia":"Riga","Germany":"Berlin","France":"Paris","Netherland":"Amsterdam","Belarus":"Minsk","Belgium":"Brussels","Austria":"Vienna","Finland":"Helsinki","Poland":"Warsaw"}

def menu():
        print("0-list dictionary\n1-check capital or country\n2-add to dictionary\n3-correct data,\n4-check your knowledge\n5-Quit")
        print( "Choose your number")
loop = 1
choice = 0
while loop == 1:
    menu()
    choice = int(input())
    if choice == 0:
       list1(Capitals)
    if choice == 1:
       checkin(Capitals)
    elif choice == 2:
       add(Capitals)
    elif choice == 3:
       correction(Capitals)
    elif choice == 4:
       check(Capitals)
    elif choice == 5:
        break
    else:
        print("Choose correct option")