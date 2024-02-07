from conexao_post import conn

cursor = conn.cursor()

id = int(input("Qual ID vc quer alterar: "))
name = input("Qual nome vai ser?: ")
1

cursor.execute("""
    UPDATE game
    SET name = %s
    WHERE id = %s


""",(name,id))

conn.commit()
conn.close()