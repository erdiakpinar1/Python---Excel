import openpyxl
from openpyxl.styles import Font

calisamaKitabi = openpyxl.Workbook()
sayfaYapım = calisamaKitabi.active


sayfaYapım.column_dimensions['A'].width=20
sayfaYapım.column_dimensions['B'].width=30
sayfaYapım.column_dimensions['C'].width=20

sayfaYapım['A1'] = 'radyan cinsinden açılar'
sayfaYapım['A2'] = 0.1
sayfaYapım['A3'] = 0.2
sayfaYapım['A4'] = 0.3
sayfaYapım['A5'] = 0.4
sayfaYapım['A6'] = 0.5
sayfaYapım['A7'] = 0.6

#fonksiyon isimlerini excel dosyasına aktar
sayfaYapım['B1'] = 'Fonksiyon'
sayfaYapım['B2'] = 'sinüs'
sayfaYapım['B3'] = 'cosinüs'
sayfaYapım['B4'] = 'Tanjant'
sayfaYapım['B5'] = 'Cosecant'
sayfaYapım['B6'] = 'Secant'
sayfaYapım['B7'] = 'Cotanjant'

#işlemler
sayfaYapım['C1'] = 'Değerler'
sayfaYapım['C2'] = '=SIN(0.1)'
sayfaYapım['C3'] = '=COS(0.2)'
sayfaYapım['C4'] = '=TAN(0.3)'
sayfaYapım['C5'] = '=CSC(0.4)'
sayfaYapım['C6'] = '=SEC(0.5)'
sayfaYapım['C7'] = '=COT(0.6)'

calisamaKitabi.save('AcılarıBul.xlsx')