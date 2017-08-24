'''
Zaimplementuj program, który będzie:
    - pobieral od uzytkownika:
        - nazwe servleta - np. 'KrzychuSerlvet'
        - port servleta - np 9003
        - ilosc ramu potrzebnego do uruchomiena serlveta - np. '15mb'
        - hosty na jakich maja byc uruchomione servlety - np. ['128.0.0.1', '127.0.0.1']
   - dobierz odpowiednia strukture danych do przechowywania servletow podanych przez uzytkownika

   - program powienien miec mozliwosc wyprinotwania obecnie dodanych servletow i zapisania ich do plikow w formacie json

'''
from pprint import pprint
import json

class Servlethandler(object):

    def __init__(self):
        self.myjson = {"servlets": {}}
        #self.myjson = {"servlets": []}
        print(self.myjson)

    def servletadding(self, servlet_port, servlet_name, ram_value):
        #self.myjson["servlets"].append({'servlet_name':servlet_name, 'port':servlet_port, 'ram':ram_value})
        self.myjson["servlets"][servlet_name] = {'port':servlet_port, 'ram':ram_value}
        print(self.myjson["servlets"])
        print("something")

    def servletprinter(self):
        print(self.myjson)

    def save_to_file(self, filename):
        pass

def get_user_input():
    servlet_port = input('set port of servlet')
    servlet_name = input('set servlet_name')
    ram_value = input('set ram value')
    return servlet_port, servlet_name, ram_value




def add_new_servlet(servlethandler_object):
    servlet_port, servlet_name, ram_value = get_user_input()
    servlethandler_object.servletadding(servlet_port, servlet_name, ram_value)


servlethandler=Servlethandler()
add_new_servlet(servlethandler)
servlethandler.servletprinter()
pprint(servlethandler.servletprinter())
servlethandler.save_to_file('mujplikzdfanymi')
