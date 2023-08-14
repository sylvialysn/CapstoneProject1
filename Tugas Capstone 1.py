#Yellow Pages database
yp = {'JR1':{'Kota':'Jakarta Utara','Jenis Bisnis':'Restoran inggris'
             ,'Nama Bisnis' : 'Mcdonald','Alamat Lengkap':'Jalan Danau Sunter Utara 1 14350'
             ,'Nomor telepon': '+62 216402570','Website':'http://www.mcdonalds.co.id/'
             ,'Products':{0:{'nama':'apple pie', 'stok':30,'harga' :7500}, 1:{'nama':'happy meal', 'stok':3,'harga' :500000}}}
    ,'TR2': {'Kota':'Jakarta Barat','Jenis Bisnis':'Restoran padang'
             ,'Nama Bisnis': 'RM Sederhana','Alamat Lengkap':'Jln.Palem Raja Raya,Panunggangan Barat,Cibodas 15138'
             ,'Nomor telepon':'+62 2155793000','Website':'https://www.restoransederhana.id/'
             ,'Products':{0:{'nama':'ayam gulai', 'stok':100,'harga' :10000}}}
    ,'BP3': {'Kota':'Balikpapan','Jenis Bisnis':'Pusat Perlengkapan'
             ,'Nama Bisnis': 'Ace Hardware','Alamat Lengkap':'Jalan Mulawarman 2, Damai, Balikpapan Kota 76114'
             ,'Nomor telepon':'+62 542443311','Website':'https://www.acehardware.co.id/'
             ,'Products':{0:{'nama':'Philips 10W', 'stok':500,'harga' :30000}}}
    }
belanjaan = []


#FUNGSI 1 : untuk memunculkan informasi umum setelah melakukan pencarian
def generalinfo(indeks): 
    print(f"Informasi umum :\n{yp[indeks]['Nama Bisnis']} merupakan {yp[indeks]['Jenis Bisnis']}. Bisnis ini terletak di {yp[indeks]['Kota']}.\nUntuk informasi lebih lanjut, silahkan kontak {yp[indeks]['Nomor telepon']}\nAlamat bisnis tersebut adalah {yp[indeks]['Alamat Lengkap']}.\nSelain menghubungi nomor telepon, anda dapat mengunjungi link : {yp[indeks]['Website']}\n")


#FUNGSI 2 : memunculkan bisnis berdasarkan kode (huruf depan daerah+ huruf depan jenis bisnis + nomor urut) yang ada pada database
def tabelnotelp(namatabel):
    print('Tabel Nomor Telepon')
    print('Index\t|Kode Bisnis\t|Kota\t\t\t|Jenis Bisnis\t\t\t|Nama Bisnis\t|')
    for i,a in zip(namatabel,range(0,len(namatabel))):
        print(f'{a}\t|{i}\t\t|{namatabel[i]["Kota"]}\t\t|{namatabel[i]["Jenis Bisnis"]}\t\t|{namatabel[i]["Nama Bisnis"]}\t|')


#FUNGSI 3 : untuk memunculkan produk bisnis
def tabelproduk(nt,ind):
    print('Index\t|Nama Produk\t|Stok\t|Harga\t|')
    for i in range(0,len(nt[ind]['Products'])):
        print(f"{i}\t|{nt[ind]['Products'][i]['nama']}\t|{nt[ind]['Products'][i]['stok']}\t|{nt[ind]['Products'][i]['harga']}\t|")

#FUNGSI 4 : untuk memunculkan hasil update 
def hasilupdate(nt,ind):
    print('Hasil Update Produk')
    tabelproduk(nt,ind)

    
