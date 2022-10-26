# input nilai variabel
a=input("masukan variabel a:")
b=input("masukan variabel b:")

# cetak nilai variabel
print("variabel a=",a)
print("variabel b=",b)

# cetak hasil operasi kedua variabel dengan string format
print("hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a/b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
