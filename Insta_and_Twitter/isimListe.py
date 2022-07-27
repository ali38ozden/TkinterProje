from tkinter import *
from turtle import left, width
import customtkinter
import json

def listedenkaldır():
    no=pavanlist1.curselection()
    print(type(no[0]))
    print(isimListe[no[0]])
    isimListe.pop(no[0])
    pavanlist1.delete(ANCHOR)
    with open("person_name.json","w")as write: 
        	json.dump(isimListe,write,indent=2)

def ekle():
    if ekleentry.get()!="":
        atil={"name":ekleentry.get(),
        "takipediyormu":True}
        if varmi(atil)!=0:
            pavanlist1.insert(END, ekleentry.get())
    

def basla():
    global isimListe,pavanlist1,ekleentry,varmi
    isimListe=[]
    with open("person_name.json","r")as read:   
        try:
            beta=json.load(read)
            for i in beta:
               isimListe.append(i)
        except:
            print("person_name.json bunun içi bos from listeekle")
            okundumu=True

    def yaz():
        with open("person_name.json","w")as write: 
            json.dump(isimListe,write,indent=2)

    def varmi(varmiatil):
        varmi=False
        for i in isimListe:
            if(i["name"]==varmiatil["name"]):
                varmi=True
                print("bu isim var")
                return 0
        if(varmi!=True):
            print("yeni isim eklendi: ")
            isimListe.append(varmiatil) 
        yaz()  

    master1 = customtkinter.CTk()
    master1.geometry("600x400")
    master1.resizable(False,False)
    master1.title("İsim Listesi")
    master1.iconbitmap("Instagram.png")
    liste_frame=Frame(master1)
    liste_frame.place(relx=.0, rely=0 ,relheight=1 , relwidth=.35)
    scrollbar1=customtkinter.CTkScrollbar(liste_frame)
    scrollbar1.pack( side = RIGHT, fill = Y )
    pavanlist1 = Listbox(liste_frame, yscrollcommand = scrollbar1.set,  width=300, bg="#212325", fg="white", font=12, height=13)
    pavanlist1.place(relx=.04, rely=.04)

    for pavanline1 in range(isimListe.__len__()):
     pavanlist1.insert(END, isimListe[pavanline1]["name"])
    
    butonlar_frame=Frame(master1, bg="#212325")
    butonlar_frame.place(relx=.36,rely=.0, relheight=1, relwidth=.62)
    ekleentry=customtkinter.CTkEntry(butonlar_frame, placeholder_text="Kullanici adi")
    ekleentry.place(relx=.5, rely=.3, anchor=CENTER)
    eklebtn=customtkinter.CTkButton(butonlar_frame, text="Ekle", command=ekle, fg_color="black", hover_color="gray").place(relx=.5, rely=.4, anchor=CENTER)
    cikar_label=Label(butonlar_frame, text="İsime tıkla Buttona bas", bg="#212325", fg="gray",font=15).place(relx=.5, rely=.6, anchor=CENTER)
    btn1=customtkinter.CTkButton(butonlar_frame, text="Çikar", command=listedenkaldır, fg_color="black", hover_color="gray").place(relx=.5, rely=.7, anchor=CENTER)
    pavanlist1.pack( side = LEFT, fill = BOTH )
    scrollbar1.config( command = pavanlist1.yview)

    master1.mainloop()  
