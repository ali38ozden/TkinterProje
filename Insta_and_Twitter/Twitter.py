from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import messagebox
def basla(Kac_kisi_takip_edilsin):
    global driver
    kacKereGecildi=0
    kacKisiTakipEdildi=0

    Giris_Yapildimi=True

    #-----------------bizim belirlediğimiz
    Bir_Sayfada_KacKisi_Takip=15

    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get("https://twitter.com")
    sleep(4)


    if Giris_Yapildimi==False:
        kullaniciAdi=input("KULLANICI ADI: ")
        kullaniciSifre=input("KULLANICI SİFRE: ")
        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")\
            .send_keys(kullaniciAdi)
        sleep(0.5)

        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")\
            .click()
        sleep(1.5)
        try:
            driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")\
                .send_keys(kullaniciSifre)
        except:
            print("\n\n\n\nkullanici adi hatalı")
            driver.close()
            exit("Tekrar deneyeiniz")
        sleep(0.5)
        driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")\
            .click()

    sleep(5)
    driver.get("https://twitter.com/i/connect_people")
    sleep(5)

    for i in range(40):

        for a in range(Bir_Sayfada_KacKisi_Takip):

            b=str(a+3)
            try: 
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div["+b+"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/span/span")\
                    .click()
                kacKisiTakipEdildi=kacKisiTakipEdildi+1;               
            except:
                kacKereGecildi=kacKereGecildi+1
                pass       
            sleep(1)
        driver.refresh()
        print("Button: "+b+" gecildi                SimdiyeKadarGecilen: "+str(kacKereGecildi)+"            Kac kisi takip ediliyor: "+str(kacKisiTakipEdildi))
        sleep(10)
        if(kacKisiTakipEdildi>Kac_kisi_takip_edilsin):
            break
    print("Bitti")

