from selenium import webdriver

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()
driver.get('http://mlbpark.com')
driver.save_screenshot('screen.png')

