#!/usr/bin/python3.4

import os
from bottle import *
import time
from bottle import SimpleTemplate as tp
import pymysql

os.chdir('/home/jozi/python/') 
#move o programa para o diretorio de execução /home/user/python.

con = pymysql.connect(user= "", host= "", passwd= "") 
cursor = con.cursor()
cursor.execute("use senha;")
#Configuração da coneção com o banco de dados.

entra = open("login.html", "r") 
entra = entra.read()
#abertura do arquivo login.html que sera a pagina de login.

arq = open("index.html", "r")
arq = arq.read()
# abertura do arquivo index.html que sera a pagina principal do programa.

@get("/login") 
def entrar():  
	return(entra)
# função do bottle que faz o request e retorna a pagina de login.

@post("/") 
def postar():
	
	hash = request.forms.get("nome")
	hash2 = request.forms.get("senha")
	cursor.execute("select * from valor;")
	for i in cursor:
		teste = (hash == i[0] and hash2 == i[1])
		if teste == True:
			return(arq)
		else:
			pass
	return("<h1> Acesso negado</h1>")
# .... ............ que faz o post e retorna a pagina principal.

@post("/default")
def page():
	mux = request.forms.get("boga")
	if mux == "j" or mux == "a":
		os.system("firefox www.youtube.com")
		return(arq)
	else:
		return(entra)
#cria um novo  request na pagina inicial

run(host="192.168.0.123", port=8080)
 
