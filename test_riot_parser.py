from riotparser import RiotOfGames
import unittest
from unittest.mock import MagicMock





class WeatherStationsTest(unittest.TestCase):
    def test_stations_summary_without_counter(self):
        weather = WeatherStations('')
        weather._ask_api = MagicMock(return_value=[
            {'id':1, 'stationName':'Wroclaw'},
            {'id':2, 'stationName':'Poznan'}
            ])
        self.assertEqual({1: "Wroclaw", 2: "Poznan"}, weather.stations_summary())

    def test_stations_summary_without_counter_3_items(self):
        weather = WeatherStations('x')
        weather._ask_api = MagicMock(return_value=[
            {'id':1, 'stationName':'Wroclaw'},
            {'id':2, 'stationName':'Poznan'},
            {'id':3, 'stationName':'Horzuf'}
            ])
        summary = weather.stations_summary()
        self.assertEqual({1: "Wroclaw", 2: "Poznan"}, summary)


