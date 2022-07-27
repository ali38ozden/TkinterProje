import insta
import jsonSil
import hikayebegenme
import isimListe
import takipEtmeyeniCikar
import Twitter
from threading import Thread
from time import sleep
from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import notifypy
from idlelib.tooltip import Hovertip

# tkinter Balloon kullanılcak4
# otomatik de manulel atınan değerlerin adamın bilmes lazım
# bildirmlere image koycaz twiter instagram
# seni her geri takip edene teşekkürler mesajı


# ==========> Fonksiyonlar <==========
def bildirim(baslik, neyazicak, aplikasyoname,foto):
    yeni.title=baslik
    yeni.icon=foto
    yeni.message=neyazicak
    yeni.application_name=aplikasyoname
    yeni.send()

def İmportTakipEt():
    print("toplaIslem: {},takipKisi: {},begenTopalm: {},Ilk_Defa_Giris: {},kullanciAdi: {},kullaniciSifre1: {}".format(a0_3.get(), a0_4.get(), a0_5.get(), Ilk_Defa_Giris,a0_7.get(), a0_8.get()))
    insta.BaslaIslem(a0_3.get(), a0_4.get(), a0_5.get(), Ilk_Defa_Giris,a0_7.get(), a0_8.get())
    bildirim("Instagram","Takip Et işlemleri bitti.","Instagram","Instagram.png")
    
def İmportTakiptenCik():
    takipEtmeyeniCikar.basla()
    bildirim("Instagram","Takipetmeyenleri Çık işlemleri bitti.","Instagram","Instagram.png")
    DakikaSay()

def İmportHikayeBegen():
    hikayebegenme.basla()
    bildirim("Instagram","Hikaye Begen işlemleri bitti.","Instagram","Instagram.png")

def İmportTwitterr():
    print(a3_3.get())
    if a3_3.get()!="":
        sayi=int(a3_3.get())
        print("demek bos default")
        Twitter.basla(sayi)
    
    bildirim("Twitter","Twitter işlemleri bitti.","Instagram","Twitter.png")

def TakipEtBilgi(gelen):
    global Ilk_Defa_Giris
    Ilk_Defa_Giris=gelen
    print("başladı")
    t1=Thread(target=İmportTakipEt)
    t1.start()
# ==========> Dakika Say <==========
def DakikaSay():
    global a1_1, a1_1Disable
    a1_1.config(state="disabled", fg_color="gray")
    a1_1Disable=True
    for say in range(dk):
        dakika=(dk-say)/60
        saniye=(dk-say)%60
        sleep(1)
        try:
            a1_2.config(text=("Beklemeniz Gereken Süre:\n{0} : {1}".format(int(dakika), saniye)))
        except:
            pass
    bildirim("Takipten Çıkar", "10 Dakika doldu", "Instagram","Instagram.png")
    a1_1Disable=False
    try:
        a1_2.config(text="Tekrardan Başlatabilirsiniz")
    except:
        pass
    try:
        a1_1.config(state="normal", fg_color="black")
    except:
        pass
# ==========> Sistem <==========     
window=customtkinter.CTk()
root = window
root.title("Insta Twitter")
root.iconbitmap("Instagram.png")
root.geometry("800x400")
root.resizable(False,False) # => ekran boyutu sabitleme



# val
takip_frame, takipCik_fram, hikayeBegen_frame, twitter_frame=Label(),Label(),Label(),Label()
baslikFont=("yu gothic ui", 19, "bold")
a1_1Disable=False # TakipCikar Başla  Button
dk=600 # kaç dakika saymasını istiyorsan x60
cizg=Frame(root,bg="#2a2d2e",width=7,height=70)
cizgi_sekil_ust=Frame(root,bg="#212325",width=7,height=15)
cizgi_sekil_alt=Frame(root,bg="#212325",width=7,height=20)
yeni=notifypy.Notify()
Ilk_Defa_Giris=False