#FUNGSI 5 : untuk belanja produk
def belanjaproduk():
    print(f"Berikut Etalase {yp[i]['Nama Bisnis']}:")
    print("Index\t|Nama\t\t|Stok\t|Harga\t|")
    indeksan = []
    for a in range(0,len(yp[i]['Products'])):
        print(f"{a}\t|{yp[i]['Products'][a]['nama']}\t|{yp[i]['Products'][a]['stok']}\t|{yp[i]['Products'][a]['harga']}\t|")
        indeksan.append(a)
        continue
                    
    while True: 
        try:
            inginbeli = int(input('Masukkan index produk yang ingin di beli (contoh, 1): '))
            if inginbeli not in indeksan:
                print('Indeks yang anda masukkan tidak sesuai')
                continue

            stokbeli = int(input('Masukkan jumlah yang ingin dibeli : '))
            if stokbeli > yp[i]['Products'][inginbeli]['stok']:
                print('Maaf Stok tidak mencukupi')
                continue
            elif stokbeli<= yp[i]['Products'][inginbeli]['stok']:
                belanjaan.append([inginbeli,yp[i]['Products'][inginbeli]['nama'],stokbeli,yp[i]['Products'][inginbeli]['harga']*stokbeli])

            masihmau = input('Masih ingin beli atau sudah cukup? (masih/tidak) ')            
            if masihmau == 'tidak':
                break   
        except ValueError:
            print('Mohon masukkan input berupa angka')

    print('\nRangkuman Pesananmu')
    print('Nama Produk\t|Jumlah Produk\t|Harga\t')
    for m in range(0,len(belanjaan)) :
        print(f"{belanjaan[m][1]}\t|{belanjaan[m][2]}\t\t|{belanjaan[m][3]}\t")
        
    #Untuk menjumlahkan total belanjaan
    total = 0
    for s in range(0,len(belanjaan)) :
        total += int(belanjaan[s][3])
    
    #Untuk mengurangi stok barang yang ada         
    yp[i]['Products'][belanjaan[s][0]]['stok'] -= belanjaan[s][2]
    print(f'\nTotal yang harus dibayarkan adalah {total}')
                
    while True : 
        try:
            uangmu = int(input("Masukkan Jumlah Uang Untuk Pembayaran : "))
            if uangmu > total :
                print(f"Transaksi berhasil\nUang Kembalimu Adalah :{uangmu-total}\nTerimakasih\n")
                print('Kembali ke menu utama\n')
                belanjaan.clear()
                indeksan.clear()
                break
            elif uangmu == total:
                print('Transaksimu berhasil\nTerima kasih\n')
                print('Kembali ke menu utama')
                belanjaan.clear()
                indeksan.clear()
                break
            else : 
                print('Maaf Jumlah tidak cukup') 
        except ValueError:
            print('Input harus berupa angka saja, silahkan coba kembali')

#FUNGSI 6 : untuk menambah produk
def menambahproduk():
    tabelproduk(yp,kodebis)
    NP= input('Masukkan Nama Produk: ')
    Stok=int(input('Masukkan Jumlah Stok: '))
    Hg = int(input('Masukkan Harga Produk: '))
    yp[kodebis]['Products'][len(yp[kodebis]['Products'])]={'nama':NP,'stok':Stok,'harga':Hg}
    hasilupdate(yp,kodebis)

#FUNGSI 7 : untuk menghapus produk
def menghapusproduk():
    tabelproduk(yp,kodebis)
    indeks = int(input('Masukkan index produk: '))
    del yp[kodebis]['Products'][indeks]
    yp[kodebis]['Products'] = dict(zip(range(0,len(yp[kodebis]['Products'])), list(yp[kodebis]['Products'].values())))
    hasilupdate(yp,kodebis)

#FUNGSI 8 : untuk mengedit produk
def editproduk():
    tabelproduk(yp,kodebis)
    if kodebis in yp:
        while True:
            editapa = input('Apakah yang ingin anda edit? (nama/stok/harga) ').lower()
            if editapa == 'nama' :
                indeks = int(input('Masukkan index produk: '))
                nama2 = input('Masukkan nama pengganti: ')
                yp[kodebis]['Products'][indeks]['nama']= nama2
                hasilupdate(yp,kodebis)
                break

            elif editapa == 'stok' :
                indeks = int(input('Masukkan index produk: '))
                stokakhir = int(input('Masukkan Jumlah Stok Yang Sebenarnya: '))
                yp[kodebis]['Products'][indeks]['stok']= stokakhir
                hasilupdate(yp,kodebis)
                break

            elif editapa == 'harga' :
                indeks = int(input('Masukkan index produk: '))
                harga2 = int(input('Masukkan Harga Yang Sebenarnya: '))
                yp[kodebis]['Products'][indeks]['harga']= harga2
                hasilupdate(yp,kodebis)
                break
            else:
                print('Mohon Masukkan nama/harga/stok')
            
            
            

