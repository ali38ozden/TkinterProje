import listeekle
import json
from time import sleep
from selenium import webdriver

bakilsinmi=True
kacKisiCikti=0

def basla():

    global driver
    def kontrol(gelenIsim,no):
        
        flag=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li["+no+"]/div")                                    
        driver.execute_script("arguments[0].scrollIntoView();",flag)
             
        global kacKisiCikti
        try:
            if(kacKisiCikti==10):
                print("14 kisi çıktı sistem anlamsın diye 10 dk beklemek gerekiyor")
                sleep(600)
                kacKisiCikti=0
        except:
            print("hata burda 211")
        

        if listeekle.kontrol(gelenIsim)==1:
            takipEdiyor=True
            print("takip ediyor: {0}".format(gelenIsim))
        elif listeekle.kontrol(gelenIsim)==0:
            takipEdiyor=False

        if takipEdiyor==False:
                print("bu kisi seni takip etmiyor: {0}".format(gelenIsim))
                kacKisiCikti=1+kacKisiCikti
                driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li["+no+"]/div/div/button/div")\
                    .click()
                sleep(0.4)
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]")\
                        .click()
                    sleep(0.4)
                except:
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[2]]")\
                    .click()
                    sleep(0.4)
                except:
                    pass
        
    manulalEkleme=input("manual isi eklemk istyomsun: y/n :")
    if(manulalEkleme=="y"):
        listeekle.yeniEklemekistenirse()
    else:
        pass
    takipEdenList=[]

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(chrome_options=options)

    sleep(1)
    driver.get("https://www.instagram.com/")
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img").click()
    sleep(0.3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div").click()
    sleep(2)

    takipSayisi=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span")
    takipciSayisi=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span")
    print(takipciSayisi.text)

    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div")\
        .click()

    sleep(2)
    #takici listesini assagı kaydırma
    if(bakilsinmi==True):
        for a in range(int(takipciSayisi.text)-1):
            try:
                flag=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li["+str(a+1)+"]/div")
                                                
                driver.execute_script("arguments[0].scrollIntoView();",flag)
            except:
                sleep(5)
                try:
                    driver.execute_script("arguments[0].scrollIntoView();",flag)
                except:
                    pass
                    print("geçti")
            sleep(0.1)
        print("takip ettiklerinin sonuna ulaşıldı bir kaç saniye bekleyiniz")
    sleep(2)
    if(bakilsinmi==True):
        #takipcilerini jsona yazdımra
        isimler3=driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li/div/div[1]/div[2]/div[1]/span/a/span")
        for c in isimler3:
            isimekle={"name":c.text,
            "takipediyormu":False}
            takipEdenList.append(isimekle)
            listeekle.varmi(isimekle)

    #json dosyasını okuma
    isimListe=[]

    with open("person_name.json","r")as read:       
            try:
                beta=json.load(read)
                for i in beta:
                    isimListe.append(i)
            except:
                print("galiba içi bos bunun")
                pass


    #gelen isimi json dosyadında var kontrol etme

 

    driver.back()
    try:
     driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()
    except:
        print("hata burda 1231")
    sleep(4)

    #takip ettiğin kişlerin sıradan isimlerini konrola gönderme

    b=range(int(takipSayisi.text))
    for a in b:
        try:
            print(a)
            flag=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li["+str(a+1)+"]/div")                         
            driver.execute_script("arguments[0].scrollIntoView();",flag)
        except:
            sleep(1)#burda try exe vardı birtane da onu sildim sanyiye 1 dusurdum

        sleep(0.1)

    for i in b:
        no=str(i+1)
        yeniIsim=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li["+no+"]/div/div[1]/div[2]/div[1]/span/a/span")
        kontrol(yeniIsim.text,no)
        sleep(0.2)

            
        
           
    

                                      

