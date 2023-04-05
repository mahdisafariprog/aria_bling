import tkinter as tk

def generate_number():
    while True:
        number = random.randint(0, 999)
        digits = [int(d) for d in str(number)]
        if len(set(digits)) == len(digits):
            return number
code = generate_number()

root = tk.Tk()
root.title("aria bling")
root.geometry("550x350")
frame = tk.Frame(root, bg="gray")
frame.pack(fill=tk.BOTH, expand=True)
label_1 = tk.Label(frame, text="name :", bg="gray",width=8,height=4, font=("Arial", 10))
label_1.place(x=11 ,y=81)

label_2 = tk.Label(frame, text="", bg="gray",width=14,height=8, font=("Arial", 16))
label_2.place(x=80,y=108)
entry_name = tk.Entry(master=label_2)
name = str(entry_name.get())
entry_name.pack()

label_3 = tk.Label(frame, text="number :", bg="gray",width=8,height=4, font=("Arial", 10))
label_3.place(x=300,y=81)

label_4 = tk.Label(frame, text="", bg="gray",width=14,height=4, font=("Arial", 16))
label_4.place(x=400,y=108)
entry_phone = tk.Entry(master=label_4)
phone = entry_phone.get()
entry_phone.pack()

label_5 = tk.Label(frame, text="serch :", bg="gray",width=8,height=4, font=("Arial", 10))
label_5.place(x=11,y=11)

label_6 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_6.place(x=80,y=38)
entry_serch = tk.Entry(master=label_6)
entry_serch.pack()   

label_button_1= tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_button_1.place(x=220,y=37)



button_serch = tk.Button(label_button_1,bg="white", text="serch")
button_serch.pack()


label_7 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_7.place(x=11,y=200)
var = tk.BooleanVar()
check_box_1 = tk.Checkbutton(master=label_7,text="hear cut", variable=var , bg="gray")
check_box_1.pack()

label_gheymat =  tk.Label(frame, text="80000 T", bg="gray", font=("Arial", 10))
label_gheymat.place(x=120,y=200)

label_8 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_8.place(x=11,y=220)
var = tk.BooleanVar()
check_box_2 = tk.Checkbutton(master=label_8,text="face cut", variable=var , bg="gray")
check_box_2.pack()

label_gheymat_1 =  tk.Label(frame, text="40000 T", bg="gray", font=("Arial", 10))
label_gheymat_1.place(x=120,y=220)

label_9 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_9.place(x=11,y=240)
var = tk.BooleanVar()
check_box_3 = tk.Checkbutton(master=label_9,text="face masage", variable=var , bg="gray")
check_box_3.pack()

label_gheymat_2 =  tk.Label(frame, text="60000 T", bg="gray", font=("Arial", 10))
label_gheymat_2.place(x=120,y=240)
label_10 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_10.place(x=11,y=260)
var = tk.BooleanVar()
check_box_4 = tk.Checkbutton(master=label_10,text="vip service", variable=var , bg="gray")
check_box_4.pack()

label_gheymat_3 =  tk.Label(frame, text="300000 T", bg="gray", font=("Arial", 10))
label_gheymat_3.place(x=120,y=260)

label_button_2 = tk.Label(frame, text="", bg="gray",width=8,height=4, font=("Arial", 10))
label_button_2.place(x=15,y=290)
        
        

sher_1 = (" خوش تر از دوران عشق ایام نیست ")
sher_2 = ("  بامداد عاشقان را شام نیست ")
def factor_1():
    factor = (f"Hello\nname : {name}\nphone : {phone}\nfactor : \n{sher_1}\n{sher_2}")
    label_factor = tk.Label(frame, text=factor, bg="white", font=("Arial", 10))
    label_factor.place(x=250,y=200)
    return label_factor
    

button_Computing = tk.Button(label_button_2,bg="white", text="Computing",command= factor_1)
button_Computing.pack()

root.mainloop()