import xlsxwriter

calismaKitabi = xlsxwriter.Workbook('Türkiye Covid19 Doughnut Grafiği.xlsx')

sayfaYapim = calismaKitabi.add_worksheet()

boldDegerim = calismaKitabi.add_format({'bold': 1})

basliklar = ['Durum', 'Sayı']

veriYapim = [
    {'Yoğun Bakım', 'Entübe', 'İyileşen'},
    {344,241,42},
]

sayfaYapim.write_row('A1', basliklar, boldDegerim)

sayfaYapim.write_column('A2', veriYapim[0])
sayfaYapim.write_column('B2', veriYapim[1])

chartYapim = calismaKitabi.add_chart({'type': 'doughnut'})

chartYapim.add_series({
    'name' : 'Doughnut Chart',
    'categories' : ['Sheet1',1,0,3,0],
    'values' : ['Sheet1', 1,1,3,1],
    'points' : [
        {'fill' : {'color' : 'black'}},
        {'fill' : {'color' : 'white'}},
        {'fill' : {'color' : 'yellow'}},
    ],
})

chartYapim.set_title({'name': 'Türkiye Covid 19 Grafiği'})

#chartYapim.set_rotation(105)

#chartYapim.set_style(10) # 2d Chart Oluştur

chartYapim.set_style(33) # 3d Chart oluşutr

sayfaYapim.insert_chart('D2', chartYapim)

calismaKitabi.close()