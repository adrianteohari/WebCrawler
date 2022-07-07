from  bs4 import BeautifulSoup
import os
import requests

queue = []
flag=0
contor =0
domain="http://riweb.tibeica.com/crawl/"
queue.append(domain)


while len(queue)!=0 and contor<=100:
    flag=0
    contor=contor+1
    element = queue.pop()
    fileElement =element.replace("/","%")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path+"/temp"):
        for file in files:
           if(file==fileElement+".html"):
               flag=1
               break
    if(flag==0):
        #print(dir_path)
        split=element.split('/',3)
        print(split[2])
        request = requests.get(element)
        #print(request.text)
        f=open(dir_path+"/temp/"+fileElement+".html","w")
        f.write(request.text)
        f.close()
        print("---------------------------------------")
        soup = BeautifulSoup(request.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            queue.append(domain+link.get('href'))

    
