import PyPDF2
import pyttsx3
#a=PyPDF2.PdfReader(r"C:\Users\dell\PycharmProjects\BiswajitProject\sample.pdf")
a=PyPDF2.PdfReader("sample.pdf")
print(a.getNumPages())
speak=pyttsx3.init() # used for loading a speech engine driver implementation from the pyttsx3.drivers module
page=a.pages[0]
print(page.extract_text()) #extracted text from page 0
s=page.extract_text() #variable s to store extracted text
#print(s[::-1])
z=s[::-1] #store reverse text in z
print(z.strip())#removes all spaces from the string
speak.say(z)
speak.runAndWait()
speak.stop()