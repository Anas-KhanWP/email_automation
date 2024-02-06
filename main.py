import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class EmailBot:
    def __init__(self, driver):
        self.driver = driver

    def sleep_random(self):
        # Generate a random sleep time between 0.5 to 1 seconds
        sleep_time = random.uniform(0.7, 1)
        time.sleep(sleep_time)

    def clickNext(self):
        try:
            # Wait for the input field to be clickable
            _next = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@data-report-value="Submit"]'))
            )
            self.sleep_random()
            _next.click()
        except Exception as e:
            print(f"Error => {e}")

    def inputEmail(self, email):
        try:
            # Wait for the input field to be clickable
            input_field = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="i0116"]'))
            )
            self.sleep_random()
            input_field.click()
            input_field.send_keys(email)  # Replace this with your email
        except Exception as e:
            print(f"Error => {e}")

    def inputPass(self, password):
        try:
            # Wait for the input field to be clickable
            input_field = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))
            )
            self.sleep_random()
            input_field.click()
            self.sleep_random()
            input_field.send_keys(password)  # Replace this with your email
        except Exception as e:
            print(f"Error => {e}")

    def inputConfirmEmail(self, confirm_email):
        try:
            # Find the email input field using its XPath
            email_input = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="iProofEmail"]'))
            )
            self.sleep_random()
            if email_input:
                email_input.send_keys(confirm_email)  # Enter email address
                print("Email entered successfully")
            else:
                print("Email input field not found")

        except Exception as e:
            print(f"Error => {e}")

    def submitConfirmEmail(self):
        # Find the submit button using its XPath
        submit_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="iSelectProofAction"]'))
        )
        self.sleep_random()
        if submit_button:
            submit_button.click()
            self.sleep_random()
            print("Submit button clicked successfully")
        else:
            print("Submit button not found")

    def submitSecurityCode(self):
        # Find the submit button using its XPath
        submit_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="iVerifyCodeAction"]'))
        )
        self.sleep_random()
        if submit_button:
            submit_button.click()
            self.sleep_random()
            print("Submit button clicked successfully")
        else:
            print("Submit button not found")

    def switchWindow(self, tab):
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def newTab(self, tab):
        # Execute JavaScript to open a new tab
        self.driver.execute_script("window.open('about:blank','_blank');")
        self.sleep_random()
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def emailForCode(self, email):
        # Find the submit button using its XPath
        _email = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="spammail"]'))
        )
        self.sleep_random()
        _email.click()
        _email.send_keys(email)
        self.sleep_random()
        _email.send_keys(Keys.RETURN)
        self.sleep_random()

    def clickForCode(self):
        # Find the <a> element using XPath with normalize-space()
        link_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space(text())="Microsoft account security code"]'))
        )

        self.sleep_random()
        link_element.click()
        self.sleep_random()

    def getSecurityCode(self):
        try:
            # Get the page source
            page_source = self.driver.page_source

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

    def enterSecurityCode(self, code):
        try:
            # Find the email input field using its XPath
            code_input = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="tel"]'))
            )
            self.sleep_random()
            if code_input:
                code_input.send_keys(code)  # Enter email address
                print("Email entered successfully")
            else:
                print("Email input field not found")

        except Exception as e:
            print(f"Error => {e}")

    def goToSettings(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            settings_ = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="owaSettingsButton"]'))
            )

            self.sleep_random()
            settings_.click()
            self.sleep_random()
        except Exception as e:
            print(f"error => {e}")

    def settingFw(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            settings_fw = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space(text())="Forwarding"]'))
            )

            self.sleep_random()
            settings_fw.click()
            self.sleep_random()
        except Exception as e:
            print(f"error => {e}")

    def staySignedIn(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
        except Exception as e:
            print(f"error => {e}")

    def emailCode(self):
        try:
            link_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[starts-with(text(), 'Email')]"))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
        except Exception as e:
            print(f"error => {e}")

    def reEnterConfirmEmail(self, confirm_email):
        try:
            # Find the <a> element using XPath with normalize-space()
            settings_ = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@name="ProofConfirmation"]'))
            )

            self.sleep_random()
            settings_.click()
            self.sleep_random()
            settings_.send_keys(confirm_email)
            self.sleep_random()

        except Exception as e:
            print(f"error => {e}")

    def clickSubmitButton(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            submit_ = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]'))
            )

            self.sleep_random()
            submit_.click()
            self.sleep_random()
            submit_.send_keys("kulejeqv26@mailforspam.com")
            self.sleep_random()

        except Exception as e:
            print(f"error => {e}")

    def breakFromPassword(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            submit_ = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="iCancel"]'))
            )

            self.sleep_random()
            submit_.click()
            self.sleep_random()

        except Exception as e:
            print(f"No popup")

    def verifyIdentity(self):
        self.emailCode()
        self.sleep_random()
        self.reEnterConfirmEmail("dfnxwrnm70@mailforspam.com")
        self.sleep_random()
        self.clickSubmitButton()
        self.sleep_random()
        self.getCode()

    def switchToggle(self):
        try:
            time.sleep(10)
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//label[text()='Enable forwarding']"))
            )

            self.sleep_random()
            link_element.click()
            print("Forwarding Toggled")
            self.sleep_random()
            print("switchToggle done")
        except Exception as e:
            print(f"error => {e}")

    def forwardTo(self, email):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]'))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            link_element.send_keys(email)
            print("Email Entered For Forwarding")
            self.sleep_random()
            print("ForwardTo done")
        except Exception as e:
            print(f"error => {e}")

    def closePopUp(self):
        try:
            # Wait for the element to be clickable
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))
            )

            # Click on the element
            element.click()
            print("Popup Closed")
        except Exception as e:
            print(f"Error Occurred => {e}")

    def selectCopy(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Keep a copy of forwarded messages']"))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            print("Select Copy done")
        except Exception as e:
            print(f"error => {e}")

    def navigateToRules(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            settings_fw = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//button[normalize-space(text())="Rules"]'))
            )

            self.sleep_random()
            settings_fw.click()
            self.sleep_random()
            print("Navigate to rules done")
        except Exception as e:
            print(f"error => {e}")

    def addNewRule(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Add new rule']"))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            print("AddNewRule done")
        except Exception as e:
            print(f"error => {e}")

    def inputRuleName(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@type="text"]'))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            link_element.send_keys("ALL MAIl")
            print("inputRuleName done")
        except Exception as e:
            print(f"error => {e}")

    def addCondition(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            condition = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Select a condition"]'))
            )

            self.sleep_random()
            condition.click()
            self.sleep_random()
            print("addCOndition done")
        except Exception as e:
            print(f"error => {e}")

    def applyToAll(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            apply_all = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Apply to all messages"]'))
            )

            self.sleep_random()
            apply_all.click()
            self.sleep_random()
            print("applytoall done")
        except Exception as e:
            print(f"error => {e}")

    def addAction(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            condition = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Select an action"]'))
            )

            self.sleep_random()
            condition.click()
            self.sleep_random()
            print("addAction Done")
        except Exception as e:
            print(f"error => {e}")

    def actionList(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            apply_all = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//span[normalize-space(text())="Forward to"]'))
            )

            self.sleep_random()
            apply_all.click()
            self.sleep_random()
            print("actionList Done")

        except Exception as e:
            print(f"error => {e}")

    def enterForwardEmail(self, forward_to):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@role="textbox"]'))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            link_element.send_keys(forward_to)
            self.sleep_random()
            # Locate the element using XPath
            confirm_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@class="MIV76 j7as6"]'))
            )

            # Click the element
            confirm_element.click()
            self.sleep_random()
            print("EnterForwardEmail Done")
        except Exception as e:
            print(f"error => {e}")

    def selectInputOption(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="iProof0"]'))
            )

            self.sleep_random()
            link_element.click()
            self.sleep_random()
            print("SelectInputOption Done")
        except Exception as e:
            print(f"error => {e}")

    def verifyCode(self):
        try:
            # Find the <a> element using XPath with normalize-space()
            link_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="idSubmit_SAOTCC_Continue"]'))
            )

            self.sleep_random()
            link_element.click()
            print("Verify Code Done")
            self.sleep_random()
        except Exception as e:
            print(f"error => {e}")

    def enableForwarding(self, comfirmation_email, forward_to):
        self.sleep_random()
        self.closePopUp()
        self.sleep_random()
        self.goToSettings()
        self.sleep_random()
        self.settingFw()
        self.sleep_random()

        # Asking for verification again
        self.emailCode()
        self.sleep_random()
        self.reEnterConfirmEmail(comfirmation_email)
        self.sleep_random()
        self.clickSubmitButton()
        self.sleep_random()

        # Get Code Again
        self.getCode(3, comfirmation_email)
        self.sleep_random()
        self.verifyCode()
        self.sleep_random()
        self.breakFromPassword()
        self.sleep_random()

        # Continue with Forwarding
        self.sleep_random()
        self.closePopUp()
        self.sleep_random()
        self.switchToggle()
        self.sleep_random()
        self.forwardTo(forward_to)
        self.selectCopy()

        # Add New Rule
        self.navigateToRules()
        self.sleep_random()
        self.addNewRule()
        self.sleep_random()
        self.inputRuleName()
        self.sleep_random()
        self.addCondition()
        self.sleep_random()
        self.applyToAll()
        self.sleep_random()
        self.addAction()
        self.sleep_random()
        self.actionList()
        self.enterForwardEmail(forward_to)

    def getCode(self, tab, comfirmation_email):
        self.newTab(tab)
        self.driver.get("https://mailforspam.com")
        self.emailForCode(comfirmation_email)
        self.sleep_random()
        self.clickForCode()
        self.sleep_random()
        security_code = self.getSecurityCode()
        self.sleep_random()

        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.sleep_random()
        self.enterSecurityCode(security_code)
        self.sleep_random()

    def bot_main(self, email, password, comfirmation_email, forward_to):
        try:
            # Open the URL
            url = "https://outlook.live.com/mail/0/"  # Replace this with your desired URL
            self.driver.get(url)

            # Wait for the element to be clickable
            sign_in = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-bi-cn="SignIn"]'))
            )

            if sign_in:
                sign_in.click()
                print("Sign in button clicked")
                self.sleep_random()
                self.switchWindow(1)
                self.sleep_random()
                self.inputEmail(email)
                self.sleep_random()
                self.clickNext()
                self.sleep_random()
                self.inputPass(password)
                self.sleep_random()
                self.clickNext()
                self.sleep_random()
                self.selectInputOption()
                self.sleep_random()
                self.inputConfirmEmail(comfirmation_email)
                self.sleep_random()
                self.submitConfirmEmail()

                # Verification Code
                self.getCode(2, comfirmation_email)
                self.submitSecurityCode()
                self.sleep_random()
                self.staySignedIn()
                self.sleep_random()
                self.breakFromPassword()

                # Enable Forwarding
                self.enableForwarding(comfirmation_email, forward_to)
                print("Email entered successfully")

            else:
                print("no sign in button")

            time.sleep(5)
        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the browser
            if 'driver' in locals():
                self.driver.quit()
