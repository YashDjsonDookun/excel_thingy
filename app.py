from openpyxl import load_workbook
data = []
excel_file = "someSheet.xlsx"
txt_file = "something.txt"
with open(txt_file) as f:
    data = [(f.read()).split('|')[:-1]]
wb = load_workbook(filename = excel_file)
ws = wb.active
for d in data:
    ws.append(d)
wb.save(filename="someSheet.xlsx")