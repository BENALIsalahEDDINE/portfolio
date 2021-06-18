#!/usr/bin/python3

import cgi, cgitb 
form = cgi.FieldStorage() 
nom = form.getvalue('nom')
prenom = form.getvalue('prenom')
print ("Content-type: text/html; charset=UTF-8")
print()
print ("Bonjour Mr <b> %s %s</b><br>Votre message a été transmis" % (nom,prenom))  