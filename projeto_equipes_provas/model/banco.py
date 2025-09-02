import mysql.connector

class Banco:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # coloque a senha do seu MySQL se existir
            database="competicoes"
        )
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS membros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                equipe_id INT,
                FOREIGN KEY (equipe_id) REFERENCES equipes(id)
            )
        """)
        self.conn.commit()