while True :
    print('Selamat Datang di Yellow Pages Indonesia\n')
    print('Berikut Menu yang dapat anda pilih:\n1.Mencari Nomor Telepon dan Membeli Produk\n2.Menambahkan atau Menghapus Nomor Telepon\n3.Menambahkan, Menghapus, atau Mengedit Produk Salah Satu Bisnis\n4.Keluar dari Program\n')
    nomenu = input('Masukkan menu yang ingin dipilih :')
    # MENU 1 : Mencari Nomor Telepon dan Membeli Produk
    if nomenu == '1' :
        jenisbisnis = input('\nMasukkan Jenis Bisnis yang Dicari(cth Restoran, - jika tidak diketahui): ').capitalize()
        kota = input('Masukkan Daerah Bisnis yang Dicari(cth Jakarta Selatan,  - jika tidak diketahui): ').capitalize()
        nama = input('Masukkan Nama Bisnis yang Dicari(cth Mcdonald, - jika tidak diketahui): ').capitalize()
        print('\n\nBerikut Hasil Pencarianmu')
        for i in yp:
            if jenisbisnis in yp[i]['Jenis Bisnis'] or kota in yp[i]['Kota'] or nama in yp[i]['Nama Bisnis']:
                print(f"{i}\t|{yp[i]['Nama Bisnis']}\t\t|{yp[i]['Jenis Bisnis']}\t|{yp[i]['Kota']}\t|{yp[i]['Nomor telepon']}\t|")
                                 
            elif jenisbisnis == '-' and kota =='-' and nama =='-':
                tabelnotelp(yp)
                break
                
        Kodebisnis = input('\nMasukkan Kode Bisnis untuk Informasi Lebih Lanjut (cth JR1): ')
        for i in yp:
            if Kodebisnis == i :
                generalinfo(i)
                jawab= input(f"Apakah anda ingin membeli sesuatu di {yp[i]['Nama Bisnis']}?(ya/tidak) ")
                if jawab == 'ya':
                    if 0 in yp[i]['Products']:
                        belanjaproduk()
                    else :
                        print('Maaf bisnis ini tidak menjual apa-apa')
                        break
                elif jawab == 'tidak':
                    break
            
                
    # MENU 2 : Menambahkan atau Menghapus Bisnis Baru
    elif nomenu == '2' : 
        jawab2 = input('Apakah anda ingin menambahkan atau menghapus sebuah bisnis baru (tambah/hapus) ? ').lower()
        if jawab2 == 'tambah':
            Ka = input("Masukkan Kota Asal (contoh, Jakarta Utara): ")
            Jb = input("Masukkan Jenis Bisnis (contoh, Pusat Perlengkapan) : ")
            Nb = input('Masukkan Nama Bisnis (contoh, Mcdonald) : ')
            AL = input("Masukkan Alamat Lengkap (contoh, Jln Iskandar muda....) : ")
            NT = input("Masukkan Nomor Telepon (contoh, 0812-1233-111): ")
            Web = input("Masukkan Websitemu (contoh: www.mcdonald.com): ")
            Pert = input("Apakah anda ingin menjual produk anda (ya/tidak) : ")
            if Pert == 'ya' :
                NP = input("Masukkan nama Produk : ")
                Stok = int(input("Masukkan Stok : "))
                Hg = int(input("Masukkan Harga : "))
                unik = Ka[0]+Jb[0]+str(len(yp)+1)
                yp[unik] = {'Kota':Ka,'Jenis Bisnis':Jb,'Nama Bisnis' :Nb ,'Alamat Lengkap':AL,'Nomor telepon': NT,'Website':Web,'Products':{0:{'nama':NP, 'stok':Stok,'harga' :Hg}}}
                print(f'Baik data sudah masuk, kodemu adalah {unik}')
                print('Kembali ke menu utama\n')
            elif Pert =='tidak':
                unik = Ka[0]+Jb[0]+str(len(yp)+1)
                yp[unik] = {'Kota':Ka,'Jenis Bisnis':Jb,'Nama Bisnis' :Nb ,'Alamat Lengkap':AL,'Nomor telepon': NT,'Website':Web,'Products':{}}
                print(f'Baik data sudah masuk, kodemu adalah {unik}')
                print('Kembali ke menu utama\n')
        elif jawab2 == 'hapus':
            tabelnotelp(yp)
            maudlt = input('Masukkan kode bisnis yang ingin dihapus : ')
            print(f'Baik, bisnis dengan kode {maudlt} sudah dihapus')
            print('Kembali ke menu utama\n')
            del yp[maudlt]

        else : 
            break

    # MENU 3 : Menambahkan, Menghapus, atau Mengedit Produk Salah Satu Bisnis    
    elif nomenu == '3' : 
        tabelnotelp(yp)
        while True:
            jawab = input('Apakah anda ingin menambahkan, menghapus, atau mengedit stok sebuah produk?(tambah/hapus/edit) ').lower()
            if jawab == 'tambah': 
                while True :
                    kodebis = input('Masukkan kode bisnis: ').upper()
                    if kodebis in yp:
                        menambahproduk()
                        break
                    else :
                        print('Mohon masukkan kode bisnis yang ada')
                print('Kembali ke menu utama\n')
                break
            elif jawab == 'hapus':
                while True :
                    kodebis = input('Masukkan kode bisnis: ').upper()
                    if kodebis in yp :
                        menghapusproduk()
                        break
                    else :
                        print('Mohon masukkan kode bisnis yang ada')
                print('Kembali ke menu utama\n')
                break
            elif jawab == 'edit':
                while True:
                    kodebis = input('Masukkan kode bisnis: ').upper()
                    if kodebis in yp:
                        editproduk()
                        break
                    else :
                        print('Mohon masukkan kode bisnis yang ada')
                print('Kembali ke menu utama\n')
                break
            else :
                print('Mohon masukkan edit/hapus/tambah')

    # MENU 4 : Untuk Keluar Dari Program        
    elif nomenu == '4' :  
        print('Terima kasih sudah menggunakan layanan kami')
        break
    # Untuk mengurus input yang tidak ada pada menu 
    else:
        print('\nMasukkan Nomor Menu Yang Tersedia\n')

