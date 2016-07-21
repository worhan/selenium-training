from selenium import webdriver

driver_path = ("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(driver_path)
driver.get("https://google.com")
driver.close()