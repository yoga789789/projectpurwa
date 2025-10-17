
from tabulate import tabulate

daftar_siswa = {
    '001': {'Nama': 'Andika', 'Kelas': 'YP70B', 'Nilai': 80, 'Status': 'Lulus'},
    '002': {'Nama': 'Dina', 'Kelas': 'YP70B', 'Nilai': 67, 'Status': 'Tidak Lulus'},
    '003': {'Nama': 'Ramzy', 'Kelas': 'YP70B', 'Nilai': 71, 'Status': 'Lulus'},
    '004': {'Nama': 'Zidane', 'Kelas': 'YP70B', 'Nilai': 54, 'Status': 'Tidak Lulus'}
}


def tampilkan_siswa():
    print('\n===Data Siswa YP70B===')
    data = []
    for siswa, nilai in daftar_siswa.items():
        data.append([siswa, nilai['Nama'], nilai['Kelas'], nilai['Nilai'], nilai['Status']])
    print(tabulate(data, headers=['NIS', 'Nama', 'Kelas', 'Nilai', 'Status'], tablefmt='grid'))

def tambah_siswa():
    while True:
        nis = input('Masukkan NIS:')
        if not nis.isdigit():
            print('NIS harus berupa angka.')
        elif nis in daftar_siswa:
            print('NIS sudah ada.')
        else:
            nama = input('Masukkan nama siswa:').capitalize()
            kelas = input(f'Masukkan kelas:')
            while True:
                nilai = int(input('Masukkan nilai (0-100):'))
                if 0 <= nilai <= 100:
                    break
                else:
                    print('Nilai harus antara 0 sampai 100.')
            if nilai >= 70:
                status = 'Lulus'
            else:
                status = 'Tidak Lulus'

            daftar_siswa[nis] = {'Nama': nama, 'Kelas': kelas, 'Nilai': nilai, 'Status': status}
            print('Siswa berhasil ditambahkan')
            break

    tampilkan_siswa()

def update_data():
    while True:
        nis = input('Masukkan NIS yang ingin di-update:')
        if not nis.isdigit():
            print('NIS harus berupa angka.')
            continue
        elif nis not in daftar_siswa:
            print('NIS tidak ditemukan.')
            continue
        else:
            siswa = daftar_siswa[nis]
            print(f'\nData terkini untuk NIS {nis}')
            print(f"Nama: {siswa['Nama']}")
            print(f"Kelas: {siswa['Kelas']}")
            print(f"Nilai: {siswa['Nilai']}")
            print(f"Status: {siswa['Status']}\n")

            print('Apa yang ingin di-update?')
            print('1. Nama')
            print('2. Kelas')
            print('3. Nilai')
            print('4. Batalkan')

            pilihan = input("Masukkan pilihan (1-4):")

            if pilihan == '1':
                nama_baru = input('Masukkan nama baru:').capitalize()
                siswa['Nama'] = nama_baru
                print('Nama berhasil diperbarui.')

            elif pilihan == '2':
                kelas_baru = input('Masukkan kelas baru:')
                siswa['Kelas'] = kelas_baru
                print('Kelas berhasil diperbarui.')

            elif pilihan == '3':
                while True:
                    nilai_baru = input('Masukkan nilai baru:')
                    if not nilai_baru.isdigit():
                        print('Input harus angka')
                        continue
                    nilai_baru = int(nilai_baru)
                    if 0 <= nilai_baru <= 100:
                        siswa['Nilai'] = nilai_baru
                        siswa['Status'] = 'Lulus' if nilai_baru >= 70 else 'Tidak Lulus'
                        print('Nilai berhasil diperbarui.')
                        break
                    else:
                        print('Nilai harus antara 0 dan 100.')

            elif pilihan == '4':
                print('Update dibatalkan')

            else:
                print('Pilihan tidak valid')
                continue
            print(f"\nData terbaru untuk NIS {nis}:")
            print(f"Nama: {siswa['Nama']}")
            print(f"Kelas: {siswa['Kelas']}")
            print(f"Nilai: {siswa['Nilai']}")
            print(f"Status: {siswa['Status']}\n")
            
            tampilkan_siswa()
            while True:
                update_lagi = (input("\nMau perbarui data lagi? (ya/tidak): ")).lower()
                if update_lagi == "ya":
                    ubah_data = True
                    break
                elif update_lagi == "tidak":
                    ubah_data = False
                    break
                else:
                    print("Input tidak valid! Hanya boleh 'ya' atau 'tidak'.")
                
            if ubah_data:
                continue
            else:
                break
    tampilkan_siswa()
                
def hapus_siswa():
    tampilkan_siswa()
    hapus = input('Masukkan NIS yang ingin dihapus:')
    if hapus in daftar_siswa:
        del daftar_siswa[hapus]
        print(f'{hapus} berhasil dihapus.')
    else:
        print('NIS tidak ditemukan.')
    tampilkan_siswa()

def cari_siswa():
    keyword = input("Masukkan nama yang ingin dicari:").capitalize()
    hasil = []
    for nis, data in daftar_siswa.items():
        if keyword in data['Nama']:
            hasil.append([nis, data['Nama'], data['Kelas'], data['Nilai'], data['Status']])
    if hasil:
        print(tabulate(hasil, headers=['NIS', 'Nama', 'Kelas', 'Nilai', 'Status'], tablefmt='grid'))
    else:
        print("Siswa tidak ditemukan.")

def menu_utama():
    while True:
        print('\nData Nilai Siswa')
        print('1. Daftar siswa')
        print('2. Tambah siswa')
        print('3. Ubah data siswa')
        print('4. Hapus data siswa')
        print('5. Cari siswa')
        print('6. Exit program')

        pilihan = input('Masukkan angka Menu (1-6):')
        
        if pilihan == '1':
            tampilkan_siswa()
        elif pilihan == '2':
            tambah_siswa()
        elif pilihan == '3':
            update_data()
        elif pilihan == '4':
            hapus_siswa()
        elif pilihan == '5':
            cari_siswa()
        elif pilihan == '6':
            print('Terima kasih sudah memakai program ini.')
            break
        else:
            print('Input tidak valid.')

menu_utama()