# ==========> Frame Label <==========
lab_frame=customtkinter.CTkFrame(root)
lab_frame.place(relx=0.21, rely=0.01, relwidth=0.78, relheight=0.97)
# ==========> Navigatin Bar <==========
navigation_fram=customtkinter.CTkFrame(root,fg_color="black")
navigation_fram.place(relx=0.001, rely=0.001, relwidth=0.2, relheight=1)
# ===== Navigation btn frame =====
navigation_mid=customtkinter.CTkFrame(navigation_fram,fg_color="black")
navigation_mid.place(relx=0.1, rely=0.15, relwidth=0.98, relheight=0.7)

# ===== Navigation Btn Fun =====
def destroy(*argv):
    for arg in argv:    
        arg.destroy()

def cizgi(x,y):
    cizg.place(x=x, y=y)
    cizgi_sekil_ust.place(x=x, y=y)
    cizgi_sekil_alt.place(x=x, y=y+55)

def other(arg1,*args):
    arg1.config(fg_color="#2a2d2e", hover_color="black", state="disabled")
    for arg in args:
        arg.config(fg_color="gray", hover_color="black")
        arg.config(state="normal")
    if str(arg1)==".!ctkframe2.!ctkframe.!ctkbutton":
        cizgi(161,53)
    elif str(arg1)==".!ctkframe2.!ctkframe.!ctkbutton2":
        cizgi(161,109)
    elif str(arg1)==".!ctkframe2.!ctkframe.!ctkbutton3":
        cizgi(161,165)
    elif str(arg1)==".!ctkframe2.!ctkframe.!ctkbutton4":
        cizgi(161,220)

# ==========> Navigation Fun <==========
def TakipFrame():
    global takip_frame, takipCik_fram, hikayeBegen_frame, twitter_frame
    global a0_3, a0_4, a0_5, a0_7, a0_8
    destroy(takipCik_fram)
    other(n_takip_btn,n_takip_cikar_btn,n_hikaye_beger_btn,n_twiter_btn)
    takip_frame=customtkinter.CTkFrame(root)
    takip_frame.place(relx=0.21, rely=0.01, relwidth=0.78, relheight=0.97)
    # ===== Değerler =====
    a0_1=Label(takip_frame, text ="Değerler", bg="#2a2d2e",font=baslikFont, fg="white")
    a0_1.place(relx=0.3, rely=.3, anchor=CENTER)
    a0_3=customtkinter.CTkEntry(takip_frame,placeholder_text="Kaç işlem")
    a0_3.place(relx=0.3, rely=.4, anchor=CENTER)
    a0_4=customtkinter.CTkEntry(takip_frame,placeholder_text="Sayfada Takip")
    a0_4.place(relx=0.3, rely=.5, anchor=CENTER)
    a0_5=customtkinter.CTkEntry(takip_frame,placeholder_text="Beğen Yorum")
    a0_5.place(relx=0.3, rely=.6, anchor=CENTER)
    # ===== Otomatik ======
    a0_0=Label(takip_frame, text ="Otomatik", bg="#2a2d2e", font=baslikFont, fg="white")
    a0_0.place(relx=0.7, rely=.2, anchor=CENTER)
    a0_2=customtkinter.CTkButton(takip_frame, text="Başla", command=lambda:TakipEtBilgi(False), fg_color="black", hover_color="gray")
    a0_2.place(relx=0.7, rely=.3, anchor=CENTER)
    # ===== El ile ======
    a0_1=Label(takip_frame, text ="El İle", bg="#2a2d2e", font=baslikFont, fg="white")
    a0_1.place(relx=0.7, rely=.5, anchor=CENTER)
    a0_7=customtkinter.CTkEntry(takip_frame, placeholder_text="Kullanici Adi")
    a0_7.place(relx=.7, rely=.6, anchor=CENTER)
    a0_8=customtkinter.CTkEntry(takip_frame, placeholder_text="Şifre")
    a0_8.place(relx=.7, rely=.7, anchor=CENTER)
    a0_6=customtkinter.CTkButton(takip_frame, text="Başla", command=lambda:TakipEtBilgi(True), fg_color="black", hover_color="gray")
    a0_6.place(relx=0.7, rely=.8, anchor=CENTER)
    
