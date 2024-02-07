from conexao_post import conn

cursor = conn.cursor()

id = int(input("Qual ID vc quer alterar: "))

sql = """
DELETE from game
WHERE id = %s
"""

cursor.execute(sql,(id,))

conn.commit()
conn.close()