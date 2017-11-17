import requests
import time
import datetime

class PlayerHandling(object):
    def __init__(self):
        self.old_viewers = []

    def get_api_json(self):
        request = {}
        request = requests.get("http://tmi.twitch.tv/group/user/lirik/chatters")
        return request.json()

    def list_comparison(self, list1, list2):
        '''function is comparing lists: 1 and 2'''
        diff_1_to_2 = list(set(list1) - set(list2))
        diff_2_to_1 = list(set(list2) - set(list1))
        return diff_2_to_1 + diff_1_to_2

    def get_players(self):
        '''returning players dfference list as json '''
        request = self.get_api_json()
        new_viewers = request['chatters']['viewers']
        difference = self.list_comparison(new_viewers, self.old_viewers)
        self.old_viewers = request['chatters']['viewers']
        return {'players': difference}


def main():
    player_handler = PlayerHandling()
    while True:
        player_handler.get_players()
        time.sleep(10)


if __name__ == "__main__":
    main()

