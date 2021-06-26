import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_perpus"
)


def insert_data(db):
    nama_buku = input("Masukan Nama Buku: ")
    pengarang = input("Masukan Nama Pengarang: ")
    jenis_buku = input("Masukan Jenis Buku: ")
    penerbit = input("Masukan Nama Penerbit: ")
    val = (nama_buku, pengarang,jenis_buku,penerbit)
    cursor = db.cursor()
    sql = "INSERT INTO tb_buku (judul_buku, pengarang, jenis_buku, penerbit) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM tb_buku"
  cursor.execute(sql)
  results = cursor.fetchall()

  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id_buku = input("Pili ID Buku")
  nama_buku = input("Masukan Nama Buku: ")
  pengarang = input("Masukan Nama Pengarang: ")
  jenis_buku = input("Masukan Jenis Buku: ")
  penerbit = input("Masukan Nama Penerbit: ")

  sql = "UPDATE tb_buku SET judul_buku=%s, pengarang=%s, jenis_buku=%s, penerbit=%s WHERE id_buku=%s"
  val = (nama_buku, pengarang, jenis_buku, penerbit, id_buku)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data berhasil Diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id_buku = input("Pili ID Buku")
  sql = "DELETE FROM tb_buku WHERE id_buku=%s"
  val = (id_buku,)
  cursor.execute(sql, val)
  db.commit()
  print("{} Data berhasil dihapus".format(cursor.rowcount))



def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)