#import os
#import PyPDF2
#file_path = r'C:\Users\dell\Downloads\sample.pdf'
#print( os.path.isfile(file_path))

import PyPDF2
#a=PyPDF2.PdfReader(r"C:\Users\dell\PycharmProjects\BiswajitProject\sample.pdf")
a=PyPDF2.PdfReader("sample.pdf")
print(a.getNumPages())
page=a.pages[0]
print(page.extract_text())