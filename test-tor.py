from selenium import webdriver 

service_args = [ '--proxy=localhost:9050', '--proxy-type=socks5']

driver = webdriver.PhantomJS(service_args = service_args)
#driver.get("http://www.naver.com")
driver.get("http://scanlover.com")
#driver.get("http://bogobogo.net")
#driver.get("http://bitsnoop.com")

print(driver.page_source)
driver.close()
