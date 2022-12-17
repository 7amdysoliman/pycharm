import requests
import bs4
import csv
from itertools import zip_longest
job_title=[]
company_name=[]
location=[]
skills=[]
links=[]
page_num=0
while True:
    url=f'https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}'
    page = requests.get(url)
    #print(page.content)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    page_limt=int (soup.find("strong").text)
    if (page_num>9):
        print("pages ended")
        break
    #print(page.content)
    job_titles = soup.find_all("h2", {"class":"css-m604qf" })
    company_names = soup.find_all("a",{"class":"css-17s97q8"})
    #print(company_names)
    location_names=soup.find_all("span",{"class":"css-5wys0k"})
    #print(location_name)
    job_skills=soup.find_all("div",{"class":"css-y4udm8"})
    #print(job_skills)
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs["href"])
        company_name.append(company_names[i].text)
        location.append(location_names[i].text)
        skills.append(job_skills[i].text)
      #  print(job_title[i],links[i],company_name[i],location[i],skills[i])

    file_list = [job_title,company_name,location,skills,links]
    page_num+=1
    print("page switched")

exported = zip_longest(*file_list)
with open("/Users/Laptop Market/documents/jobs.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company name ","location","skills","links"])
    wr.writerows(exported)
