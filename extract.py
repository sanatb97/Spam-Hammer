import os
from bs4 import BeautifulSoup

def find_occurances(text,substring):
	occurances = []
	index = 0
	while True:
		occurance = text.find(substring,index)
		if occurance == -1:
			return text
		else:
			end = text.find(">",occurance)
			text = text.replace(text[occurance:end+1],"")
			index = occurance+1


def extract_body(paths,destinations):
	a = 0
	for path in paths:
		inbox_files = os.listdir(path)
		print(len(inbox_files))
		i = 0
		htmls = []
		for i in range(0,len(inbox_files)):
			fp1 = open(path+"/"+inbox_files[i],'r',errors = 'ignore')
			lines = fp1.readlines()
			body = ""
			for j in range(0,len(lines)):
				if "Subject: " in lines[j]:
					body+= lines[j]+"\n"
				if "From: " in lines[j]:
					body+=lines[j]+"\n"
				if "Message-ID: " in lines[j]:
					body+=lines[j]+"\n"
				if 'Content-Transfer-Encoding: 7bit' in lines[j]:
					k = j + 2
					while k<len(lines):
						if "--b1_" in lines[k]:
							break
						else:
							body+=lines[k].strip("\n")
							k = k + 1
					j = k-1
			fp1.close()
			body = find_occurances(body,"<http")
			#print(body)
			fp = open(destinations[paths.index(path)]+inbox_files[i],'w')
			a = a+1
			#print(type(subject))
			#fp.write(subject)
			fp.write(body)
			fp.close()


def extract_HTML(paths,destinations):
	a = 0
	for path in paths:
		inbox_files = os.listdir(path)
		i = 0
		for i in range(0,len(inbox_files)):
			fp1 = open(path+"/"+inbox_files[i],'r',errors = 'ignore')
			lines = fp1.readlines()
			html = ""
			for j in range(0,len(lines)):
				if "<html>" in lines[j]:
					html+=lines[j].strip("\n")
					k = j + 1
					while k<len(lines):
						if "</html>" in lines[k]:
							html+=lines[k].strip("\n")
							break
						else:
							html+=lines[k].strip("\n")
							k = k + 1
					j = k - 1
			fp1.close()
			#print(body)
			fp = open(destinations2[paths2.index(path)]+inbox_files[i],'w')
			a = a+1
			#print(type(subject))
			#fp.write(subject)
			fp.write(html)
			fp.close()	


paths = ["/home/nishant/Documents/final_test_mails"]
destinations = ["/home/nishant/Documents/final_test_body/"]
paths2 = ["/home/nishant/Documents/final_test_mails"]
destinations2 = ["/home/nishant/Documents/final_test_html/"]
#extract_body(paths,destinations)
extract_HTML(paths2,destinations2)


