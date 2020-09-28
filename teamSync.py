import json
import requests

class Team(object):
    key = None
    team_id = None
    city = None
    name = None
    conference = None 
    division = None
    full_name = None 
    bye_week = None
    head_coach = None
    primary_color = None
    secondary_color = None
    tertiary_color = None
    quaternary_color = None
    wikipedia_logo_url = None

    def __init__(self, Key, TeamID, City, Name, Conference, Division, FullName, ByeWeek, HeadCoach, PrimaryColor, SecondaryColor, TertiaryColor, QuaternaryColor, WikipediaLogoUrl, **kwargs):
        self.key = Key
        self.team_id = TeamID
        self.city = City
        self.name = Name
        self.conference = Conference
        self.division = Division
        self.full_name = FullName
        self.bye_week = ByeWeek
        self.head_coach = HeadCoach
        self.primary_color = PrimaryColor
        self.secondary_color = SecondaryColor
        self.tertiary_color = TertiaryColor
        self.quaternary_color = QuaternaryColor
        self.wikipedia_logo_url = WikipediaLogoUrl

    def post_team(self):
        dictToSend = {
            "query": "mutation { insert_Team(objects: {"+ f"bye_week: {self.bye_week}, city: \"{self.city}\", conference: \"{self.conference}\", division: \"{self.division}\", full_name: \"{self.full_name}\"," + 
            f"head_coach: \"{self.head_coach}\", key: \"{self.key}\", name: \"{self.name}\" wikipedia_logo_url: \"{self.wikipedia_logo_url}\"," + 
            f"tertiary_color: \"{self.tertiary_color}\", team_id: \"{self.team_id}\", secondary_color: \"{self.secondary_color}\", quaternary_color: \"{self.quaternary_color}\", primary_color: \"{self.primary_color}\""+ 
            "}, on_conflict: {" + "constraint: SyncTeams_pkey, update_columns: [team_id, city, name, conference, division, bye_week, full_name," + 
            "head_coach, primary_color, secondary_color, tertiary_color, quaternary_color, wikipedia_logo_url]}){ affected_rows }}"
        }
        requests.post('https://fantasy-feed-hasura-dev.herokuapp.com/v1/graphql', json=dictToSend)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)