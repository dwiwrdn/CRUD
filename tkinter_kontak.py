import tkinter as tk
import mysql.connector

class KontakApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kontak Database")

        # Koneksi Database
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "toko_a"
        )
        self.cursor =  self.conn.cursor()


        # GUI elemen

        self.nama_label = tk.Label(self, text="Nama:")
        self.nama_entry = tk.Entry(self)
        self.nomor_label = tk.Label(self, text="Nomor:")
        self.nomor_entry = tk.Entry(self)
        self.add_button = tk.Button(self, text="Tambahkan Kontak", command=self.add_kontak)
        self.kontak_listbox = tk.Listbox(self)

        # Layout 
        self.nama_label.grid(row=0, column=0)
        self.nama_entry.grid(row=0, column=1)
        self.nomor_label.grid(row=1, column=0)
        self.nomor_entry.grid(row=1, column=1)
        self.add_button.grid(row=3, columnspan=2)
        self.kontak_listbox.grid(row=4, columnspan=2)

        # Event handlers
        self.kontak_listbox.bind("<Double-1>", self.edit_contact)

    def add_kontak(self):
        """ menambahkan kontak baru ke database dan memperbarui tampilan listbox.
        
        langkah_langkah:
        1. mengambbil data dari entry fields
        2. menyisipkan data ke dalam tabel 'kontak' di database
        3. memperbarui tampilan listbox untuk menampilkan kontak tersebut
        """
        nama = self.nama_entry.get()
        nomor_telepon = self.nomor_entry.get()

        # Menyisipkan data ke dalam database
        self.cursor.execute("INSERT INTO kontak (nama, number) VALUES (%s, %s)", 
                            (nama, nomor_telepon))
        self.conn.commit()

        # Memperbarui tampilan listbox
        self.kontak_listbox.delete(0, tk.END) #Menghapus semua item yang ada
        self.cursor.execute("SELECT * FROM kontak") #Mengambil semua data dari tabel
        for row in self.cursor.fetchall():
            self.kontak_listbox.insert(tk.END, row)

        # Membersihkan entry fields
        self.nama_entry.delete(0, tk.END)
        self.nomor_entry.delete(0, tk.END)

    def edit_contact(self, event):
        # ... (get selected contact, populate fields, enable editing)
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]  # Get the index of the selected item
            contact = self.cursor.execute("SELECT * FROM contacts WHERE id=?", (selected_index,)).fetchone()
            if contact:
                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, contact[1])  # Assuming 'name' is at index 1
                # ... (populate other fields similarly)
                self.edit_mode = True  # Set a flag to indicate edit mode
                self.add_button.config(text="Save Changes")

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = KontakApp()
    app.run()