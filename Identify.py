from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://facebook.com")

# Finds the element using the name attribute. Send_keys is used to type into the field.
driver.find_element_by_name("firstname").send_keys("Dupa")

# Looking for link
driver.find_element_by_link_text("Forgot account?").click()
driver.back()

# Look using xpath
driver.find_element_by_xpath(".//*[@id='email']").send_keys("Dupa")

driver.quit()
