from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("MyBook")

main = LabelFrame(root, text ="Masukan data", padx=10, pady=10, borderwidth=5 )
main.grid(row=0, column=0, padx=10, pady=10)

sub = LabelFrame(root, relief = "flat")
sub.grid(row=0, column=1, padx=10, pady=10, sticky = "ns")

#input
Ljudul = Label(main, text= "Judul", anchor = "w", width = 10).grid(row = 0 , column =0)
Ltag1 = Label(main, text= ":", width=2).grid(row=0, column = 1)
Ejudul = Entry(main, bd = 5, width= 40).grid(row=0, column=2)
Lnama = Label(main, text= "Author", anchor = "w", width = 10).grid(row = 1 , column =0)
Ltag2 = Label(main, text= ":", width=2).grid(row=1, column = 1)
Enama = Entry(main, bd = 5, width= 40).grid(row=1, column=2)
Lrilis = Label(main, text= "Tanggal Rilis", anchor = "w", width = 10).grid(row = 2 , column =0)
Ltag3 = Label(main, text= ":", width=2).grid(row=2, column = 1)
Erilis = Entry(main, bd = 5, width= 40).grid(row=2, column=2)

#drop down
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Komik','Novel','Jurnal'}
tkvar.set('Novel') # set the default option

popupMenu = OptionMenu(main, tkvar, *choices)
Ljenis = Label(main, text="Pilih Jenis", anchor = "w", width = 10).grid(row = 3, column = 0)
Ltag4 = Label(main, text= ":", width=2).grid(row=3, column = 1)
popupMenu.grid(row = 3, column =2)

def keluar():
    top = Toplevel()
    top.title("Exit ")
    d_frame = LabelFrame(top, text="Konfirmasi", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    # opts = LabelFrame(top, padx=10, pady=10)
    # opts.pack(padx=10, pady=10)
    btn_ya = Button(d_frame, text="Ya",command=root.destroy).grid(row=0, column = 0)
    btn_no = Button(d_frame, text="Tidak",command=top.destroy).grid(row=0, column = 1)
#about
def aboutMe():
    top = Toplevel()
    top.title("About ")
    d_frame = LabelFrame(top, text="Data Diri", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="1907852 - Bayu Kurniawan", anchor="w").grid(row=0, column=0, sticky="w")
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

#check box
Lgenre = Label(main, text="Genre", anchor = "w", width = 10).grid(row = 4, column = 0)
Ltag5 = Label(main, text= ":", width=2).grid(row=4, column = 1)
box = LabelFrame(main, relief = "flat")
box.grid(row=4, column =2)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

C1 = Checkbutton(box, text="Action", variable= var1, onvalue= 1, offvalue=0).grid(row=4, column= 0)
C1 = Checkbutton(box, text="Romance", variable= var1, onvalue= 2, offvalue=0).grid(row=4, column= 1)
C1 = Checkbutton(box, text="Comedy", variable= var1, onvalue= 3, offvalue=0).grid(row=4, column= 2)
C1 = Checkbutton(box, text="Historical", variable= var1, onvalue= 4, offvalue=0).grid(row=5, column= 0)
C1 = Checkbutton(box, text="Horor", variable= var1, onvalue= 5, offvalue=0).grid(row=5, column= 1)
C1 = Checkbutton(box, text="Thriller", variable= var1, onvalue= 6, offvalue=0).grid(row=5, column= 2)

#radio
Lgenre = Label(main, text="Membership", anchor = "w", width = 10).grid(row = 6, column = 0)
Ltag5 = Label(main, text= ":", width=2).grid(row=6, column = 1)
radio = LabelFrame(main, relief = "flat")
radio.grid(row=6, column =2)

vvar1 = IntVar()
vvar2 = IntVar()
R1 = Radiobutton(radio, text="Exclusive", variable=vvar1, value=1).grid(row=6, column= 0)
R2 = Radiobutton(radio, text="Reguler", variable=vvar2, value=2).grid(row=6, column= 1)

#foto
btn_foto = Button(main, text="Open File", state="disable", width= 20).grid(row=8, column=2)
#submit button
btn_foto = Button(main, text="Submit", width= 20).grid(row=9, column=2)



Ltitle = Label(sub, text = "MyBook",font= ("comic sans ms", 28),fg = "#FFA500").grid(row=0, sticky ="w")
Lsubtitle = Label(sub, text = "Sebuah aplikasi koleksi buku", font=("comic sans ms", 16)).grid(row=1)

btn_show = Button(sub, text="See All Submissions", width= 20).grid(row=2, column=0)
btn_clear = Button(sub, text="Clear All Submissions", width= 20).grid(row=3, column=0)
btn_about = Button(sub, text="About", width= 20, command=aboutMe).grid(row=4, column=0)
btn_exit = Button(sub, text="Exit", width= 20, command=keluar).grid(row=6, column=0)
root.mainloop()