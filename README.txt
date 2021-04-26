!!! FONCTIONNE SEULEMENT AVEC GOOGLE CHROME

#FONCTIONNEMENT
Cet outil permet de faire des téléchargements automatisés sur Moodle. Il vous fera choisir une matière puis après avoir été choisie, tout les fichiers pdf, dossiers, et compressés seront télécharger dans le dossier que vous choisirez. Cela permet d'aller beaucoup plus vite pour récupérer tout les fichiers d'une matière.
Cela utilise Selenium, La version actuelle de Selenium est exclusivement basée sur le HTML et le JavaScript et permet aux développeurs de tester et enregistrer les interactions avec une application Web afin de les répéter ensuite aussi souvent que souhaité, de façon entièrement automatisée.
On aura aussi besoin de chromedriver pour que selenium interagisse avec.


#AVANT UTILISATION
##Télécharger Selenium : 
Tuto installation : https://selenium-python.readthedocs.io/installation.html

Windows (sur le cmd): pip3 install selenium 
Linux, MacOs : pip3 install selenium


##Télécharger googleChromeWebdriver
https://sites.google.com/a/chromium.org/chromedriver/downloads
Tuto Windows : 
https://www.youtube.com/watch?v=Xjv1sY630Uc

Tuto Linux : 
https://www.youtube.com/watch?v=67h3IT2lm40
dans le cmd : 
	unzip ~/chromedriver_linux64.zip
	chmod +x ~/chromedriver
	sudo mv ~/chromedriver /usr/local/share/chromedriver
	sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
	sudo ln -s /usr/local/share/chromedriver /user/bin/chromedriver

(Dans le .py)
if using google-chrome then:
DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"

if using chromium browser then:
DRIVER_LOCATION = "/snap/bin/chromium.chromedriver"
BINARY_LOCATION = "/usr/bin/chromium-browser"


Tuto MacOs :
https://www.youtube.com/watch?v=1KbJdhIpcGo	

Windows, Linux, MacOs  : 
Aller dans Chrome -> Aide -> A propos de Google chrome
Regarder la version et télécharger chromedriver correspondant à la version
(ex : ChromeVersion = 90.0.4430.72, chromedriver =  ChromeDriver90.0.4430.24, preter attention au premier 90)

#Pour l'utilisation
Lancez dans le dossier où se trouve le fichier.py
dans le cmd : python3 fichier.py
1 - Indiquez votre identifiant
2 - Indiquez votre mot de passe 
3 - Indiquez le dossier dans lequel tout sera télécharger
Attendez quelques secondes
4 - Choisir le numéro de la matiere où vous voulez tout télécharger
Attendez
C'est bon ! Vous pouvez aller vérifier


#Autres
Si vous voulez voir ce qui se passe en direct sur votre navigateur, mettez en commentaire dans le code le mode headless
(rajouter "#"options.add_argument("headless"))

Il est possible que le programme ait quelques buggs, faites un CTRL^C et recommencez ou si le problème persiste signalez le.
