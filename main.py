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
            print(f"error => {str(e)}")

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
            print(f"error => {str(e)}")

    def nextButton(self):
        try:
            next_element = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="idSIButton9"]'))
            )
            self.sleep_random()
            next_element.click()
            print("Next")
        except Exception as e:
            print(f"error => {str(e)}")

    def saveRule(self):
        _save = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Save']"))
        )
        self.sleep_random()
        _save.click()

    def enableForwarding(self, confirmation_email, forward_to):
        """
        Function to enable email forwarding in Outlook Live settings.

        Args:
            confirmation_email (str): The email address used for confirmation.
            forward_to (str): The email address to forward emails to.
        """
        try:
            self.sleep_random()
            self.closePopUp()  # Close any pop-up windows
            self.sleep_random()
            self.goToSettings()  # Navigate to settings
            self.sleep_random()
            self.settingFw()  # Navigate to forwarding settings
            self.sleep_random()

            # Asking for verification again
            self.emailCode()  # Request verification code
            self.sleep_random()
            self.reEnterConfirmEmail(confirmation_email)  # Re-enter confirmation email
            self.sleep_random()
            self.clickSubmitButton()  # Click submit button
            self.sleep_random()

            # Get Code Again
            self.getCode(3, confirmation_email)  # Retrieve verification code again
            self.sleep_random()
            self.verifyCode()  # Verify the code
            self.sleep_random()
            self.breakFromPassword()  # Break from password input
            self.sleep_random()

            # Continue with Forwarding
            self.sleep_random()
            self.closePopUp()  # Close any pop-up windows
            self.sleep_random()
            self.switchToggle()  # Toggle forwarding switch
            self.sleep_random()
            self.forwardTo(forward_to)  # Set forwarding address
            self.sleep_random()
            self.selectCopy()  # Select 'keep a copy' option

            # Add New Rule
            self.navigateToRules()  # Navigate to rules settings
            self.sleep_random()
            self.addNewRule()  # Add a new rule
            self.sleep_random()
            self.inputRuleName()  # Input rule name
            self.sleep_random()
            self.addCondition()  # Add a condition
            self.sleep_random()
            self.applyToAll()  # Apply the rule to all emails
            self.sleep_random()
            self.addAction()  # Add an action
            self.sleep_random()
            self.actionList()  # Select forwarding action
            self.sleep_random()
            self.enterForwardEmail(forward_to)  # Enter email to forward to
            self.sleep_random()
            self.saveRule()  # Save the rule
            self.sleep_random()
        except Exception as e:
            print(f"Error while setting email forwarding => {str(e)}")

    def getCode(self, tab, confirmation_email):
        """
        Function to retrieve verification code from a temporary email service.

        Args:
            tab (int): The index of the tab to open.
            confirmation_email (str): The email address used for confirmation.
        """
        try:
            self.newTab(tab)  # Open a new tab
            self.driver.get("https://mailforspam.com")  # Open temporary email url
            self.emailForCode(confirmation_email)  # Enter the confirmation email
            self.sleep_random()
            self.clickForCode()  # Click to retrieve the code
            self.sleep_random()
            security_code = self.getSecurityCode()  # Get the security code
            self.sleep_random()

            # Switch to the new tab
            self.driver.switch_to.window(self.driver.window_handles[1])

            self.sleep_random()
            self.enterSecurityCode(security_code)  # Enter the security code
            self.sleep_random()
        except Exception as e:
            print(f"Error while retrieving security code => {str(e)}")

    def bot_main(self, email, password, confirmation_email, forward_to):
        """
        Main function to automate signing in, enabling email forwarding,
        and handling verification codes for Outlook Live email accounts.

        Args:
            email (str): The email address to sign in with.
            password (str): The password associated with the email account.
            confirmation_email (str): The email address used for confirmation.
            forward_to (str): The email address to forward emails to.

        Raises:
            Exception: If any error occurs during the process.
        """
        try:
            # Open the URL
            url = "https://outlook.live.com/mail/0/"
            self.driver.get(url)

            # Wait for the element to be clickable
            sign_in = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-bi-cn="SignIn"]'))
            )

            if sign_in:
                sign_in.click()
                print("Sign in button clicked")
                self.sleep_random()
                self.switchWindow(1)  # Switch to the new window
                self.sleep_random()
                self.inputEmail(email)  # Input the email address
                self.sleep_random()
                self.nextButton()  # Click the 'Next' button after email input
                self.sleep_random()
                self.inputPass(password)  # Input the password
                self.sleep_random()
                self.clickNext()  # Click the 'Next' button after password input
                self.sleep_random()
                self.selectInputOption()  # Select the input option
                self.sleep_random()
                self.inputConfirmEmail(confirmation_email)  # Input the confirmation email
                self.sleep_random()
                self.submitConfirmEmail()  # Submit the confirmation email

                # Verification Code
                self.getCode(2, confirmation_email)  # Retrieve the verification code
                self.sleep_random()
                self.submitSecurityCode()  # Submit the verification code
                self.sleep_random()
                self.staySignedIn()  # Opt to stay signed in
                self.sleep_random()
                self.breakFromPassword()  # Break from the password input

                # Enable Forwarding
                self.enableForwarding(confirmation_email, forward_to)  # Enable email forwarding
                print("Email entered successfully")

            else:
                print("no sign in button")

            time.sleep(5)  # Pause for 5 seconds after completion
        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the browser
            if 'driver' in locals():
                self.driver.quit()
