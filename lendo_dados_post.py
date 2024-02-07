from conexao_post import conn


cursor = conn.cursor()

cursor.execute("SELECT * FROM game")



print(cursor.fetchall())

