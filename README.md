# Cloud Computing Lab 1 — Flask & MongoDB Monolithic VM Service

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> A lightweight RESTful API service built with **Flask** and **MongoDB** engineered for Virtual Machine (VM) cloud infrastructure deployment.

---

## 📌 Overview

**Project-1-Cloud-Computing** is a cloud computing lab implementation demonstrating monolithic micro-service architecture on a virtual machine (VM). The project provides CRUD REST endpoints managing inventory data stored in a local MongoDB database instance (`swalayanDB`).

---

## ✨ Key Features

- ⚡ **RESTful Inventory Endpoints**: Complete CRUD lifecycle for product management (`Nama_Produk`, `Harga`, `Stok`).
- 🍃 **Flask-PyMongo Integration**: Asynchronous NoSQL database queries using PyMongo and BSON ObjectIDs.
- 🌐 **Cloud VM Ready**: Pre-configured to bind on `0.0.0.0:5000` for external cloud security group / firewall routing.

---

## 🛠️ Tech Stack

**Core Framework & Language**
- Python 3.10+
- Flask (Micro Microservice Framework)

**Database Layer**
- MongoDB (NoSQL Database)
- PyMongo & BSON (`flask_pymongo`)

---

## 📡 REST API Directory

| Method | Endpoint | Description | Request Payload |
| :--- | :--- | :--- | :--- |
| `POST` | `/produk` | Create a new inventory record | `{"Nama_Produk": "String", "Harga": Number, "Stok": Number}` |
| `GET` | `/produk` | Retrieve all inventory items | *None* |
| `PUT` | `/produk/<id>` | Update an inventory item by BSON ID | `{"Nama_Produk": "...", "Harga": ...}` |
| `DELETE` | `/produk/<id>` | Remove an inventory item by BSON ID | *None* |

---

## 📂 Project Structure

```text
Project-1-Cloud-Computing/
├── app.py                    # Flask application entry point & API endpoints
├── LICENSE                   # MIT License
└── README.md                 # Project Documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- MongoDB instance running on `localhost:27017`

### Local Execution

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RaihanHadriansyah21/Project-1-Cloud-Computing.git
   cd Project-1-Cloud-Computing
   ```

2. **Install Dependencies**:
   ```bash
   pip install flask flask-pymongo pymongo
   ```

3. **Start Flask Server**:
   ```bash
   python app.py
   ```
   Server will launch at `http://0.0.0.0:5000`.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
