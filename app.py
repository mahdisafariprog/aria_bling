import tkinter as tk
import database as dt


class aria_bling():
    def __init__(self):

        global root,frame
        root = tk.Tk()
        root.title("aria bling")
        root.geometry("450x350")
        frame = tk.Frame(root, bg="gray")
        frame.pack(fill=tk.BOTH, expand=True)
        self.labels()
        self.search_file()
        self.m_factor()
        self.button()
        self.entry()
        self.check_box()
    def labels(self):
        global label_1,label_2,label_3,label_4,label_5,label_6,label_7,label_8,label_9,label_10,label_button_1,label_button_2,label_gheymat,label_gheymat_1,label_gheymat_2,label_gheymat_3,label_factor
        label_1 = tk.Label(frame, text="name :", bg="gray",width=8,height=4, font=("Arial", 10))
        label_1.place(x=10 ,y=11)

        label_2 = tk.Label(frame, text="", bg="gray",width=14,height=8, font=("Arial", 16))
        label_2.place(x=70,y=38)

        label_3 = tk.Label(frame, text="number :", bg="gray",width=8,height=4, font=("Arial", 10))
        label_3.place(x=10,y=61)

        label_4 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_4.place(x=70,y=84)

        label_5 = tk.Label(frame, text="search :", bg="gray",width=8,height=4, font=("Arial", 10))
        label_5.place(x=10,y=260)

        label_6 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_6.place(x=70,y=286)

        label_7 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_7.place(x=11,y=140)

        label_8 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_8.place(x=11,y=160)

        label_9 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_9.place(x=11,y=180)

        label_10 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_10.place(x=11,y=200)

        label_button_1= tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_button_1.place(x=209,y=280)

        label_button_2 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
        label_button_2.place(x=15,y=230)

        label_gheymat =  tk.Label(frame, text="80000 T", bg="gray", font=("Arial", 10))
        label_gheymat.place(x=120,y=140)

        label_gheymat_1 =  tk.Label(frame, text="40000 T", bg="gray", font=("Arial", 10))
        label_gheymat_1.place(x=120,y=160)

        label_gheymat_2 =  tk.Label(frame, text="60000 T", bg="gray", font=("Arial", 10))
        label_gheymat_2.place(x=120,y=180)

        label_gheymat_3 =  tk.Label(frame, text="300000 T", bg="gray", font=("Arial", 10))
        label_gheymat_3.place(x=120,y=200)

        label_factor = tk.Label(frame, text= "a", bg="white", font=("Arial", 10))
        label_factor.place(x=250,y=80)
    def search_file(self):
        global search_term
        search_term=entry_serch.get()
        #    f = open(r"{}/{}.txt".format(s_ch,search_term), "r",encoding="utf-8")
        #    s_file=(f.read())
        
    def m_factor(self):
    
        hear_cut = 0
        face_cut = 0
        face_masage = 0
        vip_service = 0
        sher_1 = (" خوش تر از دوران عشق ایام نیست ")
        sher_2 = ("  بامداد عاشقان را شام نیست ")

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
    def button(self):

        button_Computing = tk.Button(label_button_2,bg="white", text="Computing",command= self.m_factor)
        button_Computing.pack()

        button_serch = tk.Button(label_button_1,bg="white", text="serch",command= self.search_file)
        button_serch.pack()

    def entry(self):

        global entry_name,entry_phone,entry_serch

        entry_name = tk.Entry(master=label_2) 
        entry_name.pack()
        
        entry_phone = tk.Entry(master=label_4)
        entry_phone.pack()
        
        entry_serch = tk.Entry(master=label_6)
        entry_serch.pack()
        
    def check_box(self):

        global var_1,var_2,var_3,var_4,check_box_1,check_box_2,check_box_3,check_box_4
        var_1 = tk.BooleanVar()
        check_box_1 = tk.Checkbutton(master=label_7,text="hear cut",onvalue="1",offvalue="0", variable=var_1 , bg="gray")
        check_box_1.pack()

        var_2 = tk.BooleanVar()
        check_box_2 = tk.Checkbutton(master=label_8,text="face cut",onvalue="1",offvalue="0", variable=var_2 , bg="gray")
        check_box_2.pack()

        var_3 = tk.BooleanVar()
        check_box_3 = tk.Checkbutton(master=label_9,text="face masage",onvalue="1",offvalue="0", variable=var_3 , bg="gray")
        check_box_3.pack()

        var_4 = tk.BooleanVar()
        check_box_4 = tk.Checkbutton(master=label_10,text="vip service",onvalue="1",offvalue="0",  variable=var_4 , bg="gray")
        check_box_4.pack()

        root.mainloop()

mahdi = aria_bling()
#def write_recide(factor,phone):
#    with open(f'{phone}.txt', 'w', encoding="utf-8") as f:
#        f.write(factor)
