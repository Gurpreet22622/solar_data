import xlsxwriter

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet('sun')

f = open('solar_data.txt', 'r')
lines = f.readlines()

row = 1

for line in lines:
    col = -1

    def inc_col():
        global col
        col = col + 1
        return col

    length = len(line)
    worksheet.write(row, inc_col(), line[:4])
    worksheet.write(row, inc_col(), line[4:6])
    worksheet.write(row, inc_col(), line[6:12])
    data = ['']*11
    c = 0
    for i in range(12, length-1):
        if line[i] != ' ':
            data[c] = data[c] + line[i]
        if line[i] != ' ' and line[i+1] == ' ':
            c = c+1
    for j in data:
        worksheet.write(row, inc_col(), j)
    row = row + 1

workbook.close()
