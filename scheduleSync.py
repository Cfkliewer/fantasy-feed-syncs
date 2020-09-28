import json
import requests

class Schedule(object):
    game_key = None
    season_type = None
    season = None
    week = None
    away_team = None 
    home_team = None
    date_time = None 
    global_game_id = None
    global_away_team_id = None
    global_home_team_id = None
    score_id = None
    status = None

    def __init__(self, GameKey, SeasonType, Season, Week, AwayTeam, HomeTeam, DateTime, GlobalGameID, GlobalAwayTeamID, GlobalHomeTeamID, ScoreID, Status, **kwargs):
        self.game_key = GameKey
        self.season_type = SeasonType
        self.season = Season
        self.week = Week
        self.away_team = AwayTeam
        self.home_team = HomeTeam
        self.date_time = DateTime
        self.global_game_id = GlobalGameID
        self.global_away_team_id = GlobalAwayTeamID
        self.global_home_team_id = GlobalHomeTeamID
        self.score_id = ScoreID
        self.status = Status

    def post_schedule(self):
        dictToSend = {
            "query" : "mutation { insert_Schedule(objects: {" + 
            f"game_key: \"{self.game_key}\", date_time: \"{self.date_time}\", week: {self.week}, season_type: {self.season_type}, season: {self.season}," + 
            f"status: \"{self.status}\", home_team: \"{self.home_team}\", away_team: \"{self.away_team}\", global_game_id: {self.global_game_id}, global_home_team_id: {self.global_home_team_id}," + 
            f"global_away_team_id: {self.global_away_team_id}, score_id: {self.score_id}" +
            "}, on_conflict: { constraint: Schedule_pkey, update_columns: [date_time, week, season_type, season, status, home_team, away_team," + 
            "global_game_id, global_home_team_id, global_away_team_id]}) { affected_rows } }"
        }
        requests.post('https://fantasy-feed-hasura-dev.herokuapp.com/v1/graphql', json=dictToSend)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)