#jupyter start
import os
import getpass
import platform

#aktuális user meghatározása
user = getpass.getuser()
#aktuális operációs rendszer meghatározása
osys = platform.system()

def cmline():
    #mappa beállítása, user és aktuális mappa kiírása, jupyter elindítása
    os.chdir(dir)
    print("Helló, "+user+"!")
    print("Aktuális mappa: "+dir)
    os.system("jupyter notebook --port 8888")

if osys == "Windows":
	#a jupyter indulási mappájának meghatározása
	dir = "c:/users/" +user+ "/Documents/"
	cmline()
	
elif osys == "Linux":
    #a jupyter indulási mappájának meghatározása
	dir = "/home/" +user+ "/Documents"
	cmline()
		
elif osys == "Darwin":
    #a jupyter indulási mappájának meghatározása
	dir = "users/" +user+ "/Documents"
	cmline()
		
else:
	print("Hiba! Használt operációs rendszer: "+osys+".")
