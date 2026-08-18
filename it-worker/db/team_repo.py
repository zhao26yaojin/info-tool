import logging

logger = logging.getLogger(__name__)


def get_team_ids(conn, country_id):
    with conn.cursor() as cursor:
        cursor.execute("select id, name from fb_team where country_id = %s", (country_id,))
        return {name: team_id for team_id, name in cursor.fetchall()}


def insert_teams(conn, country_id, team_names):
    existing = get_team_ids(conn, country_id)
    new_names = [name for name in team_names if name not in existing]

    if new_names:
        with conn.cursor() as cursor:
            cursor.executemany(
                "insert into fb_team (id, name, country_id) values (null, %s, %s)",
                [(name, country_id) for name in new_names],
            )
        conn.commit()

    logger.info("country_id=%s: %d new teams inserted", country_id, len(new_names))
    return {"inserted": len(new_names)}
