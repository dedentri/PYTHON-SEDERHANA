print(50*"=")
print("HASIL TANTANGAN ADVANCE CODING CHALLENGE SMKDEV")
print("----------------------TUGAS----------------------")
print("tulis program untuk mencetak hasil pangkat tiga")
print("dari bilangan 1 hingga bilangan tertentu")
print(50*"=")

#BUATLAH VARIABEL YANG NANTI AKAN DI ISI OLEH USER MENGGUNAKAN KODE DI BAWAH INI
#KODE DI BAWAH AKAN MEMINTA USER UNTUK MENGISI JUMLAH ANGKA YANG INGIN DI TAMPILKAN 
input_angka = int(input("masukan jumlah angka yang ingin di tampilkan: "))
print(50*"-")
 
#GUNAKAN FUNGSI PERULANGAN PYTHON MENGGUNAKAN FOR I IN RANGE UNTUK MEMBUAT LOOPINGAN 
#YANG BERISI JUMLAH ANGKA YANG AKAN DITAMPILKAN DAN DIMULAI DARI ANGKA 1
#ISI DENGAN (1,input_angka + 1) ANGKA 1 DI AWAL BERFUNGSI SUPAYA PROGRAM DIMULAI DARI ANGKA 1
#VARIABEL input_angka ADALAH VARIABEL YANG BERISI ANGKA YANG INGIN DITAMPILKAN
#FUNGSI (+ 1) SUPAYA 1 ANGKA TERAKHIR TETAP DI MUNCULKAN  
for i in range(1,input_angka + 1): 
    print("Current number is :",i,"The cube is", i**3)
#TAMPILKAN HASILNYA DENGAN i SEBAGAI NOMORNYA DAN i**3 SEBAGAI HASIL DARI PANGKAT 3 YANG AKAN DITAMPILKAN