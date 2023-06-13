from selenium import webdriver
from RPA.Desktop import Desktop
from RPA.Images import Images

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the website using Selenium
driver.get("https://www.collegenote.net/")

# Take a screenshot using RPA Desktop
robot = Desktop()
screenshot_path = robot.take_screenshot()

# Perform template matching with RPA Desktop
template_path = "template.png"
found_element = robot.find_template_in_image(template_path, screenshot_path)

# Close the browser
driver.quit()
