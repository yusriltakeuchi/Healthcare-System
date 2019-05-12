# Healthcare-System
Tools yang berfungsi untuk melakukan crawling ribuan data penyakit beserta penyebab gejala-gejala yang terjadi. Kemudian nantinya akan membentuk sebuah database yang dapat dipanggil sewkatu-waktu.
Versi ini belum sempurna, karena tujuan dibuatnya untuk mendeteksi penyakit berdasarkan gejala-gejala yang ada. Tetapi tools ini hanya untuk membentuk struktur databasenya saja.

# Requirements
- Python3 installed on PC
- MySQL installed on PC

# Supported OS
- Windows
- Linux

# Installation
```
pip install -r requirements.txt
```

# Configuration
- Create database on MySQL with name healthcare or anything
- Import SQL from SQL Folder named healthcare.sql (if you want to use another database name, please change in healthcare.sql CREATE DATABASE IF NOT EXISTS 'YOUR DATABASE NAME')
- Open json2mysql.py file and edit connection string
```python
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='YOUR DATABASE NAME',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
```

# How to use
```
python health.py
```

## Note
This tool uses a caching system. For the first time it might take a little longer because the caching system is making data and depends on your internet connection.
However, the second search will be much faster

# Screenshot
### Example result when searching diseases
![alt text](https://i.imgur.com/AFbRaQe.png "Example result when searching diseases")


