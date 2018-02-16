from bs4 import BeautifulSoup
import os
paths_HTML = ["/home/nishant/Documents/final_test_html"]
paths_body = ["/home/nishant/Documents/final_test_body"]
destinations = ["/home/nishant/Documents/final_test_inputs"]
non_htmls = []

def getNonHtml(lines):
    non_html = ""
    html = ""
    for line in lines:
        html+=line.strip()
    soup = BeautifulSoup(html,'lxml')
    #print(html)
    for tag in soup.find_all():
        if tag.name not in ['html','head','style']:
            text = tag.text
            non_html+=text
    return non_html


for i in range(0,len(paths_body)):
    body_files = os.listdir(paths_body[i])
    html_files = os.listdir(paths_HTML[i])
    for j in range(0,len(body_files)):
        fp_body = open(paths_body[i]+"/"+body_files[j],'r')
        body = fp_body.read()
        #print(body)
        fp_body.close()
        fp_html = open(paths_HTML[i]+"/"+html_files[j],'r')
        #print(j)
        #print(paths_HTML[i]+"/"+html_files[j])
        html = fp_html.readlines()
        non_html = getNonHtml(html)
        fp_final = open(destinations[i]+"/"+body_files[j],'w+')
        fp_final.write(body+non_html)
