def list1(dict):
    for key, value in dict.items():
        print(key, ' : ', value)

def checkin (dict):
    entry=input("Enter your capitals or country:-")
    if entry in dict:
            print("country:" + entry + '-capital-' + dict[entry])
    elif entry in dict.values():
        name = list(dict.keys())[list(dict.values()).index(entry)]
        print("country:"+name+"-capital-"+entry)
    else:
            print('No such country or capital:-' + entry)
            answer=input("Please enter Y (To add), N(To quit),C(To correct) :-")
            if answer.lower()=="y": 
                add(dict)
            elif answer.lower()=="c":
                correction(dict)
            else:
               return None

def add (dict):
    entry=input("Enter Country:-")
    entry1= input("Enter Capital:-")
    dict.update({entry:entry1})
    list1(dict)
    
def correction(dict):
    list1(dict)
    entry= input("Enter what would  you like to delete ")
    if entry in dict:
        dict.pop(entry)
        print("Deleted-Please make new entries")
        add(dict)
        print("Added")
    elif entry in dict.values():
        name2 = list(dict.keys())[list(dict.values()).index(entry)]
        dict.pop(name2)
        print("Deleted-Please make new entries")
        add(dict)
        print("Added")
    else:
        print("no such country in the dictionary")
        answer=input("Would you like to add it y/n:-")
        if answer.lower()=="y": 
                add(dict)
        else:
               return None
    
    
import random
def check(dict):
   correct_count=0
   print("enter 1 to  check capital, enter 2 to  check country")
   valik=input()
   if valik.lower()=="1":
     for k in range (5):
         x=random.choice(list(dict.values()))
         print(x)
         y_answer=input("Write your answer-")
         name = list(dict.keys())[list(dict.values()).index(x)]
         print(name)
         if name.lower()==y_answer.lower():
              print("correct")
              correct_count+=1   
         else:
                print("wrong")
                print(x,"-->",name)
   if valik.lower()=="2":
       for k in range (5):
        x=random.choice(list(dict.keys()))
        print(x)
        name=dict[x]
        y_answer=input("Write your answer-")
        if name.lower()==y_answer.lower():
                    print("correct")
                    correct_count+=1                
                 
        else:
                    print("wrong")
                    print(x,"-->",name)
   print(correct_count)
   total=(correct_count/5)*100 
   print("Procent of right answered",total)