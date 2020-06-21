import xlrd

yerBilgisi = ("yeni.xlsx")

calismaKitabi = xlrd.open_workbook(yerBilgisi)

sayfa = calismaKitabi.sheet_by_index(0)

#print(sayfa.cell_value(1,1))
#print(sayfa.cell_value(2,2))

# Satır Sayısını Bul
#print("Satır sayısı : ", sayfa.nrows)
# Sütun Sayısını Bul
#print("Sütun Sayısı : ",sayfa.ncols)

#Excel Dosyasının Başlıkları:
#for baslik in range(sayfa.ncols): # range(3) = 0,1,2
#    print(sayfa.cell_value(0,baslik))

#Excel Satırlarının hepsini alalım

yeni_baslik = []
yeni_satir = []
new = []

"""for baslik in range(sayfa.ncols): # 0 1 2
    for aciklama in range(sayfa.nrows): # 0 1 2 3
        yeni_satir.append(sayfa.cell_value(aciklama, baslik))
    new.append(yeni_satir)
    yeni_satir = []

print(new)
"""
for satir in range(sayfa.nrows):
    print(sayfa.row_values(satir))
