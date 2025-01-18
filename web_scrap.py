import pandas as pd
import requests

from bs4 import BeautifulSoup as bf

# Fetching data from intershala website from allover the india

url_list=['https://internshala.com/internships/web-development-internship-in-bangalore/','https://internshala.com/internships/internship-in-delhi/','https://internshala.com/internships/internship-in-hyderabad/','https://internshala.com/internships/internship-in-mumbai/'
          ,'https://internshala.com/internships/internship-in-chennai/','https://internshala.com/internships/internship-in-pune/','https://internshala.com/internships/internship-in-kolkata/']

company_name_list=[]
job_title_list=[]
intern_duration=[]
stipend_list=[]
job_details_list=[]
company_location_list=[]

def scrap(url):

    response= requests.get(url)

    if response.status_code == 200:
        sp = bf(response.text, 'lxml')
        main_content=sp.find('div',class_ ='container-fluid with_breadcrumbs').find('div',class_ ='internship_list_container').find('div',id ='internship_list_container_1')

        job_data=main_content.find_all('div',class_ ='container-fluid individual_internship view_detail_button visibilityTrackerItem')

        for job in job_data:
            company_name_list.append(job.find('div',class_ ='company').find('p').text.strip() if job.find('div',class_ ='company').find('p').text.strip() is not None else None)
            job_title_list.append(job.find('div',class_ ='company').find('h3').a.text.strip() if job.find('div',class_ ='company').find('h3').a.text.strip() is not None else None)
            job_details_list.append('https://internshala.com'+str(job.find('div',class_ ='company').find('h3').a['href']) if job.find('div',class_ ='company').find('h3').a['href'] is not None else None)
            company_location_list.append(job.find('div',class_ ='detail-row-1').find('div',class_ ='row-1-item locations').span.text.strip() if job.find('div',class_ ='detail-row-1').find('div',class_ ='row-1-item locations').span.text.strip() is not None else None)
            intern_duration.append(job.find('div',class_ ='detail-row-1').find_all('div',class_ ='row-1-item')[1].span.text.strip() if job.find('div',class_ ='detail-row-1').find_all('div',class_ ='row-1-item')[1].span.text.strip() is not None else None)
            stipend_list.append(job.find('div',class_ ='detail-row-1').find_all('div',class_ ='row-1-item')[2].find('span',class_ ='stipend').text.strip() if job.find('div',class_ ='detail-row-1').find_all('div',class_ ='row-1-item')[2].find('span',class_ ='stipend').text.strip() is not None else None)
            

    df_dict={
        'Job Title':job_title_list,
        'Company Name':company_name_list,
        'Company Location':company_location_list,
        'Intern Duration':intern_duration,
        'Stipend':stipend_list,
        'Job Details Url':job_details_list
    } 

    df = pd.DataFrame(df_dict)
    return df

for url in url_list:
    df = scrap(url)
    
print(df) 
df.to_csv('internshala.csv')   




    




