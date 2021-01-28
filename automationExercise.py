from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC, expected_conditions

driver = webdriver.Chrome(executable_path="C:\\Users\\sharm\\Downloads\\chromedriver_win32\\chromedriver")

driver.implicitly_wait(50)

driver.maximize_window()

driver.get("https://demo.cloubi.com/web/cloubi/login")

driver.find_element_by_name("email").send_keys("gettokeerti@gmail.com")

driver.find_element_by_name("password").send_keys("recruitmentTest")

driver.find_element_by_xpath("//div[@class ='button-wrapper']").click()

wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='cloubi-theme-top-bar']/div[1]")))

menu = driver.find_element_by_xpath("//div[@class='cloubi-theme-top-bar']/div[1]")

menu.click()

submenu = driver.find_element_by_xpath("//span[text()='Products']")

ActionChains(driver).move_to_element(menu).click(submenu).perform()

driver.find_element_by_xpath("//button[@type='button' and @data-qa ='products-add-new-product']").click()

driver.find_element_by_xpath("//div[@class='cloubi-dropdown add-dropdown transparent']").click()

wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@role='menu']")))

driver.find_element_by_xpath("//ul[@class ='dropdown-menu down menu-align-left visible']/li[2]").click()

driver.find_element_by_xpath("//input[@type ='text' and @class ='input-field']").send_keys('Test Products')

driver.find_element_by_xpath(
    "//button[@class='cloubi-button btn btn-lg has-title default' and @type ='button']").click()

products = driver.find_elements_by_xpath("//div[@class ='product-container']")

wait = WebDriverWait(driver, 15)

wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[text()='Test Products']"), 'Test Products'))

desiredtopPanel = None

for product in products:
    productName = product.find_element_by_xpath("//div[@class='item-container']/div[1]/div[2]/div[1]/p[2]").text
    print('Product name is ::' + productName)
    if productName == "Test Products":
        print('Product found')
        desiredtopPanel = product.find_element_by_xpath("//div[@class='item-container']/div[1]/div[1]")
        break

action = ActionChains(driver)

action.move_to_element(desiredtopPanel).perform()
wait = WebDriverWait(driver, 10)
productButton = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='edit-button-container']/button")))
productButton.click()

driver.find_element_by_xpath("//button[@data-cy='add-item-button']").click()

driver.find_element_by_xpath("//input[@class='input-field']").send_keys("Page")

driver.find_element_by_xpath("//div[@class ='cloubi-modal-dialog-footer']/button[1]").click()

window_before =driver.window_handles[0]

driver.find_element_by_xpath("//button[@title='Content page']").click()

window_after =driver.window_handles[1]

driver.switch_to.window(window_after)

textArea = driver.find_element_by_xpath("//div[@class ='fr-wrapper']/div[1]/h1")

textArea.click()

action = ActionChains(driver)


action.move_to_element(textArea)
action.send_keys("EDITED").perform()




