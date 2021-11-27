from module1 import*

Capitals={"Russia":"Moscow","Ukraine":"Kiev","Estonia":"Tallinn", "Latvia":"Riga","Germany":"Berlin","France":"Paris"}

def menu():
        print( "Choose your option")
loop = 1
choice = 0
while loop == 1:
    menu()
    choice = int(input())
    if choice == 1:
       entry=input("enter your capitals or country:-")
       check(Capitals,entry)
    elif choice == 2:
      add(Capitals)
    elif choice == 3:
        correction(Capitals)
    elif choice == 4:
        check(Capitals)
    elif choice == 5:
        break