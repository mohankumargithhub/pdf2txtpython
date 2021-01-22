#Developed by Mohan kumar
#    step1 (mandatory) pip install pyPDF2 and pip install urllib2


import PyPDF2       
import urllib2
import os

pdfFileObj = open('example.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
noofpages=pdfReader.numPages
textfile=""
for x in range(noofpages) 
	pageObj = pdfReader.getPage(noofpages)    
	textfile=textfile+pageObj.extractText()    
pdfFileObj.close() 



#upload the file into temp folder  temporarily to allow users to download

f = open("/temp/pdt2txtconverted.txt", "w")
f.write(textfile)
f.close()



#To download that file

response = urllib2.urlopen('/temp/pdf2txtconverted.txt')
data = response.read()
filename = "pdf2txtconverted.txt"
file_ = open(filename, 'w')
file_.write(data)
file_.close()

#delete the files from server after user downloaded the file successfully
os.remove("/temp/pdf2txtconverted.txt")

