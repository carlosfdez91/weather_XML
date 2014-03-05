#coding: utf-8
import requests
import json
from lxml import etree
from jinja2 import Template
plantilla = open("plantilla.html","r")
capitales = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']


resultado = requests.get('http://api.openweathermap.org/data/2.5/weather?',params={'q':'%s,&mode=xml&units=metric&lang=es' % capitales})
arbol = etree.parse(resultado.text)
print resultado.text

