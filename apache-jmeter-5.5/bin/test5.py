import csv
import json
import sys
import xlsxwriter

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
 
with open(input_file_path) as json_file:
    data = json.load(json_file)

# Define the list of fieldnames to be used in the CSV file
fieldnames = ["transaction", "sampleCount", "meanResTime", "medianResTime", "minResTime", "maxResTime", "pct1ResTime", "pct2ResTime", "pct3ResTime", "errorCount", "errorPct", "throughput", "receivedKBytesPerSec", "sentKBytesPerSec"]

# Open the output Excel file
workbook = xlsxwriter.Workbook(output_file_path)

# Add a bold format for the header row
bold = workbook.add_format({'bold': True})

# Add a blue fill color for the header row
header_format = workbook.add_format({'bold': True, 'bg_color': '#0070C0', 'font_color': 'white'})

# Add a red font color format for values > 5
red_fill_format = workbook.add_format({'bg_color': 'red'})

# Add a yellow fill color format for values between 3 and 5
yellow_fill_format = workbook.add_format({'bg_color': 'yellow'})

# Create a format object with a border
border_format = workbook.add_format({'border': True})

# Add a worksheet to the Excel file
worksheet = workbook.add_worksheet()

# Write header row with the custom format
worksheet.write_row(0, 0, ['Transaction', 'Iterations', 'Avg', 'Min', 'Max', '90%', 'Error Count', 'Error %', 'Throughput',
                           'Received KBytes/Sec', 'Sent KBytes/Sec'], header_format)

# Write data rows with number formatting
number_format = workbook.add_format({'num_format': '0.00'})
row_num = 1
for key, value in sorted(data.items(), key=lambda x: x[0].lower()):
    avg_res_time = value['meanResTime'] / 1000
    min_res_time = value['minResTime'] / 1000
    max_res_time = value['maxResTime'] / 1000
    pct1_res_time = value['pct1ResTime'] / 1000
    worksheet.write(row_num, 0, value['transaction'])
    worksheet.write(row_num, 1, value['sampleCount'])
    worksheet.write(row_num, 2, avg_res_time, number_format)
    worksheet.write(row_num, 3, min_res_time, number_format)
    worksheet.write(row_num, 4, max_res_time, number_format)
    worksheet.write(row_num, 5, pct1_res_time, number_format)
    worksheet.write(row_num, 6, value['errorCount'], number_format)
    worksheet.write(row_num, 7, value['errorPct'], number_format)
    worksheet.write(row_num, 8, value['throughput'], number_format)
    worksheet.write(row_num, 9, value['receivedKBytesPerSec'], number_format)
    worksheet.write(row_num, 10, value['sentKBytesPerSec'], number_format)
    # Apply conditional formatting to the cells with red and yellow fill formats
    worksheet.conditional_format(row_num, 2, row_num, 5, {'type': 'cell', 'criteria': '>', 'value': 5, 'format': red_fill_format})
    worksheet.conditional_format(row_num, 2, row_num, 5, {'type': 'cell', 'criteria': 'between', 'minimum': 3, 'maximum': 5, 'format': yellow_fill_format})
    worksheet.conditional_format(row_num, 7, row_num, 7, {'type': 'cell', 'criteria': '>', 'value': 2, 'format': red_fill_format})
    worksheet.conditional_format(row_num, 7, row_num, 7, {'type': 'cell', 'criteria': 'between', 'minimum': 0.5, 'maximum': 2, 'format': yellow_fill_format})
    # Set border for the entire worksheet
    worksheet.conditional_format(row_num, 0, row_num, 10, { 'type' : 'no_blanks' , 'format' : border_format} )
    row_num += 1



# Close the Excel file
workbook.close()