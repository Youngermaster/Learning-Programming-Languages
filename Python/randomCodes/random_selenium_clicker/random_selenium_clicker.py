from selenium import webdriver
import chromedriver_autoinstaller
import time

# Automatically install the latest version of ChromeDriver
chromedriver_autoinstaller.install()

# Create a new instance of the web driver
driver = webdriver.Chrome()

# Open the URL
url = 'https://www.menti.com/alvmpa11eqyd?source=qr-instructions-widget?source=qr'
driver.get(url)

# Find the "Lambda" team radio button by its label text
label_text = "Lambda"
radio_button = driver.find_element_by_xpath(f'//span[text()="{label_text}"]/../input')

# Click the radio button
radio_button.click()

# Find and click the "Submit" button
submit_button = driver.find_element_by_xpath('//button[contains(text(), "Submit")]')
submit_button.click()

# Introduce a sleep delay (e.g., 3 seconds)
time.sleep(30)

# Close the browser
driver.quit()
