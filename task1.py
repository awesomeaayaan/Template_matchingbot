from selenium import webdriver
from RPA.Desktop import Desktop

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.collegenote.net/")

# Take a screenshot
robot = Desktop()
screenshot_path = robot.take_screenshot()
# screenshot_path = 'template.png'

# Perform template matching
found_element = robot.find_template_on_screen("CSIT", screenshot_path)

# Click on the "CSIT" element
if found_element:
    robot.click(found_element)

# Close the browser
driver.quit()
