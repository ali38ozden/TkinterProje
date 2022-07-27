import json

def basla():
    isimListe=[]

    with open("person_name.json","r")as read:       
        try:
            beta=json.load(read)
            for i in beta:
                
                isimListe.append(i)                 
        except:
            print("galiba içi bos")
            pass


    print(isimListe.__len__())
    def bir():
        i=-1
        for k in range(isimListe.__len__()):
            i+=1
            print(i)
            print(isimListe[i]["takipediyormu"])
            if isimListe[i]["takipediyormu"]==False:
                print("bu isim çıkarlıdı: "+isimListe[i]["name"])
                isimListe.pop(i)
                i-=1
                         
    bir()          

    with open("person_name.json","w")as write: 
            json.dump(isimListe,write,indent=2)