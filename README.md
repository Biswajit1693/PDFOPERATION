Python PDF library Operation
                    
                    
                    
    Reading & Extracting Text
    
   Python supports many libraries for extracting information from PDF files.One of the important library is PyPDF2.
   In order to read a pdf document in python we import the package PyPDF2.
           
           Syntax:
       
             import PyPDF2
             a=PyPDF2.PdfReader('sample.pdf')  # Reads the pdf into the python environment(Here pdf name is sample)
             print(a.getNumPages())            # Prints the number of pages in pdf
             page=a.pages[0]                   # selects and assigns the page into the variable 'page'
             print(page.extract_text())        # Prints the extracted text from the specified page in line 15
             
   Important Note-
     
   1. Whenever importing pdf its might show error-"file or directory not found".In that case make sure that the pdf is defined in your python environment.
   Its directory should be in your python file else it throws error most of the time.
   
   2.If copying the file path into the python code make sure to use "r" before the file path.It will convert the normal string into raw string
        
        Example-
         x='hello\nPython'
         Print(x)
         >>hello
         >>Python   #here the string will create a new line with backlash
         
         x=r'hello\nPython'
         print(x)
         >>hello\nPython  # here it treats the backlash as normal character so its prints the raw string as it is.
         
   3. While importing file into python code make sure to check the directory path and if there is any issues like these you can use 'r'.
   
   4. We can import pdf file from any directory but make sure to open the pdf first then use pdfreader.
        
        
              Example-
                 import PyPDF2
                 pdf_object=open(r"path","rb")  #need to mention "rb" for reader
                 z=PyPDF2.PdfReader(pdf_object)
            
         
         
         PDF FILE TO AUDIO
         
        Extracting text to speech in a pdf file
            
              Syntax:
              import PyPDF2                        # pdf importer
              import pyttsx3                       # text-speech library

              reader=PyPDF2.PdfReader("sample.pdf") # reads pdf file
              speak=pyttsx3.init()                  # to get a reference to a pyttsx3 for drivers support 2 voice m/f with help of “sapi5”      
              page=reader.pages[0]
              text=page.extract_text()              # extract text from page
              speak.say(text)                       # passes input taxt to be spoken
              speak.runAndWait()                    # it process the voice command
              speak.stop()                          # it stops the speech at the end of text
            
