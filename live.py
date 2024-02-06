import pandas as pd
from main import EmailBot
from undetected_chromedriver import Chrome, ChromeOptions

if __name__ == "__main__":
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel('email automation_2.xlsx')

    # Iterate over rows in the DataFrame
    for index, row in df.iterrows():
        data = {
            'NAME': row['NAME'],
            'EMAILS': row['EMAILS'],
            'PASSWORD': row['PASSWORD'],
            'RECOVERY EMAIL': row['RECOVERY EMAIL'],
            'FORWARD TO': row['FORWARD TO']
        }

        print(f"Data => {data}")

        # Set up Chrome options
        options = ChromeOptions()
        # options.add_argument("--headless")  # Run Chrome in headless mode
        options.add_argument("--disable-extensions")  # Disable extensions
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Specify the correct path to Chrome binary

        # Initialize Chrome browser
        driver = Chrome(options=options)

        EB = EmailBot(driver)
        # Assuming bot_main is defined somewhere in your code
        EB.bot_main(data['EMAILS'], data['PASSWORD'], data['RECOVERY EMAIL'], data['FORWARD TO'])

        # Close the driver after iterating over all rows
        driver.quit()
