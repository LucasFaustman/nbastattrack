import datetime as dt
from marshmallow import Schema, fields

class SeasonDataSchema(Schema):
    fg3_pct = fields.Float()
    fg_pct = fields.Float()
    ft_pct = fields.Float()
    games_played = fields.Integer()
    min = fields.String()
    pts = fields.Float()
    season = fields.Integer()

class Player(object):
    def __init__(self, first_name, last_name, position, team, season_data):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        self.season_data = season_data

class PlayerSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    position = fields.Str()
    team = fields.Str()
    season_data = fields.Nested(SeasonDataSchema, many=True)