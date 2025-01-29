import sqlite3
import json

# Função para criar o banco de dados e a tabela
def create_db():
    conn = sqlite3.connect('alertas.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS alertas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            local TEXT,
            data TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para salvar alertas no banco de dados
def save_alerta(alerta):
    conn = sqlite3.connect('alertas.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO alertas (tipo, local, data)
        VALUES (?, ?, ?)
    ''', (alerta['tipo'], alerta['local'], alerta['data']))
    
    conn.commit()
    conn.close()
    print(f'Alerta {alerta["id"]} salvo no banco de dados.')

# Função para simular o recebimento de alertas e salvar no banco
def save_alerts():
    alertas = [
        {"id": 1, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:00:00Z"},
        {"id": 2, "tipo": "Risco de violência", "local": "Rua B", "data": "2025-01-29T10:15:00Z"},
        {"id": 3, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:30:00Z"}
    ]
    
    for alerta in alertas:
        save_alerta(alerta)

# Execução do processo
if __name__ == '__main__':
    create_db()
    save_alerts()
