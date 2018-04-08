import xlrd

file_location = "C:/Users/spoonath/Documents/MISC/python_scripts/my_git_python/python/Katello_input.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(2)
cell = sheet.cell_value(3, 3)

# print(cell)

# print(sheet.nrows, sheet.ncols)

# to print a particular row fully
# for col in range(sheet.ncols):
#     row_val = sheet.cell_value(3, col)
#     print(row_val)

# equivalent using list comprehension
row_val = [sheet.cell_value(3, col) for col in range(sheet.ncols)]
# print(row_val)

# to print a particular col fully
# for row in range(sheet.nrows):
#     col_val = sheet.cell_value(row, 3)
#     print(col_val)
# equivalent using list comprehension
col_val = [sheet.cell_value(row, 3) for row in range(sheet.nrows)]
# print(col_val)

# list of list using list comprehension
val = [[sheet.cell_value(row, col) for row in range(sheet.nrows)] for col in range(sheet.ncols)]
print(sheet.cell_type(val[3][3]))
