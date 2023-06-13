from selenium import webdriver
import cv2

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.collegenote.net/")

# Take a screenshot
screenshot_path = "screenshot.png"
driver.save_screenshot(screenshot_path)

# Load the template image
template_path = "template.png"
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

# Load the screenshot image
screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

# Perform template matching
result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
match_threshold = 0.8

# If a match is found above the threshold, click on the element
if max_val > match_threshold:
    element_position = (top_left[0] + template.shape[1] // 2, top_left[1] + template.shape[0] // 2)
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(None, element_position[0], element_position[1])
    action.click()
    action.perform()

# Close the browser
driver.quit()
