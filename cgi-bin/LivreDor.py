#!/usr/bin/python3
# coding:utf-8

##
#  Ecriture dans fichier "guestbook.html"
#  Paramètres reçus par méthode POST
#
 
import os, cgi, cgitb , datetime, socket

# Lecture des données formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xemail = form.getvalue('email')
xcomment = form.getvalue('commentaire')
	

#L'adresse ip de la machine
xip = cgi.escape(os.environ["REMOTE_ADDR"])

#Type du navigateur
xNavigateur = cgi.escape(os.environ["HTTP_USER_AGENT"])

#ouvrir le fichier nombreDePoste pour savoir le nombre de postes existant

go = open("/home/ginf2021/ohaoudi/public_html/NombrePostes.txt", "r")
i = int(go.read())
i = i + 1
go.close()


# Création du fichier si n'existe pas et ouverture en mode append 
gb = open("/home/ginf2021/ohaoudi/public_html/LivreDor.html", "a")


# Ecriture des informations dans le fichier avec balisage HTML

gb.write ("<div div style='border: 4px solid black; background-color: lightgrey;'>")
gb.write ("<section style='margin-left:2.5em;'>")
gb.write ("<p>Poste numéro :<b>"+str(i)+"</b>, <em>Date</em>: "+str(datetime.date.today())+"<br />\n")
gb.write ("<p><b>Prenom : </b><span>"+str(xprenom)+" </span></p>")
gb.write ("<p><b>Nom :</b> <span>"+str(xnom)+"</span></p>")
gb.write ("<p><b>Email :</b> <span>"+str(xemail)+"</span></p>")
gb.write ("<p><b>Commentaire :</b></p><section style='border: 1px solid black;'><p>&emsp; "+str(xcomment)+"</p></section>")
gb.write ("<p><i>Vous utiliser le navigateur: "+str(xNavigateur)+"</i></p>")
gb.write ("<p>Connecté  à partir de : <b>"+str(xip)+"</b></p>")
gb.write (" </section>")
gb.write ("</div> ")
gb.close()

#renseigner le nouveau nombre
gc = open("/home/ginf2021/ohaoudi/public_html/NombrePostes.txt", "w")
gc.write(str(i))
gc.close()




print('Content-type:text/html')
print("Status: 204 No Response\n\n")


