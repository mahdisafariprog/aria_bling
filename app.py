import tkinter as tk
import database
root = tk.Tk()
root.title("aria bling")
root.geometry("450x350")
frame = tk.Frame(root, bg="gray")
frame.pack(fill=tk.BOTH, expand=True)

label_1 = tk.Label(frame, text="name :", bg="gray",width=8,height=4, font=("Arial", 10))
label_1.place(x=10 ,y=11)

label_2 = tk.Label(frame, text="", bg="gray",width=14,height=8, font=("Arial", 16))
label_2.place(x=70,y=38)
entry_name = tk.Entry(master=label_2) 
entry_name.pack()



label_3 = tk.Label(frame, text="number :", bg="gray",width=8,height=4, font=("Arial", 10))
label_3.place(x=10,y=61)

label_4 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_4.place(x=70,y=84)
entry_phone = tk.Entry(master=label_4)
entry_phone.pack()

label_5 = tk.Label(frame, text="search :", bg="gray",width=8,height=4, font=("Arial", 10))
label_5.place(x=10,y=260)

label_6 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_6.place(x=70,y=286)
entry_serch = tk.Entry(master=label_6)
entry_serch.pack()   
def search_file():
    search_term=entry_serch.get()
    
#    f = open(r"{}/{}.txt".format(s_ch,search_term), "r",encoding="utf-8")
#    s_file=(f.read())
    label_factor = tk.Label(frame, text=s_file, bg="white", font=("Arial", 10))
    label_factor.place(x=250,y=80)
    


label_button_1= tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_button_1.place(x=209,y=280)



button_serch = tk.Button(label_button_1,bg="white", text="serch",command= search_file)
button_serch.pack()


label_7 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_7.place(x=11,y=140)
var_1 = tk.BooleanVar()
check_box_1 = tk.Checkbutton(master=label_7,text="hear cut",onvalue="1",offvalue="0", variable=var_1 , bg="gray")
check_box_1.pack()

label_gheymat =  tk.Label(frame, text="80000 T", bg="gray", font=("Arial", 10))
label_gheymat.place(x=120,y=140)

label_8 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_8.place(x=11,y=160)
var_2 = tk.BooleanVar()
check_box_2 = tk.Checkbutton(master=label_8,text="face cut",onvalue="1",offvalue="0", variable=var_2 , bg="gray")
check_box_2.pack()

label_gheymat_1 =  tk.Label(frame, text="40000 T", bg="gray", font=("Arial", 10))
label_gheymat_1.place(x=120,y=160)

label_9 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_9.place(x=11,y=180)
var_3 = tk.BooleanVar()
check_box_3 = tk.Checkbutton(master=label_9,text="face masage",onvalue="1",offvalue="0", variable=var_3 , bg="gray")
check_box_3.pack()

label_gheymat_2 =  tk.Label(frame, text="60000 T", bg="gray", font=("Arial", 10))
label_gheymat_2.place(x=120,y=180)
label_10 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_10.place(x=11,y=200)
var_4 = tk.BooleanVar()
check_box_4 = tk.Checkbutton(master=label_10,text="vip service",onvalue="1",offvalue="0",  variable=var_4 , bg="gray")
check_box_4.pack()

label_gheymat_3 =  tk.Label(frame, text="300000 T", bg="gray", font=("Arial", 10))
label_gheymat_3.place(x=120,y=200)

label_button_2 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_button_2.place(x=15,y=230)
        
        

sher_1 = (" خوش تر از دوران عشق ایام نیست ")
sher_2 = ("  بامداد عاشقان را شام نیست ")



def m_factor():
    hear_cut = 0
    face_cut = 0
    face_masage = 0
    vip_service = 0
    if var_1.get() == 1 :
        hear_cut = 80000
    else : 
        hear_cut = 0
    if var_2.get() == 1 : 
        face_cut = 40000
    else : 
        face_cut = 0
    if var_3.get() == 1 :
        face_masage = 60000
    else :
        face_masage = 0
    if var_4.get() == 1 :
        vip_service = 300000
        hear_cut = 0
        face_cut = 0
        face_masage = 0
        
    else :
        vip_service == 0
    gh_factor =((hear_cut)+(face_cut)+(face_masage)+(vip_service))

    name = entry_name.get()
    phone = entry_phone.get()

    
    factor = (f"Hello\nname : {name}\nphone : {phone}\nfactor : {gh_factor}\n{sher_1}\n{sher_2}")
#    write_recide(factor,phone)
    label_factor = tk.Label(frame, text=factor, bg="white", font=("Arial", 10))
    label_factor.place(x=250,y=80)
    return label_factor


button_Computing = tk.Button(label_button_2,bg="white", text="Computing",command= m_factor)
button_Computing.pack()


root.mainloop()

#def write_recide(factor,phone):
#    with open(f'{phone}.txt', 'w', encoding="utf-8") as f:
#        f.write(factor)
