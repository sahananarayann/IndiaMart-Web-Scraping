from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


company_page = []
company_name = []
visited = []

driver = webdriver.Chrome(ChromeDriverManager().install())  #Install the Chrome Webdriver
driver.get("https://www.indiamart.com/")  #Web Scraping Target
driver.find_element_by_xpath('//*[@id="search-input"]').send_keys("vermicompost")
driver.find_element_by_xpath('//*[@id="searchBtn"]').click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

links = driver.find_elements_by_xpath("//a[@class='clr3 fs12 fwn rsrc']")

for link in links:  #For loop to get the company link and company name
    company_p = link.get_attribute('href')
    company_p = company_p.split('?')
    company_page.append(company_p[0])
    company_name.append(link.get_attribute('text'))

driver.close()  #Close the Web Driver

for ind, item in enumerate(company_name):
    if item in visited:
        del company_name[ind]
        del company_page[ind]
    visited.append(item)

d = {'Supplier Company Name' : company_name, 'Supplier IndiaMart Landing Page' : company_page}
df = pd.DataFrame(d)  #Create a DataFrame Object
file_name = "IndiaMartAnalysis.xlsx"  #Save As filename

print("Creating the excel file")
print(df)
df.to_excel(file_name)  #Save the DataFrame in Excel file
print("File saved")

