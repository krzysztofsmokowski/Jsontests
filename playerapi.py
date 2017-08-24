from flask import Flask
from flask_restful import Resource, Api
from apichecker import PlayerHandling

app = Flask(__name__)
api = Api(app)
player_handling = PlayerHandling()

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class PlayersViewer(Resource):
    def get(self):
        return(player_handling.get_players())

api.add_resource(HelloWorld, '/')
api.add_resource(PlayersViewer, '/players/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
