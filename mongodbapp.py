import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db_perpus"]
collections = db["tb_buku"]


nama_buku = input("Masukan Nama Buku: ")
pengarang = input("Masukan Nama Pengarang: ")
jenis_buku = input("Masukan Jenis Buku: ")
penerbit = input("Masukan Nama Penerbit: ")
data = {"judul_buku":nama_buku, "pengarang" :pengarang, "jenis_buku":jenis_buku, "penerbit":penerbit }
x = collections.insert_one(data)
print(x.inserted_id)

