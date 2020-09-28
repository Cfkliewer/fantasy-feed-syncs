import json
import requests

class Player(object):
    player_id = None
    team = None
    number = None
    first_name = None
    last_name = None 
    position = None
    height_feet = None 
    height_inches = None 
    weight = None
    age = None
    bye_week = None
    team_id = None
    global_team_id = None

    def __init__(self, PlayerID, Team, Number, FirstName, LastName, Position, HeightFeet, HeightInches, Weight, Age, ByeWeek, TeamID, GlobalTeamID, **kwargs):
        self.player_id = PlayerID
        self.team = Team
        self.number = Number
        self.first_name = FirstName
        self.last_name = LastName
        self.position = Position
        self.height_feet = HeightFeet
        self.height_inches = HeightInches
        self.weight = Weight
        self.age = Age
        self.bye_week = ByeWeek
        self.team_id = TeamID
        self.global_team_id = GlobalTeamID

    def post_player(self):
        dictToSend = {
            "query": "mutation { insert_PlayerSync(objects: {" + 
            f"player_id: {self.player_id}, team_id: {self.team_id}, global_team_id: {self.global_team_id}, team: \"{self.team}\", first_name: \"{self.first_name}\"," + 
            f"last_name: \"{self.last_name}\", age: {self.age}, number: {self.number}, position: \"{self.position}\", height_feet: {self.height_feet}, height_inches: {self.height_inches}, weight: {self.weight}, bye_week: {self.bye_week}" +
            "}, on_conflict: { constraint: PlayerSync_pkey, update_columns: [team_id, global_team_id, team, first_name, last_name, age, number, position, height_inches, height_feet, weight, bye_week]}) { affected_rows } }"
        }

        print(dictToSend)
        requests.post('https://fantasy-feed-hasura-dev.herokuapp.com/v1/graphql', json=dictToSend)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)