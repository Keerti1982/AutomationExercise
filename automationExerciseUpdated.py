import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Load the selenium webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\sharm\\Downloads\\chromedriver_win32\\chromedriver")

driver.maximize_window()

driver.implicitly_wait(5)

# Launch the application
driver.get("https://demo.cloubi.com/web/cloubi/login")

# For login
driver.find_element_by_name("email").send_keys("gettokeerti@gmail.com")

driver.find_element_by_name("password").send_keys("recruitmentTest")

driver.find_element_by_xpath("//button[@type ='button']").click()

# For clicking Hamburger menu
driver.find_element_by_xpath("//div[@class ='handle top-bar-element']").click()

# For selecting the submenu
driver.find_element_by_xpath("//div[@class ='cloubi-theme-side-bar']/div[2]").click()

# Click on Add New Button to add new Product
driver.find_element_by_xpath("//button[@data-qa ='products-add-new-product']").click()
# for locating the dropdown list
driver.find_element_by_xpath("//div[@data-cy ='type-dropdown']").click()

# Select the desired option
driver.find_element_by_xpath("//ul[@role ='menu']/li[2]").click()

# Enter the product name
driver.find_element_by_css_selector(".input-field").send_keys('Test Products')

# Click on Save
driver.find_element_by_xpath("//div[@class ='cloubi-modal-dialog-footer']/button[1]").click()

# Get the reference of all the products container
products = driver.find_elements_by_xpath("//div[@class ='product-container']")

# Wait for the last product with the name "Test Products" to appear in the list
wait = WebDriverWait(driver, 5)

wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[text()='Test Products']"), 'Test Products'))

# Get the reference of the topPanel that has the product name as "Test Products"
desiredTopPanel = []

# Iterate through all the products on the screen and search for a product name "Test Products"
for product in products:
    productName = product.find_element_by_xpath("//p[@data-cy='product-name']")
    # Once we get the desired product get the reference of top panel and break the loop
    if productName.text == "Test Products":
        desiredTopPanel = productName.find_element_by_xpath("//div[@class='top-container']/parent::div")
        break

# Wait for the new added product to show up in the list and then mouse hover to the top panel of that product
action = ActionChains(driver)

action.move_to_element(desiredTopPanel).perform()

productButton = wait.until(
    expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='edit-button-container']/button")))

# Once the product appears in the list after mouse hover ,click the edit button
productButton.click()

# Click the add item button
driver.find_element_by_xpath("//button[@data-cy='add-item-button']").click()

# Enter data in Item Name
driver.find_element_by_xpath("//input[@class='input-field']").send_keys("Page")

# Click on save button
driver.find_element_by_xpath("//div[@class ='cloubi-modal-dialog-footer']/button[1]").click()

# Preserve the old window as new window gets open
window_before = driver.window_handles[0]

# click the link to open new window
driver.find_element_by_xpath("//button[@title='Content page']").click()

# get the reference of newly created window
window_after = driver.window_handles[1]

# switch the driver to access element of new window
driver.switch_to.window(window_after)

# get the reference of editable text area
textArea = driver.find_element_by_tag_name("h1")

textArea.click()

# get reference to action driver to relocate the curser at the start of text area
actionNewWindow = ActionChains(driver)

actionNewWindow.move_by_offset(-100, -100)

# enter text 'Edited' before the displayed text
actionNewWindow.click().send_keys('EDITED').perform()

# Close the 2nd window
driver.close()

# Switch to old window
driver.switch_to.window(window_before)
# Click on back arrow near 'Test Product'
driver.find_element_by_xpath("//div[@class ='back-arrow-container']").click()

time.sleep(4)

# below steps we are doing for looking for the newly created 'Test Product' and deleting it.
# It will help us to run the script next time also.
products = driver.find_elements_by_xpath("//div[@class ='product-container']")

for product in products:
    productName = product.find_element_by_xpath("//p[@data-cy='product-name']")

    # Once we get the desired product get the reference of top panel and break the loop
    if productName.text == "Test Products":
        desiredTopPanel = productName.find_element_by_xpath("//div[@class='top-container']/parent::div")
        break

action = ActionChains(driver)

action.move_to_element(desiredTopPanel).perform()

desiredTopPanel.find_element_by_css_selector(".delete-button").click()

time.sleep(2)

driver.find_element_by_xpath("//div[@class='cloubi-modal-dialog-footer']/button[1]").click()
