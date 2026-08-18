import logging

from db.team_repo import get_team_ids

logger = logging.getLogger(__name__)

_STANDING_COLUMNS = (
    "game_play",
    "win",
    "draw",
    "loss",
    "goals_for",
    "goals_against",
    "goals_differential",
    "points",
)

_INSERT_SQL = (
    "insert into fb_standings "
    "(`team_id`,`event_id`,`country_id`,`team_name`,`game_play`,`win`,`draw`,`loss`,"
    "`goals_for`,`goals_against`,`goals_differential`,`points`) "
    "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
)

_UPDATE_SQL = (
    "update fb_standings set `game_play`=%s, `win`=%s, `draw`=%s, `loss`=%s, "
    "`goals_for`=%s, `goals_against`=%s, `goals_differential`=%s, `points`=%s "
    "where team_name=%s and event_id=%s"
)


def get_existing_team_names(conn, event_id):
    with conn.cursor() as cursor:
        cursor.execute("select team_name from fb_standings where event_id = %s", (event_id,))
        return {row[0] for row in cursor.fetchall()}


def save_standings(conn, country_id, event_id, standings):
    team_ids = get_team_ids(conn, country_id)
    existing = get_existing_team_names(conn, event_id)

    to_insert = []
    to_update = []

    for standing in standings:
        team_name = standing["team_name"]
        if team_name not in team_ids:
            raise ValueError(
                "unknown team '{}' for country_id={}; run the team crawl first".format(team_name, country_id)
            )

        fields = tuple(standing[col] for col in _STANDING_COLUMNS)

        if team_name in existing:
            to_update.append((*fields, team_name, event_id))
        else:
            to_insert.append((team_ids[team_name], event_id, country_id, team_name, *fields))

    with conn.cursor() as cursor:
        if to_insert:
            cursor.executemany(_INSERT_SQL, to_insert)
        if to_update:
            cursor.executemany(_UPDATE_SQL, to_update)

    conn.commit()
    logger.info("event_id=%s: inserted=%d updated=%d", event_id, len(to_insert), len(to_update))
    return {"inserted": len(to_insert), "updated": len(to_update)}
