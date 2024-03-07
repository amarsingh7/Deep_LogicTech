from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import json

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get("https://time.com/")
wait = WebDriverWait(driver, 30)

try:
    close_ad = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'animate-close')))
    close_ad.click()
except:
    print("Ad could not be closed")

try:
  latest_stories = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'latest-stories__item')))
  story_dicts = []
  for story in latest_stories:
      first_child = story.find_element(By.XPATH, "./*[1]")
      link_text = first_child.text
      link_href = first_child.get_attribute("href")
      story_dicts.append({
          'title': link_text,
          'link': link_href
      })
  with open('data.json', 'w') as json_file:
    json.dump(story_dicts, json_file)

except:
    print("Could not find latest stories")

driver.quit()