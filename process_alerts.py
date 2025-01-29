import json
from collections import Counter

# Função para simular a captura de alertas (normalmente seria de um banco de dados ou API)
def get_alerts():
    return [
        {"id": 1, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:00:00Z"},
        {"id": 2, "tipo": "Risco de violência", "local": "Rua B", "data": "2025-01-29T10:15:00Z"},
        {"id": 3, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T10:30:00Z"},
        {"id": 4, "tipo": "Risco de roubo", "local": "Rua C", "data": "2025-01-29T10:45:00Z"},
        {"id": 5, "tipo": "Risco de assalto", "local": "Rua A", "data": "2025-01-29T11:00:00Z"}
    ]

# Função para gerar um relatório de alertas por tipo
def gerar_relatorio(alertas):
    tipos_alertas = [alerta['tipo'] for alerta in alertas]
    contagem_tipos = dict(Counter(tipos_alertas))
    
    # Gerar relatório em JSON
    relatorio_json = json.dumps(contagem_tipos, indent=4)
    
    # Salvar relatório
    with open('relatorio_alertas.json', 'w') as file:
        file.write(relatorio_json)
    
    print("Relatório gerado com sucesso: 'relatorio_alertas.json'.")

# Execução do processo
if __name__ == '__main__':
    alertas = get_alerts()
    gerar_relatorio(alertas)
