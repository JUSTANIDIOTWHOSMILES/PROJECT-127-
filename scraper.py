#from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []
stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,8):
        print(f'Scrapping page {i+1} ...' )

        soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("ul",attrs= {"class","brightest_stars"}):

        li_tags = ul_tag.find_all("li")

        temp_list = []
        for index,li_tag in enumerate (li_tags):

            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else: 
                try: 
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        stars_data.append(temp_list)
    
        ## ADD CODE HERE ##
        



        
# Calling Method    
scrape()

for i in range(0,len(scraped_data)):

    star_names = scraped_data[i][1]
    distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    luminosity = scraped_data[i][7]
# Define Header

headers = ["star_names", "distance", "mass", "radius", "luminosity"]
# Define pandas DataFrame   


# Convert to CSV
planet_df1 = pd.DataFrame(stars_data, columns = headers)
planet_df1.to_csv('scrap_data.csv',index = True, index_label="id")
    


