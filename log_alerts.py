import logging

# Configuração do log
logging.basicConfig(filename='seguranca.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para logar o alerta
def log_alerta(alerta):
    message = f"Alerta {alerta['id']} - Tipo: {alerta['tipo']} - Local: {alerta['local']} - Data: {alerta['data']}"
    logging.info(message)
    print(f"Logado: {message}")

# Função para simular a captura de alertas e logá-los
def log_alerts():
    alertas = [
        {"id": 1, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:00:00Z"},
        {"id": 2, "tipo": "Risco de violência", "local": "Rua B", "data": "2025-01-29T10:15:00Z"},
        {"id": 3, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:30:00Z"}
    ]
    
    for alerta in alertas:
        log_alerta(alerta)

# Execução do processo
if __name__ == '__main__':
    log_alerts()
