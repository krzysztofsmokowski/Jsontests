'''
Napisz program ktory wystawia po api sekundy, minuty, godziny, dzien tygodnia, rok, unixtime, wszystkie te wartosci w osobnym, odpowiednim endpoincie
'''
import time
import datetime
from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class apitimer(object):
    def __init__(self):
        self.dateutc = datetime.utcnow()
        self.unix = time.mktime(self.dateutc.timetuple())
    
    def day(self):
        day = self.dateutc.strftime("%d")
        return {'day':day}
    def hour(self):
        hours = self.dateutc.strftime("%H")
        return{'hours':hours}
    def minute(self):
        month = self.dateutc.strftime("%M")
        return{'month':month}
    def second(self):
        day_of_week = self.dateutc.strftime("%A")
        return{'day of the week':day_of_week}

    def unixtime(self):
        print(self.unix)
        return{'unixtime':self.unix}

apidate = apitimer()

class apitimerday(Resource):
    def get(self):
        return(apidate.day())


api.add_resource(apitimerday, '/')

if __name__ == '__main__':
        app.run(host ='back.hellgate.pl',debug=True)

