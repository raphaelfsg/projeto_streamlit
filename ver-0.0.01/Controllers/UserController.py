import services.database as db

def incluir(p_team):
    count = db.cursor.execute("""
    INSERT INTO project_user (p_name, p_age, p_occupation, p_social)
    VALUES (?,?,?,?)""",
    p_team.name, p_team.age, p_team.occupation, p_team.social).rowcount 
    db.cnxn.commit()

