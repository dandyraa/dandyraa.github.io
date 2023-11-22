"""
CAPSTONE PROJECT MODULE 1
JCDSOL-012 (C)
BY : DANDY RAMADI
"""

# Data Penjualan Toko Alat Tulis (Stationary)

# 1. Buat Dictionary
products = {
    1: {'produk': 'Buku Tulis' , 'harga' : 3500 , 'quantity' : 120 },
    2: {'produk': 'Buku Gambar' , 'harga' : 5000 , 'quantity' : 60 },
    3: {'produk': 'Pulpen Gel' , 'harga' : 3000 , 'quantity' : 72 },
    4: {'produk': 'Pensil 2B' , 'harga' : 3000 , 'quantity' : 120 },
    5: {'produk': 'Spidol Boardmarker' , 'harga' : 11000 , 'quantity' : 48 },
    6: {'produk': 'Penghapus' , 'harga' : 1500 , 'quantity' : 80 },
}

# 2. Definisikan function untuk isi dari menu
def daftarpenjualan():
    border = '-' * 70
    while True :
        option1 = input('''
            =====================================================
                       * * * Data Penjualan * * *
            =====================================================
    Pilihan sub-menu :
    1. Tampilkan seluruh data penjualan
    2. Tampilkan data penjualan berdasarkan index                    
    3. Kembali ke Menu Utama

    Silahkan masukkan angka sesuai menu pilihan (1 - 3) : ''')
        if option1.isnumeric():
            option1b = int(option1)

            if option1b == 1:
                if len(products) == 0:
                    print("\n\tMAAF, TIDAK ADA DATA PENJUALAN YANG DAPAT DITAMPILKAN.")
                else:
                    total_penjualan = 0
                    print("""
                    =========================================
                     Data penjualan Toko Buku Purwadhika 24
                    =========================================
        {}
    {:>7}|{:<23}|{:<15}|{:<8}|{}
        {}""".format(border, "No.","Nama Produk","Harga Satuan","Jumlah","Total Penjualan",border))
                    for i in products:
                        totalpenjualan = products[i]['harga']*products[i]['quantity']
                        total_penjualan += totalpenjualan
                        print('\t{:>3}|{:<23}| Rp. {:<10}|{:<8}| Rp. {}'.format
                        (i,products[i]['produk'],products[i]['harga'],products[i]['quantity'],totalpenjualan))
                    print("""\t{}
        {}{}""".format(border,'Grand total penjualan Toko Buku Purwadhika 24 = Rp. ',total_penjualan))
                
            elif option1b == 2:
                cariindex = input('''
    ----------------------------
     Cari data berdasarkan index
    ----------------------------
    Masukkan index data yang ingin dicari : ''')
                if cariindex.isnumeric():
                    cariindex2 = int(cariindex)
                    if cariindex2 not in products.keys():
                        print("\n\tMAAF, TIDAK ADA DATA PENJUALAN YANG DAPAT DITAMPILKAN. MOHON MASUKKAN INDEX YANG SESUAI!")
                    else :
                        totalpenjualan = products[cariindex2]['harga']*products[cariindex2]['quantity']
                        print('''
        Menampilkan data penjualan dengan index : {}
        {}
        {} | {:<21} | {:<10} | {:<6} | {}
        {}
        {:>4}|{:<23}| Rp. {:<9}|{:<8}| Rp. {}
        {}'''.format(cariindex2, border, "No.", "Nama Produk", "Harga Satuan", "Jumlah", "Total Penjualan", border, cariindex2,
                    products[cariindex2]['produk'], products[cariindex2]['harga'], products[cariindex2]['quantity'], totalpenjualan,border))
                else: 
                    print("\n\tMAAF, TIDAK ADA DATA PENJUALAN YANG DAPAT DITAMPILKAN. MOHON MASUKKAN INDEX YANG SESUAI!")
            elif option1b == 3:
                break

            else:
                print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
        else:
            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")

