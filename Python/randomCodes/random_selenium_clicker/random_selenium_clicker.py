from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

# Automatically install the latest version of ChromeDriver
chromedriver_autoinstaller.install()

# Set up options for the Chrome driver to wait implicitly for elements to appear
options = webdriver.ChromeOptions()

# Create a new instance of the web driver
driver = webdriver.Chrome(options=options)

# Define an explicit wait (WebDriverWait instance)
wait = WebDriverWait(driver, 10)  # wait for a maximum of 10 seconds

# Open the URL
url = 'https://www.menti.com/alvmpa11eqyd?source=qr-instructions-widget?source=qr'
driver.get(url)

# Wait for the radio button associated with the "Lambda" team to be clickable
label_text = "Lambda"
try:
    # Wait until the element which contains the text "Lambda" is present
    element_present = EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Lambda')]"))
    element = wait.until(element_present)

    # Find the parent label of this span, and then find the input element
    radio_button = element.find_element(By.XPATH, "./ancestor::label//input[@type='radio']")
    
    # Click the radio button
    radio_button.click()

    # Wait for the "Submit" button to be clickable and then click it
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Introduce a sleep delay (e.g., 3 seconds)
    time.sleep(30)
    # Close the browser
    driver.quit()
