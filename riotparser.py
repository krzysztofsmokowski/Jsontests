'''
This module is used for getting data out of s3 riot developer example.
In this particular module I am using locally downloaded file with data
in json format.
Original link:
https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/matches1.json #is that module useful for anything elso or it just parsing the example?
'''
import json
import argparse


class LolJsonParser(object):
    '''
This class is working on input in form of json. #indent is wrong + not true
I am using json locally to avoid unecessary requests on data that
is not changing.
Class is used for getting all sort of informations about league of legends games
and details about them (specific gear of players etc)
Input: file with data in json format #not true
Output: At this moment Argparse is used to get data out of this #class returns object, not argparse, you are not inheriting after argparse here
program but in future it can be also in json format
'''

    def __init__(self, jsonfile):
        self.jsondata = json.load(open(jsonfile)) #so it only takes file names?? if you really want that behavior, move json loading into different hidden method, for easier Us
        self.teams_with_ids = {} # same as below
        self.teamids_with_participants = {} #shall it be here? is it really needed to have them in init? Maybe return would be wiser from methods?

    def gameids_and_teams(self, records=int(1)): #it shall be assumed that records are int.
        '''
    Function is using json from __init__. #indentatnion + not revelant info
    Main purpose is to get gameId and match it in form of dict with teams.
    Teams are having detailed data inside such as: firstblood, firstbaron etc.
    In order to shorten output i used kwargs named records, that by default is equal 0.
    Input: records passed by argparse or left in default form
    Output: dictionary with gameId matched with teams
    '''
        for dictionary in self.jsondata["matches"][:records]: # dictionary is a generic name, means nothing, be more descriptive with variable names + comment from method name
            self.teams_with_ids[dictionary["gameId"]] = dictionary["teams"] # 'dictionary' does not help with visibility, you don't need to put self.teams_with_ids into object, you can return it straight from the method.
        return self.teams_with_ids # same as above, you can just return it here, you don't have to put it into object

    def teamid_and_participants(self, team=int(9)):
        '''
        Function is using json from __init__. #not revelant info
        Created to know match teamId with participants of this team.
        Data in "participants" dict is showing info about #not finished?
        '''
        for dictionary in self.jsondata["matches"]: #same problem as above
            self.teamids_with_participants[dictionary["participants"][int(team)]["teamId"]] = dictionary["participants"][int(team)] #same
        return self.teamids_with_participants #same


def main():
    '''
    Main function in which argparse are being declared and class is
    assigned to an object. #not revelant
    Function is taking no input
    Output: served by argparse #no. there is no outout, as there is no return ~!!!
    '''
    parser = argparse.ArgumentParser() #no description for the program when --help is invoked.
    parser.add_argument("--idswithteams", help='printing teams with ids of games') #they are boolean args
    parser.add_argument("--teams_and_participants", help='printing teamIds with participants details') #same as above, set is as boolean
    #what is default expected behaviour from the script?
    riot = LolJsonParser("riotjson.json") #shall it take filename or nested python structure?
    args = parser.parse_args()
    if args.idswithteams:
        print(riot.gameids_and_teams(args.idswithteams))
    if args.teams_and_participants:
        print(riot.teamid_and_participants(args.teams_and_participants))


if __name__ == '__main__':
    main()
