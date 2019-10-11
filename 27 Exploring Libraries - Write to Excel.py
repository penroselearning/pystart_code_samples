# Install xlsxwriter using the below command on your computer
# pip install xlsxwriter
# Copy the Code to your Python Editor to run the program
# Explore more Options with the PIL Library using the below documentation
# https://xlsxwriter.readthedocs.io/tutorial01.html

try:

    import xlsxwriter

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('VacationBudget.xlsx')
    worksheet = workbook.add_worksheet()

    # Sample data we want to write to the worksheet
    budget = {'Flight': 2500,
              'Hotel': 1000,
              'Food': 300,
              'SightSeeing': 1000,
              'Local Transport': 300,
              'Shopping': 1000
              }

    # First Row and First Columns start at Index of 0
    row = 0
    col = 0

    # Iterate over the budget dictionary and write it to the Excel File row by row.
    for item, cost in budget.items():
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        row += 1

    # Write a total at the bottom of the Budget Data using an Excel Formula
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')

    workbook.close()

except ModuleNotFoundError:
    print('Kindly import the PIL Library')