def addingdata():
    while True:
        option2 = input("""
            =====================================================
                   * * * Menambahkan Data Penjualan * * *
            =====================================================
    Pilihan sub-menu :
    1. Menambahkan data penjualan baru
    2. Kembali ke Menu Utama
                      
    Silahkan masukkan angka sesuai menu pilihan (1 atau 2) : """)
        if option2.isnumeric():
            option2b = int(option2)
        
            if option2b == 1:
                while True :
                    indexbaru = input("""
            Masukkan index data yang ingin ditambahkan : """)
                    if indexbaru.isnumeric():
                        indexbaru2 = int(indexbaru)
                        if indexbaru2 in products:
                            print("\n\tMAAF, INDEX YANG ANDA MASUKKAN TELAH TERDAFTAR. MOHON MASUKKAN KEMBALI INDEX BARU!")
                        else:
                            products[indexbaru2] = {}
                            print("""
                    -----------------------------------------------------
                        * * * Menambahkan Data Penjualan * * *
                    -----------------------------------------------------""")
                            produkbaru = input("\tMasukkan nama produk baru : ")
                            hargabaru = int(input("\tMasukkan harga satuan produk baru : "))
                            jumlahbaru = int(input("\tMasukkan jumlah produk baru yang telah terjual : "))
                            databaru = input("\tApakah anda yakin ingin menambahkan data penjualan baru dengan index {}? (Y/N) :  "
                                            .format(indexbaru2))

                            if databaru.upper() == "Y":
                                print("\n\tDATA PENJUALAN BERHASIL DITAMBAHKAN!")
                                products[indexbaru2]['produk'] = produkbaru
                                products[indexbaru2]['harga'] = hargabaru
                                products[indexbaru2]['quantity'] = jumlahbaru
                                break
                            elif databaru.upper() == "N":
                                print("\n\tDATA PENJUALAN BATAL DITAMBAHKAN!")
                            else :
                                print("\n\tMAAF, PENAMBAHAN DATA PENJUALAN GAGAL!")
                    else:
                        print("\n\tMAAF, PENAMBAHAN DATA PENJUALAN GAGAL!")
            elif option2b == 2:
                break

            else:
                print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
        else:
            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")

def updatedata():
    border = '-' * 70
    while True :
        option3 = input('''
            =====================================================
                   * * * Memperbarui Data Penjualan * * *
            =====================================================
    Pilihan sub-menu :
    1. Perbarui data penjualan
    2. Kembali ke Menu Utama

    Silahkan masukkan angka sesuai menu pilihan (1 atau 2) : ''')
         
        if option3.isnumeric():
            option3b = int(option3)
         
            if option3b  == 1:
                indexupdate = input("""
            Masukkan index data yang ingin diperbarui : """)
                if indexupdate.isnumeric():
                    indexupdate2 = int(indexupdate) 
                    if indexupdate2 not in products.keys():
                        print("\n\tMAAF, INDEX YANG ANDA MASUKKAN BELUM TERDAFTAR. MOHON MASUKKAN KEMBALI INDEX YANG SESUAI!")
                    else:
                        totalpenjualan = products[indexupdate2]['harga']*products[indexupdate2]['quantity']
                        print('''
                    =====================================================
                        * * * Memperbarui Data Penjualan * * *
                    =====================================================
            Menampilkan data penjualan dengan index : {}
            {}
            {} | {:<21} | {:<10} | {:<6} | {}
            {}
            {:>4}|{:<23}| Rp. {:<9}|{:<8}| Rp. {}
            {}'''.format(indexupdate2, border, "No.", "Nama Produk", "Harga Satuan", "Jumlah", "Total Penjualan", border, indexupdate2,
                        products[indexupdate2]['produk'], products[indexupdate2]['harga'], products[indexupdate2]['quantity'], totalpenjualan,border))
                        
                        updateproduk = input("\tApakah anda ingin memperbarui nama produk? (Y/N) : ")
                        if updateproduk.upper() == "Y":
                            gantiproduk = input("\tMasukkan nama produk : ")
                        elif updateproduk.upper() == "N":
                            gantiproduk = products[indexupdate2]['produk']
                        else :
                            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
                            break

                        updateharga = input("\tApakah anda ingin memperbarui harga satuan produk? (Y/N) : ")
                        if updateharga.upper() == "Y":
                            gantiharga = int(input("\tMasukkan harga satuan produk : "))
                        elif updateharga.upper() == "N": 
                            gantiharga = products[indexupdate2]['harga']
                        else :
                            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
                            break
                        
                        updatequantity = input("\tApakah anda ingin memperbarui jumlah produk yang terjual? (Y/N) : ")
                        if updatequantity.upper() == "Y":
                            gantiquantity = int(input("\tMasukkan jumlah produk yang terjual : "))
                        elif updatequantity.upper() == "N":
                            gantiquantity = products[indexupdate2]['quantity']
                        else :
                            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
                            break

                        print("\n\tDATA BERHASIL DIPERBARUI!")
                        products[indexupdate2]['produk'] = gantiproduk
                        products[indexupdate2]['harga'] = gantiharga
                        products[indexupdate2]['quantity'] = gantiquantity
                else:
                    print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
            elif option3b == 2:
                break
            else:
                print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
        else:
            print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
             
