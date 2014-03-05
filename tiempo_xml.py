#coding: utf-8
import requests
import json
from lxml import etree
from jinja2 import Template
plantilla = open("plantilla.html","r")
capitales = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']

html = ''
for linea in plantilla:
	html += linea

plantilla = Template(html)

pasar = True

lista_temp_min = []
lista_temp_max = []
lista_redon = []
lista_direccion = []

def orientacion(direccion):
	"""Función que calcula la dirección de la que procede el viento"""
	for grados in str(direccion):
		if direccion >= 337 and direccion < 22.5:
			return 'N'
		elif direccion >= 22.5 and direccion < 67.5:
			return 'NE'
		elif direccion >= 67.5 and direccion < 112.5:
			return 'E'
		elif direccion >= 112.5 and direccion < 157.5:
			return 'SE'
		elif direccion >= 157.5 and direccion < 202.5:
			return 'S'
		elif direccion >= 202.5 and direccion < 247.5:
			return 'SO'
		elif direccion >= 247.5 and direccion < 292.5:
			return 'O'
		elif direccion >= 292.5 and direccion < 337.5:
			return 'NO'

for capital in capitales:
	valores = {'q': '%s' % capital,'mode': 'xml','units': 'metric','lang': 'es'}
	resultado = requests.get('http://api.openweathermap.org/data/2.5/weather?',params=valores)
#resultado = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seville&mode=xml&units=metric&lang=es')

arbol = etree.parse(resultado.text)
print resultado.text

	#if dicc == {u'message': u'Error: Not found city', u'cod': u'404'}:
	#	pasar = False
	#	temp_min = ' '
	#	temp_max = ' '
	#	redon = ' '
	#	direccion = ' '


	#if pasar == True:
	#	temp_min = dicc["main"]["temp_min"] - 273
	#	temp_max = dicc["main"]["temp_max"] - 273
	#	viento = round(dicc["wind"]["speed"] * 1.61,2)
	#	redon = round(viento, 2)
	#	direccion = dicc["wind"]["deg"]
	#	direccion = orientacion(direccion)
	#	lista_temp_min.append(temp_min)
	#	lista_temp_max.append(temp_max)
	#	lista_redon.append(redon)
	#	lista_direccion.append(direccion)

#	pasar = True

#plantilla = plantilla.render(capitales=capitales,temp_min=lista_temp_min,temp_max=lista_temp_max,speed=lista_redon,direccion_viento=lista_direccion)

#resultado=open('salida.html','w')
#resultado.write(plantilla)

#webbrowser.open("salida.html")