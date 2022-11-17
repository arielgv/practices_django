from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

import datetime 


class PersonMaker:
    def __init__(self,nombre,apellido,fechanac):
        self.nombre = nombre
        self.apellido = apellido
        self.fechanac = int(fechanac)


def home(request):
    # HOME IS THE 'SALUTE'TEMPLATE

    templatevariable = open("/Users/arielvillafane/Documents/November/Django/practices/practices/templates/salutes.html")
    template_load = Template(templatevariable.read())
    templatevariable.close()

    the_context = Context()
    document = template_load.render(the_context)


    return HttpResponse(document)


def userpage(request):

    opentemplate = open("/Users/arielvillafane/Documents/November/Django/practices/practices/templates/users.html")
    tmpl = Template(opentemplate.read())
    opentemplate.close()
    ctx = Context()

    document = tmpl.render(ctx)


    return HttpResponse(document)



def mainpage(request):

    #catchingfile = open("mainpage.html")
    #intemplate = Template(catchingfile.read())
    #catchingfile.close()

    templador = loader.get_template('mainpage.html')

    ctx = Context()

    document = templador.render()

    return HttpResponse(document)


def timefunc(request):
    fecha_actual = datetime.datetime.now()
    output ="""
    <html><body><h1>
    Actual Time and date : %s
    </h1></body></html>
    """ % fecha_actual
    return HttpResponse(output)



def testpage(request, entero, name):

    #openfile = open("/testpage.html")
    #templating = Template(openfile.read())
    #openfile.close()
    name = name.upper()

    milista = []
    #['hola', 'mundo', 'esto', 'es', 'una', 'lista']

    #construccion de persona
    per1 = PersonMaker('Ariel','Villafane',1985)

    ctx = Context()
    document = loader.get_template
    {"probando":entero, "nombre": name, 'nombre2':per1.nombre , "ape2" : per1.apellido, "year2": per1.fechanac, 'lista': milista}
    document = templating.render(ctx)

    return HttpResponse(document)





def yearcalculator (request, year,age):
    abrirarchivo = open("/yearcalculator.html")
    templadeo = Template(abrirarchivo.read())
    abrirarchivo.close()



    today= datetime.datetime.today()
    todayyear= today.year
    actualage = age
    calculation = (year - todayyear) + actualage

    ctx = Context({
        "todayyear":todayyear, 
        "actualage":actualage, 
        "year":year , 
        "calculation": calculation
        })



    document = templadeo.render(ctx)
    return HttpResponse(document)