def TakipCikFrame():
    global takip_frame,takipCik_fram,hikayeBegen_frame,twitter_frame, a1_1, a1_2
    destroy(takip_frame)
    other(n_takip_cikar_btn, n_takip_btn, n_hikaye_beger_btn, n_twiter_btn)
    takipCik_fram=customtkinter.CTkFrame(root)
    takipCik_fram.place(relx=0.21, rely=0.01, relwidth=0.78, relheight=0.97)
    a1_0=Label(takipCik_fram, text ="Takipten Çikar", bg="#2a2d2e", fg="white",font=baslikFont)
    a1_0.place(relx=.72, rely=.4, anchor=CENTER)
    a1_1=customtkinter.CTkButton(takipCik_fram, text="Başla", command=lambda:Thread(target=İmportTakiptenCik).start(), fg_color="black", hover_color="gray")
    a1_1.place(relx=.72, rely=.52, anchor=CENTER)

    if(a1_1Disable==False):
        a1_1.config(state="normal",fg_color="black")
    else:
        a1_1.config(state="disabled",fg_color="gray") 
    a1_3=Label(takipCik_fram, text ="Eski Bilgileri Sil", bg="#2a2d2e", fg="white",font=baslikFont)
    a1_3.place(relx=.3, rely=.6, anchor=CENTER)
    a1_4=customtkinter.CTkButton(takipCik_fram, text="Sil", command=lambda:Thread(target=jsonSil.basla).start(), fg_color="black", hover_color="gray")
    a1_4.place(relx=.3, rely=.72, anchor=CENTER)
    Hovertip(a1_4,'Bu buton \nEl ile eklenenleri silmez.',hover_delay=00)
    a1_2=Label(takipCik_fram, bg="#2a2d2e", text="10 Dk beklemenizi rica ediyoruz. \nAlgoritma anlamasin!!", fg="white", font=15)
    a1_2.place(relx=.5, rely=.1, anchor=CENTER)
    # === İsimleri yazdircak yer
    a1_5=Label(takipCik_fram, text="Listeyi Aç", font=baslikFont, bg="#2a2d2e", fg="white")
    a1_5.place(relx=.3, rely=.4, anchor=CENTER)
    a1_6=customtkinter.CTkButton(takipCik_fram, text="Aç", command=isimListe.basla, fg_color="black", hover_color="gray")
    a1_6.place(relx=.3, rely=.5, anchor=CENTER)

def HikayeBegenFrame():
    global takip_frame,takipCik_fram,hikayeBegen_frame,twitter_frame
    destroy(takip_frame,takipCik_fram)
    other(n_hikaye_beger_btn, n_takip_btn, n_takip_cikar_btn, n_twiter_btn)
    hikayeBegen_frame=customtkinter.CTkFrame(root)
    hikayeBegen_frame.place(relx=0.21, rely=0.01, relwidth=0.78, relheight=0.97)
    # ===== Hikaye Beğen =====
    a2_3=Label(hikayeBegen_frame, bg="#2a2d2e", fg="white",text="Hikaye Beğen", font=baslikFont)
    a2_3.place(relx=.3, rely=.45, anchor=CENTER)
    a2_0=customtkinter.CTkButton(hikayeBegen_frame, text="Başla", fg_color="black", hover_color="gray", command=lambda:Thread(target=İmportHikayeBegen).start())
    a2_0.place(relx=.3, rely=.55, anchor=CENTER)
    # ===== Hikaye İzle =====
    a2_4=Label(hikayeBegen_frame, bg="#2a2d2e", fg="white", text="Hikaye İzle", font=baslikFont)
    a2_4.place(relx=.7, rely=.45, anchor=CENTER)
    a2_1=customtkinter.CTkButton(hikayeBegen_frame,text="Başla", fg_color="black", hover_color="gray")
    a2_1.place(relx=.7, rely=.55, anchor=CENTER)

