from conexao_post import conn

cursor = conn.cursor()


cursor.execute(
    """
    ALTER TABLE game
    ADD COLUMN criador VARCHAR(255);
    """
)

# Confirme a transação
conn.commit()

# Feche a conexão
conn.close()
