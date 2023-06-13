from selenium import webdriver
from selenium.webdriver.common.by import By
from RPA.Desktop import Desktop

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.collegenote.net/")

# Find and click on the element
csit_element = driver.find_element(By.LINK_TEXT, "CSIT")
csit_element.click()

# Close the browser
driver.quit()
