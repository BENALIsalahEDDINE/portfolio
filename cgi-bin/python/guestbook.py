#!/usr/bin/python3
# coding:utf-8

##
#  Ecriture dans fichier "guestbook.html"
#  Paramètres reçus par méthode POST
#
 
import cgi, cgitb , datetime, os

# Lecture des données formulaire
form = cgi.FieldStorage() 
xnom = form.getvalue('nom')
xprenom  = form.getvalue('prenom')
xville = form.getvalue('ville')
xcomment = form.getvalue('comment')
xip = ""
for key in os.environ.keys():
	if key == "REMOTE_ADDR":
		xip =os.environ[key]
xnav=""
for key in os.environ.keys():
	if key == "HTTP_USER_AGENT":
		xnav=os.environ[key]
# Création du fichier si n'existe pas et ouverture en mode append 
gb = open("/home/ginf2021/ielannaoui/public_html/guestbook.html", "a")
v = open("/home/ginf2021/ielannaoui/public_html/nbrvisiteur.txt","r")
t =  str(v.read())
v.close()
v = open("/home/ginf2021/ielannaoui/public_html/nbrvisiteur.txt","w+")
nbr = int(t)
nbr = nbr + 1
v.write(str(nbr))
# Ecriture des informations dans le fichier avec balisage HTML
gb.write('<div>')
gb.write ("<h5><em>Post</em>:"+str(nbr)+" <em>le</em>: "+str(datetime.date.today())+"</h5><br />\n")
gb.write ("<p><em>De</em>: <strong>"+str(xnom)+", ")
gb.write(str(xprenom)+"</strong><br />")
gb.write ("<em>Email</em>: "+str(xville)+"\n")
gb.write ("<br /><em>Message</em>: "+str(xcomment)+"</p><br/>")
gb.write("Vous utilisez le navigateur: \" "+xnav+" \"<br/>")
gb.write("<em>Connecte a partir de</em>: "+str(xip)+"</div>")
gb.close()

# Sortie sur UA de l'accusé de réception
print ("Content-type: text/html; charset=UTF-8\n")
a = """
<!DOCTYPE html>
<html>
<head>
<title>Merci!...</title>
</head>
 <body style="background-color: #78f5e4;">
<style>
	.body {
  border-radius: 5px;
  
  padding: 20px;
  text-align: center;
  width: 350px;
  height: 400px;
  margin-left:200px;
  border: 1px solid black;
  

}

.cont{
  text-align: center;
  padding: 200px;
}


div {
  border: 4px solid black;
  background-color: lightgrey;
  text-align: center;
  font-size: 40px;font-weight: bold;
	
  width: 500px;
  height: 400px;
  margin-left:400px;
  
  
}
</style>
<div>
"""
print(a)
print ("<p> Merci %s %s </p>" % (xnom, xprenom));
a = """

<p> Votre message a été transmis </p>
<p><em> Au revoir </em></p>
<h4><a href="http://yasmina.emi.ac.ma/~ielannaoui/guestbook.html">Voir ton message</a></h4>
</div>
</body>
</html>
"""
print(a)