import mysql.connector

dtb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "toko_a"
)

cursor = dtb.cursor()
sql = """CREATE TABLE kontak (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(50),
        number INT  (20)
        )"""
try:
    cursor.execute(sql)
    dtb.commit()
    print("Create table successfully!")
except mysql.connector.Error as err:
    print("Error:", err)

def create(name, number):
    query = "INSERT INTO kontak (nama, number) VALUES (%s, %s)"
    value = (name, number)
    cursor.execute(query, value)
    dtb.commit()

def read():
    query = ("SELECT * FROM kontak")
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print( f"{x[0]}. nama : {x[1]}, nomor : {x[2]}")
        # database tuh bentuknya tuple beda sama list yang kalo akses harus pake nomor urut atau indekss

def update(id, name, number):
    query = ("UPDATE kontak SET nama = %s, number = %s WHERE id = %s")
    value = (name, number, id)
    cursor.execute(query, value)
    dtb.commit()

def delete(id):
    query = ("DELETE FROM kontak WHERE id = %s")
    value = (id,)
    cursor.execute(query, value)
    dtb.commit

while True:
    print("""
        MENU PILIHAN
        1. create
        2. read
        3. update
        4. delete
    """)
    choice = int(input("masukan pilihan : "))

    if choice == 1:
        name = input("masukan nama kontak yang ingin anda buat (ketik 'exit' untuk keluar): ")
        while True:
            if name == "exit":
                break
            number = int(input("masukan nomor :"))
            create(name, number)
            break

    elif choice == 2:
        read()

    elif choice == 3:
        while True:
            number_id = input("Masukan nomor berapa yang ingin dirubah (ketik 'exit' untuk keluar): ")
            if number_id == 'exit' :
                break
            nama_baru = str(input("Masukan nama baru : "))
            nomor_baru = int(input("Masukan nomor baru : "))
            update(number_id, nama_baru, nomor_baru)
    elif choice == 4:
        while True:
            number_id = input("Masukan nomor berapa yang ingin dihapus (ketik 'exit' untuk keluar):")
            if number_id == "exit":
                break
            delete(number_id)
    else :
        break
