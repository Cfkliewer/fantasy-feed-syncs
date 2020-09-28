from flask import Flask
from timeframeSync import Timeframe
from teamSync import Team
from scheduleSync import Schedule
from standingsSync import Standings
from playerSync import Player
import requests

class Sync():
    @staticmethod
    def SyncTimeframe():
        res = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Timeframes/current?key=c4f34674f7e84173a3ee66d91abae1ab')
        for i in res.json():
            timeframe = Timeframe.from_json(i)
            timeframe.post_timeframe()
    
    @staticmethod
    def SyncTeam():
        res = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/AllTeams?key=c4f34674f7e84173a3ee66d91abae1ab')
        for i in res.json():
            team = Team.from_json(i)
            team.post_team()
        
    @staticmethod
    def SyncSchedule():
        res = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Schedules/2020REG?key=c4f34674f7e84173a3ee66d91abae1ab')
        for i in res.json():
            schedule = Schedule.from_json(i)
            schedule.post_schedule()
        
    @staticmethod
    def SyncStanding():
        res = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Standings/2020REG?key=c4f34674f7e84173a3ee66d91abae1ab')
        for i in res.json():
            standings = Standings.from_json(i)
            standings.post_standings()

    @staticmethod
    def SyncPlayer():
        res = requests.get('https://api.sportsdata.io/v3/nfl/scores/json/Players?key=c4f34674f7e84173a3ee66d91abae1ab')
        for i in res.json():
            player = Player.from_json(i)
            player.post_player()
