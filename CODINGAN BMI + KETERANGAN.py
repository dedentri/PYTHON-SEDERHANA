print(20*'=') #UNTUK MENCETAK '=' SEBANYAK 20
print('KALKULATOR BMI') #SEBAGAI JUDUL 
print(20*'=') #UNTUK MENCETAK '=' SEBANYAK 20

berat_badan=float(input('masukan berat badan kamu:  ')) #UNTUK MEMASUKAN BERAT BADAN DAN MENGGUNAKAN FLOAT SUPAYA BISA DIMASUKAN ANGKA DENGAN KOMA
tinggi_badan=float(input('masukan tinggi badan kamu:  '))#UNTUK MEMASUKAN TINGGI BADAN DAN MENGGUNAKAN FLOAT SUPAYA BISA DIMASUKAN ANGKA DENGAN KOMA

print(20*'==') #UNTUK MENCETAK '=' SEBANYAK 20
hasil=berat_badan/(tinggi_badan/100)**2 #RUMUS UNTUK MENENTUKAN KONDISI BERAT BADAN 
print('HASIL BMI ADALAH: ',hasil) #UTNUK MENAMPILKAN HASIL DARI RUMUS YANG TELAH DI TULIS 
print(20*'==') #UNTUK MENCETAK '=' SEBANYAK 20

print('KETERANGAN:')#UNTUK MENCETAK KETERANGAN DARI HASIL YANG DIKELUARKAN

if hasil < 18: #JIKA HASILNYA DI BAWAH 18 MAKA BERAT BADAN KURANG 
    print('berat badan kamu kurang')
elif hasil < 22.9:  #JIKA HASILNYA DI BAWAH 22,9 MAKA BERAT BADAN NORMAL 
    print('berat badan kamu normal')
elif hasil == 23:  #JIKA HASILNYA SAMA DENGAN 23 MAKA BERAT BADAN BERLEBIHAN 
    print('berat badan kamu berlebihan')
elif hasil <= 24:  #JIKA HASILNYA KURANG/SAMA DENGAN 24 MAKA BERAT BADAN TERLALU BERLEBIHAN 
    print('berat badan kamu terlalu berlebihan')
elif hasil <= 29.9: #JIKA HASILNYA KURANG/SAMA DENGAN 29,9 MAKA BERAT BADAN MENGALAMI OBESITAS TAHAP 1
    print('obesitas tahap 1')
else:#OPSI TERAKHIR JIKA RUMUS MENGHASILKAN ANGKA DI ATAS 29,9 MAKA TERMASUK OBESITAS TAHAM 2 YANG BERBAHAYA
    print('obesitas tahap 2,bahaya!!!')