def TwitterrFrame():
    global takip_frame,takipCik_fram,hikayeBegen_frame,twitter_frame,   a3_3
    destroy(takip_frame,takipCik_fram)
    other(n_twiter_btn, n_takip_btn, n_takip_cikar_btn, n_hikaye_beger_btn)
    twitter_frame=customtkinter.CTkFrame(root)
    twitter_frame.place(relx=0.21, rely=0.01, relwidth=0.78, relheight=0.97)
    # ===== Değerler =====
    x=.05
    a3_1=Label(twitter_frame, text ="Değerler", bg="#2a2d2e",font=baslikFont, fg="white")
    a3_1.place(relx=0.3, rely=.4+x, anchor=CENTER)
    a3_3=customtkinter.CTkEntry(twitter_frame,placeholder_text="Kaç Kişi Takip Etsin")
    a3_3.place(relx=0.3, rely=.5+x, anchor=CENTER)
    # ===== Otomatik ======
    a3_0=Label(twitter_frame, text ="Otomatik", bg="#2a2d2e", font=baslikFont, fg="white")
    a3_0.place(relx=.5, rely=.15, anchor=CENTER)
    a3_2=customtkinter.CTkButton(twitter_frame, text="Başla", command=lambda:Thread(target=İmportTwitterr).start(), fg_color="black", hover_color="gray")
    a3_2.place(relx=.5, rely=.25, anchor=CENTER)
    # ===== El ile ======
    a3_1=Label(twitter_frame, text ="El İle", bg="#2a2d2e", font=baslikFont, fg="white")
    a3_1.place(relx=.7, rely=.4+x, anchor=CENTER)
    a3_7=customtkinter.CTkEntry(twitter_frame,placeholder_text="Kullanici Adi")
    a3_7.place(relx=.7, rely=.5+x, anchor=CENTER)
    a3_8=customtkinter.CTkEntry(twitter_frame,placeholder_text="Şifre")
    a3_8.place(relx=.7, rely=.6+x, anchor=CENTER)
    a3_6=customtkinter.CTkButton(twitter_frame, text="Başla", command=lambda:print("el ile button"), fg_color="black", hover_color="gray")
    a3_6.place(relx=.5, rely=.72+x, anchor=CENTER)

def Kapat():
    try:
        insta.driver.close()
    except:
        pass
    try:
        takipEtmeyeniCikar.driver.close()
    except:
        pass
    try:
        hikayebegenme.driver.close()
    except:
        pass
    try:
        Twitter.driver.close()
    except:
        pass

# ===== Navigation Btnlar =====
n_takip_btn=customtkinter.CTkButton(navigation_mid, text="Takip ET", command=TakipFrame)
n_takip_btn.pack(fill="y", expand=True)             
n_takip_cikar_btn=customtkinter.CTkButton(navigation_mid, text="Çıkar", command=TakipCikFrame)      
n_takip_cikar_btn.pack(fill="y", expand=True)           
n_hikaye_beger_btn=customtkinter.CTkButton(navigation_mid, text="Hikaye", command=HikayeBegenFrame) 
n_hikaye_beger_btn.pack(fill="y", expand=True)             
n_twiter_btn=customtkinter.CTkButton(navigation_mid, text="Twitier", command=TwitterrFrame)                 
n_twiter_btn.pack(fill="y", expand=True)
n_kapat_btn=customtkinter.CTkButton(navigation_mid, text="Kapat", command=Kapat, fg_color="red", hover_color="#ff8080")                 
n_kapat_btn.pack(fill="y", expand=True)
# Butona basiyoruz
n_takip_btn.clicked()



root.mainloop()
