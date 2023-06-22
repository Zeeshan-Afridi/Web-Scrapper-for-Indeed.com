# Web-Scrapper-for-Indeed.com using Python
This is a Python script that demonstrates web scraping using Selenium to scrape job data from the Indeed website. It performs a job search based on the specified job title and location, retrieves job titles, company names, and locations from each search result page, and stores the data in a list.

The script uses the webdriver module from Selenium to automate the web browser. It sets up the Chrome driver, navigates to the Indeed website, and enters the job details. It then iterates through the search result pages, extracts the job data using XPath, and appends it to the indeed_data list.

The script handles scenarios such as clicking the "Next Page" button to navigate through multiple pages of search results and closing any pop-up windows that may appear
