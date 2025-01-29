import requests
import json

# Função para enviar alertas ao backend
def send_alert_to_backend(alerta):
    url = 'http://localhost:5000/alert'  # Rota do seu backend
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(alerta), headers=headers)
    
    if response.status_code == 200:
        print(f'Alerta {alerta["id"]} enviado com sucesso!')
    else:
        print(f'Falha ao enviar alerta {alerta["id"]}: {response.status_code}')

# Função para simular envio de múltiplos alertas
def send_alerts():
    alertas = [
        {"id": 1, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:00:00Z"},
        {"id": 2, "tipo": "Risco de violência", "local": "Rua B", "data": "2025-01-29T10:15:00Z"},
        {"id": 3, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:30:00Z"}
    ]
    
    for alerta in alertas:
        send_alert_to_backend(alerta)

# Execução do processo
if __name__ == '__main__':
    send_alerts()
