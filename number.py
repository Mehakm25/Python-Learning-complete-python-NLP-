#integer = 1234567
#string = anything that comes between quotationmarks
#floats = numeric with points, decimal
#boolean = true and false
#arth operators =  + - * / // **
#list []
# tupple ()
# list is mutable , changeable
# tupple is not changeable / cant modify
# = is assignment operator 
# == is comparison opt

# x = 10
# y = 90
# print (x + y)
#string * integer = correct
#integer * string = correct and other arth opt = wrong

# x = "Mehak"
# y = "hello!" #string + string is concatencate, we can only add + , not other arth marks
# print (x + y)
# x = 5 
# print(5 < 10 )

#variable should be meaning full
#indexong starts from 0 ex: apple is 0
#indexing can only be in list 
# fruits =["apple","banana","mango", "guava"]
# print(type(fruits))
# fruits[1] = "orange" 
# print(fruits[-4])

# positive indexing starts from 0 ,1,2,4. left to right 
#negative indexing starts from guava right to left

# to check mutliple items, we will use tupple, to check one we will use
# fruits =("apple")
# # print(fruits[-2])
# # print(fruits[2])
# print(fruits[1:-1]) #ans is ppl
# print (fruits[-4:]) #to see whatever is after negative one. whole list

#dictionary doesnt contain duplaicate items {}
# dct = {
#     "name": "shoaib",
#      "CGPA": 3.9
#     }
# print(dct) #in dictionary we always have key and value , without key (name) code will show error. 
# dct = {
#     "name": "shoaib",
#      "CGPA": 3.9,
# "cgpa" : 3.5,
# "CGPA": 3.5, 
#     }
# print(dct)
# there are 5 lines of same key and value data, dic will print only once, it will not dupicate. 
#keys should be diff, value can remain same, if keys are diff, value are same it will only print once. 

# st = {1,2,3,4,5,4,2,23}
# st1 = {98,9,8,7,6,5,}
# print(st - st1) #we cant add, multply, only we can minus

#dict is mutable throughkey 
# dct = {
#     "name": "Shoaib",
#     "CGPA": 3.6,
#     "GPA": 3.6,
#     "Score": 3.6,
#     "Result": 3.6
#     }

# dct["CGPA"] = 3.5 #mutable through key 
# print(dct)

# username = "Mehak"
# password = 12345

# if username == "Mehak" and password == 1234:
#     print("successfully login")

# else: 
#     print("user not found") # here we can use boolean, like we used "and" both statement true , we can also use "or" in which one statement should be true

# num = 16
# if num % 2 == 0:
#     print("even num")

# elif num % 2 == 1:
#     print("odd num")

# else:
#     print("nothing")
    

# num = int(input("enter your number"))
# if num % 2 == 0:
#     print("even num")

# else:
#     print("nonot an even number")

# for num in range(16):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is not even")

# import nltk
# nltk.download('punkt')
# nltk.download ("wordnet")
# nltk.download("omw-1.4")
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer

# with open(".txt","r", encoding="utf-8") as file:
#     content = file.read()
#     #print(content)
# #text = "Hello this is a testing text for tokenization"
# #tokenize text
# words = word_tokenize(content)
# #lemmatizer
# lemmatizer = WordNetLemmatizer()
# # apply lemmatization
# lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
# print(lemmatized_words)

# a = 30 # we added this line to import data in test.py file 
# b = 5

# x = input("enter your name ")
# y = "you are loking good"
# wth = "today is clody weather"

#numpy
# import numpy as np
# x = np.array([1,2,3,4,5,6])
# print(x * 2 )

# from docx import document
# PendingDeprecationWarning
# add = Document.write("hello i am mehak", "w")
# x = Docx_paragraph

# doc = Document()
# doc.document_heading("Main Heading")
# doc.paragraphs("this is testing file")
# doc.save("d.docx")

# for p in doc.paragraphs:
#     print(doc)


# from docx import Document

# # Create a new document
# doc = Document()

# # Add a heading
# doc.add_heading("Main Heading", level=1)

# # Add paragraphs
# doc.add_paragraph("Hello, I am Mehak.")
# doc.add_paragraph("This is a testing file.")

# # Save the document
# doc.save("d.docx")

# # Print all paragraphs
# for p in doc.paragraphs:
#     print(p.text)

#excel file


# # list 
# mylist = ["one","two","three"] #indexing
# # print(mylist[0:]) #slicing
# # anotherlist = ["four"," five"]
# # newlist = mylist + anotherlist #concatenate
# # print(newlist)

# #mylist[1] = "mehak"  #we can change element in list 
# #print(mylist)

# mylist.append("six") # append used to add items in the list 
# print(mylist)

# mylist.append("ten")
# print(mylist)

# # pop used to remove the item from the list 
# mylist.pop() #it removes the last word
# print(mylist)

# mylist.pop(1) #if you want to remove from center or any indexing
# print(mylist)

# num_list = [1,4,3,2] 
# num_list.sort()  #for sorting list
# print(num_list)

# num_list.reverse() #to reverese the list 
# print(num_list)

#Dictionary

# my_dict = {"key1":"value1", "key2": "value2"}
# print(my_dict["key1"])

# prices_lookup = {"apple": '25euros', "banana":'30 euros', "oranges": '2 euros'}
# print(prices_lookup["apple"])

#d = {"K": 123, "k2": [0,1,2],"k3":{'insideKey':100}}
# print(d["k2"])
# print(d["k3"])
# print(d["k3"]["insideKey"])

#print(d["k2"][2]) #to check index 2 

# d = {"key1": ["a","b", "c" ]}
# mylist = d["key1"]
# letter = mylist[2]
# letter.upper()
# print(letter.upper())

d = {"k1":10, "k2":20} #to add new items in dictionary
# d["k3"] =30
# print(d)

# d["k1"] =30
# print(d)
# print(d.values()) #to print values
# print(d.items())  #to print items
x = 2
while x > 3:
    print("True")
    
