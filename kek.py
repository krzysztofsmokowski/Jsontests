from pprint import pprint
from mojedane import json
##git class

class Jsoncutter(object):
    def __init__(self, json):
        self.json = json
    def servletprinter(self):
        '''wypisz wszystkie nazwy servletow'''
        for servlet in self.json["web-app"]["servlet"]:
            print servlet["servlet-name"]

    def servletadder(self, servlet):
        '''dodaj nowy servlet do slownika json (we wlasciwym miejscu)#
        dodawanie servleta do jsona
        TODO: zabezpieczyc ta funkcje przed dodaniem zlego typu danych'''
        self.json["web-app"]["servlet"].append(servlet)

    def servletprinter(self, servlet_to_check):
        '''sprawdzanie czy servlet zostal dodany do jsona
        sprawdzmy czy dodal sie nasz servlet'''
        for servlet in self.json["web-app"]["servlet"]:
            if servlet["servlet-name"]==servlet_to_check['servlet-name']:
                print ("Dodalem servlet {}".format(servlet_to_check['servlet-name']))

    def templatechanger(self):
        '''#zmien wszystkie templatePath na 'None'#'''
        for servlet in self.json["web-app"]["servlet"]:
            if 'init-param' in servlet:
                if "templatePath" in servlet['init-param']:
                    print servlet
                    servlet["init-param"]["templatePath"]= "none"
                    print ("papapapa")

moj_nowy_servlet = {"servlet-name": "KrzychoServlet",
                    "servlet-class": "org.cofax.cds.KrzychoServlet"}
moj_nowy_servlet2 = {"servlet-name": "MacioServlet",
                    "servlet-class": "org.cofax.cds.KrzychoServlet"}


checker = Jsoncutter(json)
checker.servletadder(moj_nowy_servlet)
checker.servletadder(moj_nowy_servlet2)
checker.servletprinter(moj_nowy_servlet)
checker.servletprinter(moj_nowy_servlet2)
