import PyPDF2
pdf_object=open(r"C:\Users\dell\Downloads\test.pdf","rb")#need to mention "rb" for reader
z=PyPDF2.PdfReader(pdf_object)
print(z.getNumPages())