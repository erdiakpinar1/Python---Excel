import xlwt
from xlwt import Workbook

calismaKitabi = Workbook()

sayfa = calismaKitabi.add_sheet("Sayfa 1")

sayfa.write(1,0,"Python")
sayfa.write(2,0,"Java")
sayfa.write(3,0, "Matlab")

sayfa.write(0,1, "SQL")
sayfa.write(0,2, "C++")

#calismaKitabi.save('DosyaYazmak.xlsx')

style = xlwt.easyxf('font:bold 1, color blue')
sayfa.write(4,4,"Udemy",style)
calismaKitabi.save('styleDosyası2.xlsx')