def deletedata():
    while True :
        option4 = input('''
            =====================================================
                   * * * Menghapus Data Penjualan * * *
            =====================================================
    Pilihan sub-menu :
    1. Hapus data penjualan
    2. Kembali ke Menu Utama

    Silahkan masukkan angka sesuai menu pilihan (1 atau 2) : ''')
        if option4.isnumeric():
            option4b = int(option4)
         
            if option4b == 1:
                indexdelete = input("""
        Masukkan index data yang ingin dihapus : """)
                if indexdelete.isnumeric():
                    indexdelete2 = int(indexdelete)
                    if indexdelete2 not in products.keys():
                        print("\n\tMAAF, INDEX YANG ANDA MASUKKAN BELUM TERDAFTAR. MOHON MASUKKAN KEMBALI INDEX YANG SESUAI!")
                    else:
                        datadelete = input("\tApakah anda yakin ingin menghapus data penjualan baru dengan index {}? (Y/N) :  "
                                            .format(indexdelete2))

                        if datadelete.upper() == "Y":
                            print("\n\tDATA PENJUALAN BERHASIL DIHAPUS!")
                            del products[indexdelete2]
                        elif datadelete.upper() == "N":
                            print("\n\tDATA PENJUALAN BATAL DIHAPUS!")
                        else :
                            print("\n\tMAAF, PENGHAPUSAN DATA PENJUALAN GAGAL!")
                else:
                    print("\n\tMAAF, PENGHAPUSAN DATA PENJUALAN GAGAL!")
            elif option4b == 2:
                break
            else :
                print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")
        else :
                print("\n\tMAAF, MENU YANG ANDA MASUKKAN SALAH. MOHON MASUKKAN PILIHAN MENU YANG SESUAI!")

while True:
    menuutama = input('''
            =====================================================
            =====================================================
                    * * * TOKO BUKU PURWADHIKA 24 * * *
            =====================================================
            
    Selamat datang! Anda berada pada program data penjualan Toko Buku Purwadhika.
    Pilihan menu :
    ------------------------------------------------------------
    1. Data Penjualan
    2. Menambahkan Data Penjualan
    3. Mengubah Data Penjualan
    4. Menghapus Data Penjualan
    5. Keluar
    ------------------------------------------------------------
    Silahkan masukkan angka sesuai menu pilihan (1 - 5) : ''')
        
    if (menuutama =='1') :
        daftarpenjualan()
    elif(menuutama=='2') :
        addingdata()
    elif(menuutama=='3') :
        updatedata()
    elif(menuutama=='4') :
        deletedata()
    elif(menuutama=='5') :
        print('''
        ---------------------------------------------------------------------
        Anda telah keluar dari program Data Penjualan Toko Buku Purwadhika 24
        ---------------------------------------------------------------------
                                    TERIMA KASIH!
        ---------------------------------------------------------------------
        ''')
        break