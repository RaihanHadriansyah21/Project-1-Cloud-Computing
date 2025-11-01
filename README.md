# Project 1 Cloud Computing - Toko Swalayan (Monolithic)

Ini adalah implementasi tugas No. 6: Aplikasi CRUD Monolithic di VM dengan NoSQL.

- **Platform:** Monolithic (VM)
- **Database:** MongoDB
- **Aplikasi:** Flask (Python)

## Cara Menjalankan

1.  Pastikan MongoDB sudah terinstal dan berjalan (`sudo systemctl start mongod`).
2.  Pastikan `flask` dan `flask_pymongo` sudah terinstal (`pip install flask flask_pymongo`).
3.  Jalankan server: `python3 app.py`
4.  Konfigurasi Port Forwarding di VM (Host 5000 -> Guest 5000) untuk mengakses dari host.

## Endpoint API

- `POST /produk`: Membuat produk baru.
- `GET /produk`: Membaca semua produk.
- `PUT /produk/<id>`: Memperbarui produk.
- `DELETE /produk/<id>`: Menghapus produk.
