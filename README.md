# 🧮 Data Nilai Siswa – Capstone Project Python

## 📋 Deskripsi Proyek
Program **Data Nilai Siswa** ini dibuat sebagai bagian dari **Capstone Project Python – Modul 1**.  
Tujuan dari program ini adalah untuk membantu guru atau admin sekolah dalam **mengelola data nilai siswa** secara sederhana melalui **terminal**.  
Program ini dibuat menggunakan bahasa **Python** dan berjalan berbasis **CLI (Command Line Interface)**.

Program ini memiliki fitur utama **CRUD (Create, Read, Update, Delete)** serta **fitur tambahan pencarian data siswa**.  
Selain itu, semua data ditampilkan dengan format tabel menggunakan library `tabulate` agar hasil lebih rapi dan mudah dibaca.

---

## 🚀 Fitur Utama
| Fitur | Deskripsi | Komponen Python |
|-------|------------|----------------|
| **Create (Tambah Data)** | Menambahkan data siswa baru dengan validasi input (NIS unik, nilai 0–100). | `while`, `if-else`, dictionary |
| **Read (Tampilkan Data)** | Menampilkan seluruh data siswa dalam bentuk tabel rapi. | `for loop`, `tabulate` |
| **Update (Ubah Data)** | Mengubah nama, kelas, atau nilai siswa tertentu. | nested `while`, `if-elif`, validasi |
| **Delete (Hapus Data)** | Menghapus data siswa berdasarkan NIS. | `if in`, `del`, dictionary |
| **Search (Cari Data)** | Mencari siswa berdasarkan nama. | `for loop`, `if in`, list append |

---

## 🧠 Struktur Data
Semua data siswa disimpan dalam sebuah **dictionary** bernama `daftar_siswa`,  
dengan format sebagai berikut:
```python
daftar_siswa = {
    '001': {'Nama': 'Andika', 'Kelas': 'YP70B', 'Nilai': 80, 'Status': 'Lulus'},
    '002': {'Nama': 'Dina', 'Kelas': 'YP70B', 'Nilai': 67, 'Status': 'Tidak Lulus'}
}
```

Setiap **key utama** adalah NIS (Nomor Induk Siswa),  
dan **value-nya** adalah dictionary berisi:
- `Nama` → Nama siswa  
- `Kelas` → Kelas siswa  
- `Nilai` → Nilai ujian  
- `Status` → Status kelulusan otomatis (Lulus/Tidak Lulus)

---

## 🧩 Fungsi Utama dalam Program

### 1️⃣ `tampilkan_siswa()`
Menampilkan seluruh data siswa dalam bentuk tabel menggunakan library `tabulate`.

### 2️⃣ `tambah_siswa()`
Menambahkan data baru dengan validasi:
- NIS harus berupa angka dan belum terdaftar.  
- Nilai harus di antara 0–100.  
- Status kelulusan otomatis berdasarkan nilai.

### 3️⃣ `update_data()`
Mengubah nama, kelas, atau nilai siswa tertentu.  
Jika nilai diubah, status kelulusan diperbarui secara otomatis.  
Terdapat validasi input dan pilihan untuk memperbarui data lagi tanpa keluar dari menu.

### 4️⃣ `hapus_siswa()`
Menghapus data siswa berdasarkan NIS dengan konfirmasi dan tampilan hasil akhir.

### 5️⃣ `cari_siswa()`
Mencari siswa berdasarkan nama (dapat sebagian huruf) dan menampilkan hasil pencarian dalam bentuk tabel.

### 6️⃣ `menu_utama()`
Menampilkan menu interaktif yang menghubungkan seluruh fitur.  
Menggunakan loop agar program terus berjalan sampai user memilih keluar.

---

## 🖥️ Cara Menjalankan Program
1. Pastikan Python sudah terinstal di perangkat Anda.  
   Versi yang disarankan: **Python 3.10 atau lebih baru**.

2. Install library `tabulate` terlebih dahulu:
   ```bash
   pip install tabulate
   ```

3. Jalankan file program di terminal:
   ```bash
   python data_nilai_siswa.py
   ```

4. Pilih menu sesuai kebutuhan:
   ```
   1. Daftar siswa
   2. Tambah siswa
   3. Ubah data siswa
   4. Hapus data siswa
   5. Cari siswa
   6. Exit program
   ```

---

## 📸 Contoh Output
```
===Data Siswa YP70B===
+-------+---------+---------+---------+---------------+
|  NIS  | Nama    | Kelas   | Nilai   | Status        |
+=======+=========+=========+=========+===============+
| 001   | Andika  | YP70B   | 80      | Lulus         |
| 002   | Dina    | YP70B   | 67      | Tidak Lulus   |
| 003   | Ramzy   | YP70B   | 71      | Lulus         |
+-------+---------+---------+---------+---------------+
```

---

## 🧩 Teknologi yang Digunakan
- **Python 3** (Core logic)
- **Tabulate** → Untuk menampilkan tabel rapi di terminal
- **Dictionary & Looping** → Struktur utama data dan logika kontrol
- **Conditional Statements** → Validasi input dan penentuan status kelulusan

---

## 🏁 Kesimpulan
Program ini berhasil mengimplementasikan konsep dasar Python seperti:
- **Collection Data Type (Dictionary)**
- **Loop dan Conditional Statement**
- **Function dengan parameter dan return value**
- **Validasi input user**
- **Struktur program modular dan maintainable**

Dengan tambahan fitur pencarian dan validasi nilai,  
program ini memiliki tingkat kompleksitas lebih tinggi dibanding contoh dasar CRUD.

---

## 🧑‍💻 Author
**Nama:** Yoga Brahma  
**Kelas:** Purwadhika – Python Fundamental  
**Project:** Capstone Project Modul 1  
**Tanggal:** Oktober 2025  
