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
        print(x)

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

    else :
        break
    #elif choice == 2:
   #     pass
  #  elif choice == 3:
 #       pass
#    elif choice == 4:
#        pass