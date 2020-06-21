import xlsxwriter

calisamaKitabi = xlsxwriter.Workbook('Türkiye Covid 19 Bar Grafiği.xlsx')

sayfa = calisamaKitabi.add_worksheet()

boldDegeri = calisamaKitabi.add_format({'bold': 1})

basliklar = ['Tarih', 'Vaka Sayısı', 'Vefat Sayısı']

verilerim = [
    ['22 Mart', '23 Mart', '24 Mart', '25 Mart', '26 Mart', '27 Mart'],
    [1236,1529,1872,2433,3629,5698],
    [300,370,440,590,750,920]
]

sayfa.write_row('A1', basliklar, boldDegeri)
sayfa.write_column('A2', verilerim[0])
sayfa.write_column('B2', verilerim[1])
sayfa.write_column('C2', verilerim[2])

chartYapim = calisamaKitabi.add_chart({'type' : 'bar'})

chartYapim.add_series({
    'name' : ['Sheet1', 0,1],
    'categories' : ['Sheet1', 1, 0, 6, 0],
    'values' : ['Sheet1', 1,1,6,1],
})

chartYapim.add_series({
    'name' : ['Sheet1', 0, 2],
    'categories' : ['Sheet1', 1,0,6,0],
    'values' : ['Sheet1', 1,2,6,2],
})

sayfa.insert_chart('E2', chartYapim)

chartYapim.set_title({'name' : 'Türkiye Covid19 Grafiği'})
chartYapim.set_x_axis({'name' : 'Sayılar'})
chartYapim.set_y_axis({'name': 'Günler'})

calisamaKitabi.close()
