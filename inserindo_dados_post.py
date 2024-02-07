from conexao_post import conn

cursor = conn.cursor()

games = [('Star Wars',2023,9.0)]

for game in games:
    cursor.execute("""

    INSERT INTO game(name,year,score)
    VALUES (%s,%s,%s)
""",game)
conn.commit()
conn.close()
