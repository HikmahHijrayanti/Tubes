import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
from tkinter import ttk

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("800x600")

page1= tk.Frame(window)
page2= tk.Frame(window)
page3= tk.Frame(window)
page4= tk.Frame(window)
page5= tk.Frame(window)
page6= tk.Frame(window)

for frame in (page1,page2,page3,page4,page5,page6):
    frame.grid(row=0,column=0,sticky="nsew")

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

################################################### Page 1 ##############################################################
page1.config(background="#e6e6e6")

content_frame = tk.Frame(page1, bg="#e6e6e6")
content_frame.pack(side="top", fill="both", expand=True)

bg_image = tk.PhotoImage(file="Page1G.png")
bg_label = tk.Label(content_frame, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

start_button = tk.Button(content_frame, text="Get Started", font=("Candara", 16), fg="white", bg="#333333", activebackground="#333333", padx=20, pady=10, bd=0, command=lambda: show_frame(page2))
start_button.place(relx=0.52, rely=0.8, anchor="center")

####################################################### PAGE 2 #######################################################
page2.config(background="#e6e6e6")
bg2 = PhotoImage(file="Page2B.png")

content_frame = tk.Frame(page2, bg="#e6e6e6")
content_frame.pack(side="top", fill="both", expand=True)

# show image using label
label3 = Label(page2, image=bg2)
label3.place(x=0, y=0)

# create user button
user_button = tk.Button(page2, text="USER", command=lambda: show_frame(page3), font=(20), activebackground='blue')
user_button.place(x=530, y=500)

# create admin button
admin_button = tk.Button(page2, text="ADMIN", command=lambda: show_frame(page5), font=(20), activebackground='blue')
admin_button.place(x=998, y=500)

############################################################ PAGE 3 #######################################################
page3.config(background="#e6e6e6")
bg3 = PhotoImage(file="Page3A.png")

label3 = Label(page3, image=bg3)
label3.place(x=0, y=0)

# membuat form login
form_frame = tk.Frame(page3, bg="#e6e6e6")
form_frame.pack(pady=20)
form_frame.place(x = 615 , y =280)

# Fungsi untuk cek login
def cek_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "User" and password == "12345":
        error_label.config(text="")
        page2.pack_forget()
        show_frame(page4)
    
    else:
        messagebox.showinfo("WARNING"," password anda salah")        

 # membuat label dan entry untuk username
username_label = tk.Label(form_frame, text="Username:", font=("Arial", 14), fg="black", bg="#e6e6e6", padx=10, pady=10)
username_label.grid(row=0, column=0, sticky="e")
username_entry = tk.Entry(form_frame, font=("Arial", 14), bd=0)
username_entry.grid(row=0, column=1)

# membuat label dan entry untuk password
password_label = tk.Label(form_frame, text="Password:", font=("Arial", 14), fg="black", bg="#e6e6e6", padx=10, pady=10)
password_label.grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(form_frame, font=("Arial", 14), bd=0, show="*")
password_entry.grid(row=1, column=1)

# membuat tombol login
login_button = tk.Button(page3, text="Login", font=("Arial", 16), fg="white", bg="#333333", activebackground="#333333", padx=20, pady=10, bd=0,command=cek_login)
login_button.place(x=730, y=385)


# membuat label untuk pesan error
error_label = tk.Label(page3, text="", font=("Arial", 12), fg="red", bg="#e6e6e6", padx=20, pady=10)
################################################################### Page 4 ####################################################################
page4.config(background="#ACF1F4")
bg4 = PhotoImage(file = "Page46C.png")
  
# Show image using label
label4 = Label( page4, image = bg4)
label4.place(x = 0,y = 0)

# Data Inventaris Kantor
NamaBarang = [ {"nama": "Laptop", "jenis": "Alat elektronik", "harga": 5000000, "jumlah": 2},   
               {"nama": "Printer", "jenis": "Alat elektronik", "harga": 2500000, "jumlah": 1},
               {"nama": "Meja", "jenis": "Perabotan", "harga": 2000000, "jumlah": 4},
               {"nama": "Lemari", "jenis": "Perabotan", "harga": 2200000, "jumlah": 2},
               {"nama": "AC", "jenis": "Alat elektronik", "harga": 3000000, "jumlah": 3},
               {"nama": "Kursi", "jenis": "Perabotan", "harga": 1000000, "jumlah": 5},
               {"nama": "Komputer", "jenis": "Alat elektronik", "harga": 9800000, "jumlah": 1},
               {"nama": "Kertas", "jenis": "Kebutuhan Kantor", "harga": 1200000, "jumlah": 10},
               {"nama": "Kalkulator", "jenis": "Alat elektronik", "harga": 1000000, "jumlah": 2}]

def bubble_sort_nama():
    daftar_barang = list(NamaBarang.items())

    # Melakukan Bubble Sort berdasarkan nama barang (nilai pertama pada tuple)
    n = len(daftar_barang)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if daftar_barang[j][0] > daftar_barang[j + 1][0]:
                daftar_barang[j], daftar_barang[j + 1] = daftar_barang[j + 1], daftar_barang[j]

    # Menampilkan daftar barang setelah diurutkan
    sorted_treeview1.delete(*sorted_treeview1.get_children())
    for item in daftar_barang:
        sorted_treeview1.insert("", tk.END, values=[item[0]] + item[1])

# Membuat tombol "Urutkan berdasarkan nama"
urutkan_button_nama = tk.Button(page4, text="Sorting Nama", command=bubble_sort_nama, font=(15), activebackground='blue')
urutkan_button_nama.place(x=560, y=485)


# Membuat daftar barang dari dictionary
def bubble_sort_harga():
    daftar_barang = list(NamaBarang.items())

    # Melakukan Bubble Sort berdasarkan harga (nilai kedua pada tuple)
    n = len(daftar_barang)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if daftar_barang[j][1][1] > daftar_barang[j + 1][1][1]:
                daftar_barang[j], daftar_barang[j + 1] = daftar_barang[j + 1], daftar_barang[j]

    # Menampilkan daftar barang setelah diurutkan
    sorted_treeview1.delete(*sorted_treeview1.get_children())
    for item in daftar_barang:
        sorted_treeview1.insert("", tk.END, values=[item[0]] + item[1])
        
# Membuat tombol "Urutkan berdasarkan harga"
urutkan_button_harga = tk.Button(page4, text="Sorting Harga", command=bubble_sort_harga, font=(15), activebackground='blue')
urutkan_button_harga.place(x=710, y=485)


def bubble_sort_jumlah():
    daftar_barang = list(NamaBarang.items())

    # Melakukan Bubble Sort berdasarkan jumlah (nilai ketiga pada tuple)
    n = len(daftar_barang)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if daftar_barang[j][1][2] > daftar_barang[j + 1][1][2]:
                daftar_barang[j], daftar_barang[j + 1] = daftar_barang[j + 1], daftar_barang[j]

    # Menampilkan daftar barang setelah diurutkan
    sorted_treeview1.delete(*sorted_treeview1.get_children())
    for item in daftar_barang:
        sorted_treeview1.insert("", tk.END, values=[item[0]] + item[1])
        
# Membuat tombol "Urutkan berdasarkan jumlah"
urutkan_button_jumlah = tk.Button(page4, text="Sorting Jumlah", command=bubble_sort_jumlah, font=(15), activebackground='blue')
urutkan_button_jumlah.place(x=860, y=485)

# Membuat treeview untuk daftar barang yang diurutkan
sorted_treeview1 = ttk.Treeview(page4, columns=("nama", "jenis", "harga", "jumlah"), show="headings")
sorted_treeview1.heading("nama", text="Nama Barang")
sorted_treeview1.heading("jenis", text="Jenis Barang")
sorted_treeview1.heading("harga", text="Harga Barang")
sorted_treeview1.heading("jumlah", text="Jumlah Barang")
sorted_treeview1.place(x=380, y=250)

# Menampilkan data  awal di treeview
for item in NamaBarang:
    sorted_treeview1.insert("", tk.END, values=(item["nama"], item["jenis"], item["harga"], item["jumlah"]))

m_button = tk.Button(page4, text="Back", command=lambda: show_frame(page2), font=(15), activebackground='blue')
m_button.place(x=310, y=700)

m_button = tk.Button(page4, text="Home", command=lambda: show_frame(page1), font=(15), activebackground='blue')
m_button.place(x=1190, y=700)

############################################################ PAGE 5 #######################################################
page5.config(background="#e6e6e6")
bg5 = PhotoImage(file="Page5A.png")

label5 = Label(page5, image=bg5)
label5.place(x=0, y=0)

# membuat form login
form_frame = tk.Frame(page5, bg="#e6e6e6")
form_frame.pack(pady=20)
form_frame.place(x = 615 , y =280)

# Fungsi untuk cek login
def cek_login():
    username1 = username_entry1.get()
    password1 = password_entry1.get()

    if username1 == "Admin" and password1 == "12345":
        error_label.config(text="")
        page5.pack_forget()
        show_frame(page6)
    
    else:
        messagebox.showinfo("WARNING"," password anda salah")        

 # membuat label dan entry untuk username
username_label1 = tk.Label(form_frame, text="Username:", font=("Arial", 14), fg="black", bg="#e6e6e6", padx=10, pady=10)
username_label1.grid(row=0, column=0, sticky="e")
username_entry1 = tk.Entry(form_frame, font=("Arial", 14), bd=0)
username_entry1.grid(row=0, column=1)

# membuat label dan entry untuk password
password_label1 = tk.Label(form_frame, text="Password:", font=("Arial", 14), fg="black", bg="#e6e6e6", padx=10, pady=10)
password_label1.grid(row=1, column=0, sticky="e")
password_entry1 = tk.Entry(form_frame, font=("Arial", 14), bd=0, show="*")
password_entry1.grid(row=1, column=1)

# membuat tombol login
login_button = tk.Button(page5, text="Login", font=("Arial", 16), fg="white", bg="#333333", activebackground="#333333", padx=20, pady=10, bd=0,command=cek_login)
login_button.place(x=730, y=385)


# membuat label untuk pesan error
error_label1 = tk.Label(page5, text="", font=("Arial", 12), fg="red", bg="#e6e6e6", padx=20, pady=10)

######################################################## Page 6 #####################################################################
page6.config(background="#ACF1F4")
bg6 = PhotoImage(file = "Page46B.png")

# Show image using label
label2 = Label( page6, image = bg6)
label2.place(x = 0,y = 0)

NamaBarang = {"Laptop": ["Alat Elektronik", 5000000, 2],
              "Printer": ["Alat Elektronik", 2500000, 1],
              "Meja": ["Perabotan Kantor", 2000000, 4],
              "Lemari": ["Perabotan Kantor", 2200000, 2],
              "AC": ["Alat Elektronik", 3000000, 3],
              "Kursi": ["Perabotan Kantor", 1000000, 5],
              "Komputer": ["Alat Elektronik", 9800000, 1],
              "Kertas": ["Alat Tulis Kantor", 1200000, 10],
              "Kalkulator": ["Alat Tulis Kantor", 1000000, 2]
              }

def tambah_NamaBarang():
    nama = nama_entry.get()
    jenis = jenis_entry.get()
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()

    NamaBarang[nama] = [jenis, int(harga), int(jumlah)]
    sorted_treeview.insert("", tk.END, values=[nama, jenis, harga, jumlah])

    nama_entry.delete(0, tk.END)
    jenis_entry.delete(0, tk.END)
    harga_entry.delete(0, tk.END)
    jumlah_entry.delete(0, tk.END)
    
# Membuat tombol "Tambah"
tambah_button = tk.Button(page6, text="Tambah", command=tambah_NamaBarang, font=(15), activebackground='blue')
tambah_button.place(x=635, y=610)

def hapus_NamaBarang():
    selection = sorted_treeview.selection()
    if selection:
        item = sorted_treeview.item(selection[0])
        NamaBarang_nama = item["values"][0]
        del NamaBarang[NamaBarang_nama]
        sorted_treeview.delete(selection[0])
        
# Membuat tombol "Hapus"
hapus_button = tk.Button(page6, text=" Hapus ", command=hapus_NamaBarang, font=(15), activebackground='blue')
hapus_button.place(x=733, y=610)

def edit_NamaBarang():
    selection = sorted_treeview.selection()
    if selection:
        item = sorted_treeview.item(selection[0])
        NamaBarang_nama = item["values"][0]

        # Mengambil nilai lama dari item yang dipilih
        NamaBarang_jenis = item["values"][1]
        NamaBarang_harga = item["values"][2]
        NamaBarang_jumlah = item["values"][3]

        # Membuat window baru untuk mengedit data
        edit_window = tk.Toplevel()
        edit_window.geometry("270x130")
        edit_window.title("Edit Nama Barang")

        # Menambahkan label dan entry untuk masing-masing nilai
        tk.Label(edit_window, text=" Nama Barang ").grid(row=0, column=0)
        jenis_entry = tk.Entry(edit_window)
        jenis_entry.insert(0, NamaBarang_nama)
        jenis_entry.grid(row=0, column=1)
        
        tk.Label(edit_window, text=" Jenis Barang ").grid(row=1, column=0)
        jenis_entry = tk.Entry(edit_window)
        jenis_entry.insert(0, NamaBarang_jenis)
        jenis_entry.grid(row=1, column=1)

        tk.Label(edit_window, text=" Harga Barang ").grid(row=2, column=0)
        harga_entry = tk.Entry(edit_window)
        harga_entry.insert(0, NamaBarang_harga)
        harga_entry.grid(row=2, column=1)

        tk.Label(edit_window, text=" Jumlah Barang ").grid(row=3, column=0)
        jumlah_entry = tk.Entry(edit_window)
        jumlah_entry.insert(0, NamaBarang_jumlah)
        jumlah_entry.grid(row=3, column=1)

        # Menambahkan tombol untuk menyimpan perubahan
        def simpan_perubahan():
            NamaBarang[NamaBarang_nama] = [jenis_entry.get(), int(harga_entry.get()), int(jumlah_entry.get())]
            sorted_treeview.item(selection[0], values=[NamaBarang_nama, jenis_entry.get(), harga_entry.get(), jumlah_entry.get()])
            edit_window.destroy()

        tk.Button(edit_window, text=" Simpan ", command=simpan_perubahan).grid(row=5, column=1)
        
# Membuat tombol untuk mengedit data
edit_button = tk.Button(page6, text="  Edit  ", command=edit_NamaBarang, font=(15), activebackground='blue')
edit_button.place(x=827, y=610)

# Membuat treeview daftar barang yang diurutkan
sorted_treeview = ttk.Treeview(page6, columns=("nama", "jenis", "harga", "jumlah"), show="headings")
sorted_treeview.heading("nama", text="Nama Barang")
sorted_treeview.heading("jenis", text="Jenis Barang")
sorted_treeview.heading("harga", text="Harga Barang")
sorted_treeview.heading("jumlah", text="Jumlah Barang")
sorted_treeview.place(x=380, y=250)

# Menampilkan data awal di treeview
for item in NamaBarang.items():
    sorted_treeview.insert("", tk.END, values=[item[0]] + item[1])

# Membuat frame untuk menambahkan daftar barang
tambah_frame = tk.Frame(page6)
tambah_frame.place(x=635, y=485)

nama_label = tk.Label(tambah_frame, text="Nama Barang:",font=(15))
nama_label.grid(row=0, column=0)

nama_entry = tk.Entry(tambah_frame,bg="#B9C6C8")
nama_entry.grid(row=0, column=1)

jenis_label = tk.Label(tambah_frame, text="Jenis Barang:", font=(15))
jenis_label.grid(row=1, column=0)

jenis_entry = tk.Entry(tambah_frame, bg="#B9C6C8")
jenis_entry.grid(row=1, column=1)

harga_label = tk.Label(tambah_frame, text="Harga Barang:", font=(15))
harga_label.grid(row=2, column=0)

harga_entry = tk.Entry(tambah_frame, bg="#B9C6C8")
harga_entry.grid(row=2, column=1)

jumlah_label = tk.Label(tambah_frame, text="Jumlah Barang:", font=(15))
jumlah_label.grid(row=3, column=0)

jumlah_entry = tk.Entry(tambah_frame, bg="#B9C6C8")
jumlah_entry.grid(row=3, column=1)

next_button = tk.Button(page6, text="Back", command=lambda: show_frame(page2), font=(15), activebackground='blue')
next_button.place(x=310, y=700)

next_button = tk.Button(page6, text="Home", command=lambda: show_frame(page1), font=(15), activebackground='blue')
next_button.place(x=1190, y=700)

#menjalankan aplikasi
window.mainloop()
