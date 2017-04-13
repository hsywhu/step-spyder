from bs4 import BeautifulSoup
import re
import os

file_object=open('input.txt')
try:
	file_text=file_object.read()
finally:
	file_object.close()
soup=BeautifulSoup(file_text,"html.parser")
div=soup.find(id="test-editormd-view2")
div=str(div).replace("\n"," ")
output=open('output.txt','w')
output.write('')
output.close()
output=open('output.txt','a',encoding='utf-8')
for text in re.findall(r"\d\.\d.*?<center>", div):
	text=text[:-8].replace("\t","")
	print(text)
	output.write(text+'\n')
output.close()
