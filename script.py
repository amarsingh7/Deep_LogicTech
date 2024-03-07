from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import json

# Install ChromeDriver based on the installed Chrome version
chromedriver_autoinstaller.install()

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Time.com website
driver.get("https://time.com/")

# Set up a WebDriverWait object with a timeout of 30 seconds
wait = WebDriverWait(driver, 30)

try:
    # Close any pop-up ads if present
    close_ad = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'animate-close')))
    close_ad.click()
except:
    print("Ad could not be closed")

try:
    # Find all elements containing the latest stories
    latest_stories = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'latest-stories__item')))
    
    # Initialize an empty list to store story dictionaries
    story_dicts = []

    # Iterate through each story element
    for story in latest_stories:
        # Find the first child element within the story element
        first_child = story.find_element(By.XPATH, "./*[1]")
        # Extract the text and href attribute of the first child element
        link_text = first_child.text
        link_href = first_child.get_attribute("href")
        # Create a dictionary with the story title and link
        story_dicts.append({'title': link_text, 'link': link_href})
    
    # Write the story dictionary list to a JSON file
    with open('data.json', 'w') as json_file:
        json.dump(story_dicts, json_file)

except:
    print("Could not find latest stories")

# Quit the WebDriver session
driver.quit()
