from selenium import webdriver

CHROMEDRIVER = "chromium.chromedriver"
browser = webdriver.Chrome(CHROMEDRIVER)
browser.get("http://localhost:8000")

assert "Django" in browser.title