#!/usr/bin/python
# coding:utf-8
# Pour le source avec des caractères Unicode

# Import de APIs CGI 
import cgi, cgitb 

# On récupère la zone des paramètres
form = cgi.FieldStorage() 

# On récupère les valeurs de chaque paramètre
vnom = form.getvalue('nom')
vprenom  = form.getvalue('prenom')


# Sortie du HTML
print "Content-type: text/html; charset=UTF-8"
print
print """
<!DOCTYPE html>
<html>
<head>
<title>Bonjour - version 2</title>
</head>
<body>
"""
print "<p> Hello %s %s </p>" % (vnom, vprenom)   # Sortie des données nom et prenom
print """
<em> Au revoir </em>
</body>
</html>
"""

