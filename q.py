import os
import re
import time

books_name = os.listdir('exclastxt')  #list of books

dicti=set()

ignore = ['a', "the", "is" , "an" , "am" , "and" , "are" ,"or","he","she" ,"for" , "you" ,"we" ,"they" , "of" , "to" , "in","not" , "this" , "that" , "it" , "as"]    

for book in books_name:
   print(book)
   f = open("exclastxt/"+ book, "r")
   words = re.sub("[^\w]", " ",  f.read()).split()  
   for w in words :
       if w.lower() not in ignore :
            dicti.add((w.lower(),book))

dicti=list(dicti)


posting={}

for a in dicti:
    if a[0] in posting.keys():
        posting[a[0]].append(a[1])
    else:
        posting[a[0]]=[a[1]]

t1 = time.perf_counter()
print("time of making posting list : ", t1)



while True:
    print("enter word (exit ==> $exit) : ")
    inp=input(">>")
    t2 = time.perf_counter()
    if (inp=="$exit"):
        print("Good bye...")
        break
    if inp in posting.keys():
        print("num of books : ",len(posting[inp]))
        print(posting[inp])
    else:
        print("not found!!")
    t3 = time.perf_counter()
    print("time of finding : ", t3-t2)





   