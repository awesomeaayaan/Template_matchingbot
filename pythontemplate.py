from RPA.Browser.Selenium import Selenium
from RPA.Desktop import Desktop
from RPA.Images import Images

browser = Selenium()
desktop = Desktop()
image = Images()

random_location_website = "https://www.randomlists.com/random-location"
directions_screenshot = "${CURDIR}/output/directions.png"

def find_travel_directions_between_two_random_locations():
    locations = get_random_locations()
    open_maps_app()
    maximize_window()
    view_directions(locations[0], locations[1])

def get_random_locations():
    browser.open_available_browser(random_location_website, headless=True)
    browser.set_window_size(1600, 1200)
    location_elements = browser.get_elements("css:.rand_medium")
    location_1 = browser.get_text(location_elements[0])
    location_2 = browser.get_text(location_elements[1])
    return location_1, location_2

def open_maps_app():
    desktop.run_process("open", "-a", "Maps")
    desktop.wait_for_element(alias="Maps.MapMode", timeout=10)

def maximize_window():
    not_maximized = desktop.run_keyword_and_return_status("Find Element", alias="Desktop.WindowControls")
    if not_maximized:
        desktop.press_keys("ctrl", "cmd", "f")
    desktop.wait_for_element_not_visible(alias="Desktop.WindowControls")

def view_directions(location_1, location_2):
    directions_open = desktop.run_keyword_and_return_status("Find Element", alias="Maps.SwapLocations")
    if not directions_open:
        desktop.press_keys("cmd", "r")
    desktop.wait_for_element(alias="Maps.SwapLocations")
    desktop.click(alias="Maps.ResetFromAndToLocationsIcon")
    desktop.press_keys("cmd", "r")
    desktop.wait_for_element(alias="Maps.SwapLocations")
    enter_location("alias:Maps.FromLocation", location_1)
    enter_location("alias:Maps.ToLocation", location_2)
    directions_found = desktop.run_keyword_and_return_status("Wait For Element", alias="Maps.RouteIcon", timeout=20.0)
    if directions_found:
        desktop.take_screenshot(filename=directions_screenshot)
    else:
        view_directions_using_google_maps(location_1, location_2)

def enter_location(locator, location):
    desktop.wait_for_element(locator)
    desktop.click(locator)
    desktop.type_text(location, enter=True)

def view_directions_using_google_maps(location_1, location_2):
    browser.go_to(f"https://www.google.com/maps/dir/{location_1}/{location_2}/")
    accept_google_consent()
    desktop.wait_until_element_is_visible("id:section-directions-trip-0")
    desktop.screenshot(filename=directions_screenshot)

def accept_google_consent():
    browser.click_button_when_visible("xpath://form//button")

find_travel_directions_between_two_random_locations()
