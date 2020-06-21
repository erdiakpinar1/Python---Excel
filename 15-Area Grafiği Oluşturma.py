import xlsxwriter

calismaKitabi = xlsxwriter.Workbook('Türkiye Covid 19 Area Grafiği.xlsx')

sayfa = calismaKitabi.add_worksheet()

boldDegeri = calismaKitabi.add_format({'bold': 1})
basliklar = ['Tarih', 'Vaka Sayısı', 'Vefat Sayisi']

verilerim = [
    ['17 Mart', '18 Mart', '19 Mart', '20 Mart', '21 Mart', '22 Mart'],
    [90,191,359,670,947,1236],
    [10,20,40,90,210,300]
]

sayfa.write_row('A1', basliklar, boldDegeri)

sayfa.write_column('A2', verilerim[0])
sayfa.write_column('B2', verilerim[1])
sayfa.write_column('C2', verilerim[2])

chartYapim = calismaKitabi.add_chart({'type' : 'area'})

chartYapim.add_series(
    {
        'name': ['Sheet1', 0, 1],
        'categories' : ['Sheet1', 1,0,6,0],
        'values' : ['Sheet1', 1,1,6,1]
    })


sayfa.insert_chart('E2', chartYapim)

calismaKitabi.close()
