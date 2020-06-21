import xlsxwriter

calismaKitabi = xlsxwriter.Workbook("COVID19 Türkiye Grafiği Açı.xlsx")
sayfaYapim = calismaKitabi.add_worksheet()

boldDegeri = calismaKitabi.add_format({'bold': 1}) #Kalın Yazılacak Yazılara eklemek için style

basliklar = ['Durum', 'Sayılar']

veriYapım = [
    ['Vefat Eden', 'Vaka', 'İyileşen'],
    [92,5698,42]
]

sayfaYapim.write_row('A1', basliklar, boldDegeri)
sayfaYapim.write_column('A2', veriYapım[0])
sayfaYapim.write_column('B2', veriYapım[1])

chartYapim = calismaKitabi.add_chart({'type':'pie'})

chartYapim.add_series({
    'name':'Covid19 Grafiği',
    'categories' : ['Sheet1',1,0,3,0],
    'values' : ['Sheet1',1,1,3,1],
    'points' : [
        {'fill' : {'color' : 'red'}},
        {'fill' : {'color' : 'purple'}},
        {'fill' : {'color' : 'yellow'}},
    ]
})
chartYapim.set_title({'name': 'COVİD19 TURKİYE GRAFİĞİ'})
chartYapim.set_rotation(90)
sayfaYapim.insert_chart('C2', chartYapim)
calismaKitabi.close()