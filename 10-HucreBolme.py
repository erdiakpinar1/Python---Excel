import openpyxl
from openpyxl.styles import Font

calisamaKitabi = openpyxl.Workbook()
sayfaYapım = calisamaKitabi.active

sayfaYapım['A1'] = 1
sayfaYapım['A2'] = 2
sayfaYapım['A3'] = 3
sayfaYapım['A4'] = 4
sayfaYapım['A5'] = 5

sayfaYapım['A7'] = '=SUM(A1:A5)'

sayfaYapım['C1'] = 1
sayfaYapım['C2'] = 2
sayfaYapım['C3'] = 3
sayfaYapım['C4'] = 4
sayfaYapım['C5'] = 5

sayfaYapım['C7'] = '=PRODUCT(C1:C5)'

sayfaYapım['E1'] = 12
sayfaYapım['E2'] = 60
sayfaYapım['E3'] = 31
sayfaYapım['E4'] = 44
sayfaYapım['E5'] = 56

sayfaYapım['E7'] = '=AVERAGE(E1:E5)'

sayfaYapım['F1'] = '=QUOTIENT(E2,E1)'

sayfaYapım['G1'] = '=MOD(100,10)'
sayfaYapım['G2'] = '=MOD(9,2)'

calisamaKitabi.save('HucreModAlma.xlsx')