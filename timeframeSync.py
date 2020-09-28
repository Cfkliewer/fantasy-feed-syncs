import json
import requests

class Timeframe(object):
    season_type = None
    season = None
    week = None
    has_games = None
    has_started = None 
    has_ended = None
    api_season = None 
    api_week = None

    def __init__(self, SeasonType, Season, Week, HasGames, HasStarted, HasEnded, ApiSeason, ApiWeek, **kwargs):
        self.season_type = SeasonType
        self.season = Season
        self.week = Week
        self.has_games = HasGames
        self.has_started = HasStarted
        self.has_ended = HasEnded
        self.api_season = ApiSeason
        self.api_week = ApiWeek

    def post_timeframe(self):
        dictToSend = {
	        "query" : "mutation { insert_Timeframe(objects: {" + 
            f"week: {self.week}, season_type: {self.season_type}, season: \"{self.season}\", has_started: \"{self.has_started}\", has_games: \"{self.has_games}\", has_ended: \"{self.has_ended}\", api_week: \"{self.api_week}\", api_season: \"{self.api_season}\""
             + "}, on_conflict: {" + "constraint: Timeframe_season_key, update_columns: [season_type, has_ended, has_games, has_started, week, api_week, api_season]}){ affected_rows }}"
        }
        requests.post('https://fantasy-feed-hasura-dev.herokuapp.com/v1/graphql', json=dictToSend)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)