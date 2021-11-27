def checkin (dict):
    entry=input("enter your capitals or country:-")
    if entry in dict:
            print("country:" + entry + '-capital-' + dict[entry])
    elif entry in dict.values():
        name = list(dict.keys())[list(dict.values()).index(entry)]
        print("country:"+name+"-capital-"+entry)
    else:
            print(' no such country or capital' + entry)
            add(dict)


def add (dict):
    entry=input("Enter Country:-")
    entry1= input("Enter Capital:-")
    dict.update({entry:entry1})
    print(dict)
    
def correction(dict):
    entry= input("Enter you would like to delete ")
    if entry in dict:
        dict.pop(entry)
        print("Make new entries")
        add(dict)
    elif entry in dict.values():
        name2 = list(dict.keys())[list(dict.values()).index(entry)]
        dict.pop(name2)
        print("Make new entries")
        add(dict)
    print(dict)
    
import random
def check(dict):
   correct_count=1
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
   prin(correct_count)
   total=5/correct_count*100 
   print("Procent of right answered",total)