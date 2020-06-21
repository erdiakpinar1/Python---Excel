import openpyxl
from openpyxl.styles import Font

calisamaKitabi = openpyxl.Workbook()
sayfaYapım = calisamaKitabi.active

sayfaYapım['A1'] = 1
sayfaYapım['A2'] = 2
sayfaYapım['A3'] = 3
sayfaYapım['A4'] = 4
sayfaYapım['A5'] = 5

sayfaYapım['A8'] = '=PRODUCT(A1:A5)'

calisamaKitabi.save('hucreCarpma.xlsx')
