class jual_beli:
  #fungsi rumus harga kali banyak barang
  def harga_total(harga_satuan, jumlah_barang):
    return harga_satuan*jumlah_barang
  
 #fungsi tanpa kembalian berisi identitas kelompok 
  def Identitas_kelompok():
    print("Kelompok 35")
    print("Shift 2")
    print("Engelbert Jubile Satrio Lukito 21120120140080")
    print("Muhammad Sulthon Auliya 21120120130047")
    print("Rafif Sadid Hamdani 21120120140137")
  
#program main/untuk eksekusi
objek=jual_beli()
x="y"
  #perulangan berupa jumlah berapa kali transksi
while(x=="y"):

    #daftar barang
    print("1:Buku tulis")
    print("2:Pensil")
    print("3:Bolpoin")

    pilihan=int(input("masukan pilihan anda (1-3): "))
    jumlah_barang=int(input("Masukan jumlah barang yang akan dibeli: "))
    
    harga1=objek.harga_total(3000, jumlah_barang)
    harga2=objek.harga_total(2000, jumlah_barang)
    harga3=objek.harga_total(3000, jumlah_barang)
    harga_akhir=0

    if pilihan==1:
        print("Harga sementara : ", harga1)
        harga_akhir=harga_akhir+harga1
    elif pilihan==2:
        print("Harga sementara : ", harga2)
        harga_akhir=harga_akhir+harga2
    elif pilihan==3:
        print("Harga sementara : ", harga3)
        harga_akhir=harga_akhir+harga3
    else:
        print("input anda salah")

    x=input("Beli barang lain?(y=yes,selain itu dianggap no) ")  
  

print("Jumlah uang yang harus anda bayar: ", harga_akhir)

  
  
#penjelasan
Program ini merupakan program sederhana yang berfungsi melakukan mekanisme perhitungan jual beli.
disini dalam class yang bernama jual_beli, terdapat 2 fungsi method yaitu yang pertama adalah
yang pertama adalah fungsi harga_total yang merupakan fungsi kembalian yang mengembalikan nilai dari parameternya
yaitu mengembalikan operasi perkalian variabel harga_satuan dan jumlah_barang. selanjutnya merupakan fungsi identitas_kelompok yang akan mengeluarkan beberapa output.
