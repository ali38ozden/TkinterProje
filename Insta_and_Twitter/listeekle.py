
import json

isimListe=[]
print("calıstı")

with open("person_name.json","r")as read:   
     
    try:
        beta=json.load(read)
        for i in beta:
           isimListe.append(i)
    except:
        print("person_name.json bunun içi bos from listeekle")
        okundumu=True
def oku(okuatil):
    varmi(okuatil)  

def yaz():
    with open("person_name.json","w")as write: 
        json.dump(isimListe,write,indent=2)
    
def varmi(varmiatil):
    varmi=False
    for i in isimListe:
        if(i==varmiatil):
            varmi=True
            print("bu isim var")

    if(varmi!=True):
        print("yeni isim eklendi: ")
        isimListe.append(varmiatil) 
    yaz()  


def yeniEklemekistenirse():

    print("\n\n**********************************") 
    print("Manuel isim eklemek için 0 dan başka bir şey girin")
    print("\n\n-----------İsim girilmeyecekse 0 yazin----------\n")

    isimGirilcekmi=input("kac isim girilcek(sayi ile): ")

    if(isimGirilcekmi!="0"):
        isimGirilcekmi1=int(isimGirilcekmi)
        for c in range(isimGirilcekmi1):
            ad=input("ad gir: ")
            atil={"name":ad,
            "takipediyormu":True}#yeni paremetre ekledim bi bakılacak
            oku(atil)
        gene=input("\n Daha ekliyecekmisin y/n : ")
        if(gene=="y"):
            yeniEklemekistenirse()
        else:
            pass
    else:
        pass

def kontrol(gelenisim):
    isimvarmi=False
    for i in range(isimListe.__len__()):
        if(isimListe[i]["name"]==gelenisim):
            isimvarmi=True
            print("bu isim var")
            return 1

    if(isimvarmi!=True):
        return 0
    
    
