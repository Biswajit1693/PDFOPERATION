import PyPDF2
import pyttsx3

reader=PyPDF2.PdfReader("sample.pdf")
speak=pyttsx3.init()
page=reader.pages[0]
text=page.extract_text()
speak.say(text)
speak.runAndWait()
speak.stop()