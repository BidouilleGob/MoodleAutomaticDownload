from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"

username = input("Identifiant : ")
pwd = input("Mot de passe : ")
directory = input("Dossier destination téléchargement (ex : '/home/paul/Documents') : ")
# start selenium chromedriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option("prefs",{"download.default_directory": directory,
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True
})
driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

#go moodle ups
driver.get("https://cas.univ-tlse3.fr/cas/login?service=https%3A%2F%2Fmoodle.univ-tlse3.fr%2Flogin%2Findex.php")

print("Connection....")
#input username
search_user = driver.find_element_by_id("username")
search_user.send_keys(username)

#input password
search_pwd = driver.find_element_by_id("password")
search_pwd.send_keys(pwd)

#Bouton connect
search_submit = driver.find_element_by_name("submit")
search_submit.click()

#Connexion Fin

time.sleep(2)


#Lister toutes les matières
def Matiere() :
        driver.get("https://moodle.univ-tlse3.fr/")
        time.sleep(1)
        liste_matiere = driver.find_elements_by_class_name("media-body")
        if len(liste_matiere) == 0:
            print("Connexion Refusée ou vous n'êtes inscrit à aucune matières")
            exit()

        i = 0
        for i in range(len(liste_matiere)) :
            print(str(i)+ " - " + liste_matiere[i].get_attribute("innerHTML"))

        #choix de la matiere


        contain = False
        while (contain == False) :

            choix_matiere = input("Choississez votre matière (numéro) : ")
            j = 0
            contain = False

            for  j in range(len(liste_matiere)) :
                if int(choix_matiere) == j :
                    contain = True

            if contain == False :
                print("Matière inexistante, veuillez recommencer")

            #Direction vers le lien de la matière

        x = driver.find_element_by_xpath("//span[text()='"+liste_matiere[int(choix_matiere)].get_attribute("innerHTML")+"']")
        y = x.find_element_by_xpath("./../../..")
        lien_matiere = y.get_attribute("href")
        driver.get(lien_matiere)

        return lien_matiere


#download folder pdf

def download_folder(lien_matiere):
    driver.get(lien_matiere)
    liste_folder_parent = []
    liste_folder = driver.find_elements_by_xpath("//img[@src='https://moodle.univ-tlse3.fr/theme/image.php/boost/folder/1613982422/icon']")
    if len(liste_folder) > 0 :
        for i in range(len(liste_folder)) :
            lien = liste_folder[i].find_element_by_xpath("./..").get_attribute("href")
            liste_folder_parent.append(lien)

    if len(liste_folder_parent) > 0 :
        for i in range(len(liste_folder_parent)) :
            driver.get(liste_folder_parent[i])
            download_folder = driver.find_elements_by_xpath("//button[@class='btn btn-secondary']")
            #si il y a un bouton "telecharger dossier"
            if len(download_folder) > 0:
                download_folder[0].click()
                folder_name = driver.find_element_by_xpath("//h2")
                print(folder_name.get_attribute("innerHTML") + ".zip")
            else:
                download_pdf(liste_folder_parent[i], True)


#download file pdf
def download_pdf(lien_matiere, folder):
    driver.get(lien_matiere)
    liste_pdf_parent = []
    liste_pdf = driver.find_elements_by_xpath("//img[@src='https://moodle.univ-tlse3.fr/theme/image.php/boost/core/1613982422/f/pdf-24']")
    if len(liste_pdf) > 0 :
        for i in range(len(liste_pdf)) :
            if folder == True :
                lien = liste_pdf[i].find_element_by_xpath("./../..").get_attribute("href")
            else :
                lien = liste_pdf[i].find_element_by_xpath("./..").get_attribute("href")
            liste_pdf_parent.append(lien)

    if len(liste_pdf_parent) > 0 :
        for i in range(len(liste_pdf_parent)) :
            time.sleep(0.5)
            try  :
                driver.get(liste_pdf_parent[i])
            except Exception as e:
                print(e)

            search_pdf = driver.find_elements_by_xpath('//div[@class="resourceworkaround"]//a[@href=contains(text(),"' + ".pdf" + '")]')
            if len(search_pdf) > 0 :
                 search_pdf[0].click()
                 print(search_pdf[0].get_attribute("innerHTML"))
            else :
                try :
                    print(liste_pdf[i].get_attribute("alt"))
                except Exception as e:
                    print("(NomFichierInconnu.pdf)")



#download zip

def download_zip(lien_matiere) :
    driver.get(lien_matiere)
    liste_zip_parent = []
    liste_zip = driver.find_elements_by_xpath("//img[@src='https://moodle.univ-tlse3.fr/theme/image.php/boost/core/1613982422/f/archive-24']")
    if len(liste_zip) > 0 :
        for i in range(len(liste_zip)) :
            lien = liste_zip[i].find_element_by_xpath("./..")
            liste_zip_parent.append(lien.get_attribute("href"))

    if len(liste_zip_parent) > 0:
        for i in range(len(liste_zip)) :
            driver.get(liste_zip_parent[i])
            search_zip = driver.find_elements_by_xpath("//div[@class='resourceworkaround']//a")
            if len(search_zip) > 0 :
                search_zip[0].click()
                print(search_zip[0].get_attribute("innerHTML"))
            else :
                print("dir.zip")

#main
continuer = "o"

while (continuer == "o") :

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_experimental_option("prefs",{"download.default_directory": directory,
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    })
    driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

    #go moodle ups
    driver.get("https://cas.univ-tlse3.fr/cas/login?service=https%3A%2F%2Fmoodle.univ-tlse3.fr%2Flogin%2Findex.php")

    #input username
    search_user = driver.find_element_by_id("username")
    search_user.send_keys(username)

    #input password
    search_pwd = driver.find_element_by_id("password")
    search_pwd.send_keys(pwd)

    #Bouton connect
    search_submit = driver.find_element_by_name("submit")
    search_submit.click()

    #Connexion Fin

    time.sleep(1)
    lien_matiere = Matiere()
    matiere_by_title = driver.find_elements_by_xpath("//span[@class='media-left']//i[@class='icon fa fa-folder-o fa-fw ']")
    if len(matiere_by_title) <= 0 :
        download_pdf(lien_matiere, False)
        download_zip(lien_matiere)
        download_folder(lien_matiere)
    else :
        link_matiere_by_title = []

        for i in range(len(matiere_by_title)) :
            lien = matiere_by_title[i].find_element_by_xpath("./../../../..")
            link_matiere_by_title.append(lien.get_attribute("href"))

        for i in range(len(link_matiere_by_title)) :
            driver.get(link_matiere_by_title[i])
            download_pdf(link_matiere_by_title[i], False)
            download_zip(link_matiere_by_title[i])
            download_folder(link_matiere_by_title[i])
    continuer = input("Voulez-vous continuer sur une autre matière ?  (tapez 'o' pour continuer) : ")
    if continuer != "o" :
        exit()
    directory = input("Dossier destiné au téléchargement : ")

    driver.close()
    driver.quit()


# close browser and quit driver
driver.close()
driver.quit()
