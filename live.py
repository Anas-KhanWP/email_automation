from main import EmailBot
from undetected_chromedriver import Chrome, ChromeOptions
import openpyxl

if __name__ == "__main__":
    # Load the Excel file
    workbook = openpyxl.load_workbook('email automation_2.xlsx.xlsx')

    # Assuming the data is in the first sheet
    sheet = workbook.active

    # Iterate over rows, starting from the second row (assuming the first row contains headers)
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data = {}
        name, email, password, recovery_email, forward_to = row
        data['NAME'] = name
        data['EMAILS'] = email
        data['PASSWORD'] = password
        data['RECOVERY EMAIL'] = recovery_email
        data['FORWARD TO'] = forward_to

        # Set up Chrome options
        options = ChromeOptions()
        # options.add_argument("--headless")  # Optional: Run Chrome in headless mode
        options.add_argument("--disable-extensions")  # Disable extensions
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Specify the correct path to Chrome binary

        # Initialize Chrome browser
        driver = Chrome(options=options)

        EB = EmailBot(driver)
        # Assuming bot_main is defined somewhere in your code
        EB.bot_main(email, password, recovery_email, forward_to)

    # Close the workbook after you're done
    workbook.close()
