from models.team import Team
from models.db import db


def get_all_teams():
    teams = Team.query.order_by(Team.name).all()
    return [team.serialize() for team in teams]


def get_team_by_id(id_team):
    team = Team.query.get(id_team)
    if not team:
        return None
    return team.serialize()