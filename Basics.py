from selenium import webdriver

# Driver object will be working with Firefox
driver = webdriver.Firefox()

# Opens URL
driver.get("https://www.google.com")

# Prints current URL and page title
print(driver.current_url)
print(driver.title)

# Go to Gmail
driver.get("https://www.gmail.com")

# Go back, and forward, check title
driver.back()
driver.forward()
print(driver.title)

# Refresh page
driver.refresh()

# Maximize window
driver.maximize_window()

# Closes browser
driver.close()
# driver.quit() would kill the app and all windows. The former option will only close the current window

# Comment added to test Gist


