
import tkinter as tk
import database as dt


class aria_bling():
    def __init__(self, root):
        self.root = root
        self.root.title("AromaLab")
        root.title("aria bling")
        root.geometry("450x350")
        self.main_page()
    def main_page(self):
        frame = tk.Frame(root, bg="gray")
        frame.pack(fill=tk.BOTH, expand=True)
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
        


        
if __name__ == "__main__":
    root = tk.Tk()
    app = aria_bling(root)
    root.mainloop()