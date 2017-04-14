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

#对DIV内容进行预处理，删除【实验步骤】前的内容，删除"`"符号
position=re.search("实验步骤",div,flags=0).span()[1]
div=div[position:].replace("`","")

output=open('output.txt','w')
output.write('')
output.close()
count=1
output=open('output.txt','a',encoding='utf-8')
for text in re.findall(r"\d\.\d.*?<center>", div):
	text=text[:-8].replace("\t","")
	position=re.search(r"\d.\d+ ?",text,flags=0).span()[1]
	text=text[position:]
	print(str(count)+" "+text+"\n")
	output.write(str(count)+' '+text+'\n'+'\n')
	count=count+1
output.close()