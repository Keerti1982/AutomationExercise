from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Load the selenium webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\sharm\\Downloads\\chromedriver_win32\\chromedriver")

driver.maximize_window()

# Launch the application
driver.get("https://demo.cloubi.com/web/cloubi/login")

# For login
driver.find_element_by_name("email").send_keys("gettokeerti@gmail.com")

driver.find_element_by_name("password").send_keys("recruitmentTest")

driver.find_element_by_xpath("//div[@class ='button-wrapper']").click()

# For clicking Hamburger menu
wait = WebDriverWait(driver, 20)

# Access the Menu and click the submenu Product
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class ='handle top-bar-element']")))

menu = driver.find_element_by_xpath("//div[@class ='handle top-bar-element']").click()

driver.find_element_by_xpath("//div[@class ='cloubi-theme-side-bar']/div[2]").click()

# Click on Add New Button to add new Product
driver.find_element_by_xpath("//div[@class ='products-bar-actions']/button").click()

driver.implicitly_wait(20)

driver.find_element_by_xpath("//div[@class ='cloubi-modal-dialog-content']/div[1]/div[1]").click()

# Select the desired option
driver.find_element_by_xpath("//ul[@role ='menu']/li[2]").click()

# Enter the product name
driver.find_element_by_xpath("//input[@type ='text' and @class ='input-field']").send_keys('Test Products')

# Click on Save
driver.find_element_by_xpath("//div[@class ='cloubi-modal-dialog-footer']/button[1]").click()

# Get the reference of all the products container
products = driver.find_elements_by_xpath("//div[@class ='product-container']")

# Wait for the last product with the name "Test Products" to appear in the list
wait = WebDriverWait(driver, 15)

wait.until(
    expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[text()='Test Products']"), 'Test Products'))

# Get the reference of the topPanel that has the product name as "Test Products"
desiredtopPanel = None

# Iterate through all the products on the screen and search for a product name "Test Products"
for product in products:
    productName = product.find_element_by_xpath("//p[@data-cy='product-name']")
    print('product name is ' + productName.text)

    # Once we get the desired product get the reference of top panel and break the loop

    if productName.text == "Test Products":
        desiredtopPanel = product.find_element_by_xpath("//div[@class='item-container']/div[1]/div[1]")
        # Preferred way to navigate but it messes up the flow later
        # desiredtopPanel = productName.find_element_by_xpath("//div[@class='top-container']/parent::div")

        break

# Wait for the new added product to show up in the list and then mouse hover to the top panel of that product
action = ActionChains(driver)

action.move_to_element(desiredtopPanel).perform()

wait = WebDriverWait(driver, 10)

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
textArea = driver.find_element_by_xpath("//div[@class ='fr-wrapper']/div[1]/h1")

textArea.click()

# get reference to action driver to relocate the curser at the start of text area
actionNewWindow = ActionChains(driver)

actionNewWindow.move_by_offset(0, 0)

actionNewWindow.click().perform()

y_coordinate = textArea.location["y"]

x_coordinate = textArea.location["x"]

# again get reference to action to insert custom text
actionNewWindow = ActionChains(driver)

driver.implicitly_wait(10)

actionNewWindow.click().key_down(Keys.INSERT).send_keys("EDITED").perform()

# To-do:need to work on deleting Test product to run automation successfully

# driver.find_element_by_xpath("//div[@id ='_fi_cloubi_portlets_library_LibraryEditor_toolbar']/div[2]/div[1]/button").click()

# driver.switch_to.window(window_before)

# driver.find_element_by_xpath("//div[@class ='back-arrow-container']")
