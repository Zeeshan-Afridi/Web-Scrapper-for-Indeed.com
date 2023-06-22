#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

class IndeedScraper:
    def __init__(self):
        self.driver = None
        self.indeed_data = [["Job Title", "Company", "Location"]]

    def setup_selenium(self):
        # Set up Selenium and open the Indeed website
        url = "https://pk.indeed.com/?from=gnav-homepage"
        os.environ['PATH'] += r"Chromedriver.exe"
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def enter_job_details(self, job, location):
        # Enter job details and click the search button
        add_job = self.driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
        add_location = self.driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
        find_jobs_btn = self.driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button')

        add_job.clear()
        add_location.clear()

        add_job.send_keys(job)
        add_location.send_keys(location)
        find_jobs_btn.click()

    def scrape_data(self):
        # Scrape job data from each page
        while True:
            job_titles = self.driver.find_elements(By.XPATH, '//h2[@class="jobTitle css-1h4a4n5 eu4oa1w0"]')
            company = self.driver.find_elements(By.XPATH, '//div[@class="heading6 company_location tapItem-gutter companyInfo"]/span')
            location = self.driver.find_elements(By.XPATH, '//div[@class="companyLocation"]')

            for i in range(len(job_titles)):
                job_title = job_titles[i].text
                company_name = company[i].text
                location_info = location[i].text

                self.indeed_data.append([job_title, company_name, location_info])

                print(job_title, company_name, location_info)

            try:
                next_page_button = self.driver.find_element(By.XPATH, '//a[@aria-label = "Next Page"]')
                if 'disabled' in next_page_button.get_attribute("class"):
                    break

                next_page_button.click()
                self.driver.implicitly_wait(3)
                
                try:
                    close_button = self.driver.find_element(By.XPATH, '//button[@aria-label = "close"]')
                    close_button.click()
                    self.driver.implicitly_wait(3)
                except NoSuchElementException:
                    pass

            except NoSuchElementException:
                print("No more data is available.")
                break

    def close_browser(self):
        # Close the browser
        self.driver.quit()


# Usage example
scraper = IndeedScraper()
scraper.setup_selenium()
scraper.enter_job_details("Software engineer", "Lahore")
scraper.scrape_data()
scraper.close_browser()

