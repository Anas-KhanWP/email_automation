from main import bot_main
import openpyxl

if __name__ == "__main__":
    # Load the Excel file
    workbook = openpyxl.load_workbook('your_file.xlsx')

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

        # Assuming bot_main is defined somewhere in your code
        bot_main(email, password, recovery_email, forward_to)

    # Close the workbook after you're done
    workbook.close()
