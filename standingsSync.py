import json
import requests

class Standings(object):
    team_id = None
    season_type = None
    season = None
    conference = None 
    division = None
    team = None 
    name = None
    wins = None
    losses = None
    global_team_id = None

    def __init__(self, TeamID, SeasonType, Season, Conference, Division, Team, Name, Wins, Losses, GlobalTeamID, **kwargs):
        self.team_id = TeamID
        self.season_type = SeasonType
        self.season = Season
        self.conference = Conference
        self.division = Division
        self.team = Team
        self.name = Name
        self.wins = Wins
        self.losses = Losses
        self.global_team_id = GlobalTeamID

    def post_standings(self):
        dictToSend = {
            "query": "mutation { insert_Standings(objects: {" + 
            f"team_id: {self.team_id}, global_team_id: {self.global_team_id}, team: \"{self.team}\", season_type: {self.season_type}, season: {self.season}," + 
            f"name: \"{self.name}\", losses: {self.losses}, division: \"{self.division}\", conference: \"{self.conference}\", wins: {self.wins} " + 
            "}, on_conflict: { constraint: Standings_pkey, update_columns: [global_team_id, season_type, season, conference, division," + 
            "team, name, wins, losses]}) { affected_rows } }"
        }

        requests.post('https://ff-data-api-dev.herokuapp.com/v1/graphql', json=dictToSend)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)