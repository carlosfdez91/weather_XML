#coding: utf-8
import requests
import webbrowser
from lxml import etree
from jinja2 import Template
plantilla = open("plantilla.html","r")
capitales = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']

html = ''
for linea in plantilla:
	html += linea

plantilla = Template(html)

lista_temp_min = []
lista_temp_max = []
lista_velocidad = []
lista_direccion = []

for capital in capitales:
	opciones = {'q': '%s' % capital,'mode': 'xml','units': 'metric','lang': 'es'}
	resultado = requests.get('http://api.openweathermap.org/data/2.5/weather?',params=opciones)
	raiz = etree.fromstring(resultado.text.encode("utf-8"))

	minima = raiz.find("temperature")
	temp_min = round(float(minima.attrib["min"]),1)
	maxima = raiz.find("temperature")
	temp_max = round(float(maxima.attrib["max"]),1)
	velocidad = raiz.find("wind/speed")
	speed = velocidad.attrib["value"]
	orientacion = raiz.find("wind/direction")
	direccion = orientacion.attrib["code"]
	
	lista_temp_min.append(temp_min)
	lista_temp_max.append(temp_max)
	lista_velocidad.append(speed)
	lista_direccion.append(direccion)


plantilla = plantilla.render(capitales=capitales,temp_min=lista_temp_min,temp_max=lista_temp_max,speed=lista_velocidad,direccion_viento=lista_direccion)

resultado=open('salida.html','w')
resultado.write(plantilla)

webbrowser.open("salida.html")