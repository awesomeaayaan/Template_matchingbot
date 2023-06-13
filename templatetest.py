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

# Perform template matching with RPA.Desktop
template_path = "template.png"
found_elements = robot.find_template_on_screen(template_path, screenshot_path)

# Close the browser
driver.quit()

# Load the screenshot image using RPA.Images
image = Images()
screenshot = image.open(screenshot_path)

# Draw rectangles on the matched templates and save the image
for element in found_elements:
    image.rectangle(screenshot, element["left"], element["top"], element["width"], element["height"], color="red", width=2)
    
image.save(screenshot, "matches.png")

# Click on the matched templates
for element in found_elements:
    x = element["left"] + element["width"] // 2
    y = element["top"] + element["height"] // 2
    robot.click_position(x, y)
