from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://free-proxy.cz/zh/proxylist/country/EG/http/ping/all"
click_export_selector = '//*[@id="clickexport"]'
zkzk_selector = '//*[@id="zkzk"]'
output_file = "eg-proxy.txt"

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Uncomment this line to run the browser in headless mode

driver = webdriver.Chrome(options=options)
driver.get(url)

try:
    # Wait for the clickexport element to be clickable and perform the click action
    click_export_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_export_selector))
    )
    click_export_element.click()

    # Wait for the zkzk element to be visible and get its content
    zkzk_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, zkzk_selector))
    )
    content = zkzk_element.text

    # Save content to a file
    with open(output_file, "w") as file:
        file.write(content)
    print(f"Content saved to {output_file}")

finally:
    driver.quit()


input_file = "eg-proxy.txt"
output_file = "eg-proxy.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

with open(output_file, "w") as file:
    for line in lines:
        file.write("http://" + line.strip() + "\n")

print(f"Updated content saved to {output_file}")
