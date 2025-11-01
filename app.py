from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId # Untuk mengelola ID unik Mongo
import os

app = Flask(__name__)

# --- Konfigurasi Database ---
# Terhubung ke MongoDB yang berjalan di localhost (VM)
app.config["MONGO_URI"] = "mongodb://localhost:27017/swalayanDB"
mongo = PyMongo(app)

# Tentukan koleksi (tabel) yang akan digunakan
produk_collection = mongo.db.produk

# --- FUNGSI CRUD (Create, Read, Update, Delete) ---

# 1. CREATE: Menambah produk baru
@app.route('/produk', methods=['POST'])
def create_produk():
    data = request.json
    
    # Menggunakan key dengan huruf kapital
    nama_produk = data.get('Nama_Produk')
    harga = data.get('Harga')
    stok = data.get('Stok')

    if not nama_produk or not harga or stok is None:
        return jsonify({'error': 'Data tidak lengkap (Nama_Produk, Harga, Stok)'}), 400
        
    produk_id = produk_collection.insert_one({
        # Menyimpan ke DB dengan key huruf kapital
        'Nama_Produk': nama_produk,
        'Harga': harga,
        'Stok': stok
    }).inserted_id
    
    return jsonify({'message': 'Produk berhasil ditambahkan', 'id': str(produk_id)}), 201

# 2. READ: Menampilkan semua produk
@app.route('/produk', methods=['GET'])
def get_semua_produk():
    semua_produk = []
    for produk in produk_collection.find():
        semua_produk.append({
            'id': str(produk['_id']),
            # Membaca dari DB dengan key huruf kapital
            'Nama_Produk': produk['Nama_Produk'],
            'Harga': produk['Harga'],
            'Stok': produk['Stok']
        })
    return jsonify(semua_produk), 200

# 3. UPDATE: Mengubah data produk berdasarkan ID
@app.route('/produk/<id>', methods=['PUT'])
def update_produk(id):
    try:
        data = request.json
        
        # Cek data apa saja yang dikirim untuk di-update
        update_data = {}
        if 'Nama_Produk' in data:
            update_data['Nama_Produk'] = data['Nama_Produk']
        if 'Harga' in data:
            update_data['Harga'] = data['Harga']
        if 'Stok' in data:
            update_data['Stok'] = data['Stok']

        result = produk_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': update_data}
        )
        
        if result.matched_count == 0:
            return jsonify({'error': 'Produk tidak ditemukan'}), 404
            
        return jsonify({'message': 'Data produk berhasil diupdate'}), 200
    except Exception as e:
        return jsonify({'error': 'ID tidak valid atau data salah', 'detail': str(e)}), 400

# 4. DELETE: Menghapus produk berdasarkan ID
@app.route('/produk/<id>', methods=['DELETE'])
def delete_produk(id):
    try:
        result = produk_collection.delete_one({'_id': ObjectId(id)})
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Produk tidak ditemukan'}), 404
            
        return jsonify({'message': 'Produk berhasil dihapus'}), 200
    except Exception as e:
        return jsonify({'error': 'ID tidak valid', 'detail': str(e)}), 400

# --- Jalankan Server ---
if __name__ == "__main__":
    # Gunakan host="0.0.0.0" agar bisa diakses dari luar VM
    app.run(host="0.0.0.0", port=5000, debug=True)
