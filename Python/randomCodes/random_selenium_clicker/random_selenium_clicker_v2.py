from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

# Automatically install the latest version of ChromeDriver
chromedriver_autoinstaller.install()

# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Open the URL
url = 'https://www.menti.com/alvmpa11eqyd'
driver.get(url)

try:
    # Wait for the "Lambda" team radio button to be clickable
    lambda_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/main/form/div/div[2]/label[6]/div/div/span[2]/label/span/svg/circle'))
    )
    lambda_button.click()
    print("Lambda radio button clicked.")

    # time.sleep(3)
    # Wait for the submit button to be clickable and click it
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()
    print("Submit button clicked.")

    # Introduce a sleep delay (e.g., 3 seconds) to observe the changes (optional)
    time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
