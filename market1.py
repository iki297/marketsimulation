print("===============Selamat Datang di RR Market===============")
print("Daftar Produk")
print("1. Daging - Rp 20000")
print("2. Lampu - Rp 15000")
print("3. Apel - Rp 30000\n")
print("Daftar Produk Promo")
print("1. Susu - Rp 50000")
print("2. Maker - Rp 25000")
# Define the products and their prices
products = {"susu": 50000, "daging": 20000, "lampu": 15000, "masker":25000, "apel":30000}

# Define the cashier function
def cashier():
  total = 0
  while True:
    item = input("Masukan Produk (or 'hitung' to exit): ")
    jumlah= int(input("Jumlah (Masukan 1 setelah hitung): "))
    if item == "hitung":
      break
    elif item in products:
      price = products[item]
      total += price*jumlah
      print(f"{item} costs {price:.2f}. Total: {total:.2f}")
    else:
      print(f"Item '{item}' not found.")
  print(f"Final total: {total:.2f}")
  uang=int(input("Uang Tunai Pembeli: Rp "))
  kembalian=int(uang-total)
  print("\n========================================")
  print("========== S T R U K   B E L I =========")
  print("========================================")
#print ("Nama\t\t:",pembeli)
#print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
#print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
  print ("Tagihan\t\t: Rp",total)
  print ("Dibayar\t\t: Rp",uang)
  print ("Kembalian\t: Rp",kembalian)
  print("========================================")
  print("========================================")

# Call the cashier function
cashier()
