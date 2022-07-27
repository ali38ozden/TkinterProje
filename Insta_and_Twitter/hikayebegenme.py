from time import sleep
from selenium import webdriver

def basla():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(chrome_options=options)

    driver.maximize_window()
    driver.get("https://www.instagram.com") 
    sleep(2)
    
    canlikacta=3
    for say in range(5):
            try:
                canli=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[2]/div/div/div/div/ul/li["+str(say+3)+"]/div/button/div[1]/div[2]")
                print(canli.text)
                if canli.text=="CANLI":
                    print("canlı yayın var")
                    canlikacta=say+4
                    pass
                else:
                    print("canlı gecildi")
                    pass
            except:
                print("canli bulunamadı")
                pass

    while True:
        try:
            a=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[2]/div/div/div/div/ul/li["+str(canlikacta)+"]/div/button")
            if a.accessible_name[-11:-1]==", görülmed":
                print("hikaye izlenebilir") 
                a.click()
                sleep(0.5)
                hikayeGirildi=True
            else:
                hikayeGirildi=False                                  
        except:
            hikayeGirildi=True
            print("burya dustu 1")
        if(hikayeGirildi==True):
            print("girildi")
            try:
                kacHikayeVar=driver.find_elements_by_css_selector("._ac3n").__len__()
                kacHikayeGecildi=driver.find_elements_by_css_selector("._ac3p").__len__()
                print(kacHikayeVar-kacHikayeGecildi)
                for i in range(kacHikayeVar-kacHikayeGecildi):
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[2]/span/button").click()
                    except:
                        print("beğen bulunamdı")
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div").click()
                    except:
                        print("hikaye gec button bulunamadi")
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div/svg").click()
                    except:  
                        print("bu ne bilmiyorum")                         
                        pass
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div").click()
                    except: 
                        print("bu da ne bilimiyorum")                          
                        pass
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]").click()
                    except:
                        print("bir gec button daha gecildi")
                        pass

            except:
                print("burya dustu 2")
                pass


