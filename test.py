#module
# import number
# print(number.a)
# print(number.b)
# print(number.a + number.b)

# import number 
# print ("hello", number.x, number.y, "and", number.wth)

#creating txt file, and writing
# file = open("text.txt", "w") #name of file
# x = file.write("this is a testing file, i want to tell you i hte you ")
# print(x)

#reading file 
# file =open ("text.txt", "r")
# x = file.read()
# print(x) # we can copy address location of that file, if it show error use double backslash 

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

# import pandas as pd
# data = {"name": ["Ali"], "score":[80]}
# df = pd.DataFrame(data)
# df.to_excel("data.xlsx", index= False)
# df = pd.read_excel("data.xlsx")
# print(df)