import time
import random
import json

# Função para simular eventos de alerta
def generate_alert():
    tipos = ["Risco de assalto", "Risco de violência", "Risco de roubo"]
    locais = ["Rua A", "Rua B", "Rua C"]
    
    alerta = {
        "id": random.randint(1, 100),
        "tipo": random.choice(tipos),
        "local": random.choice(locais),
        "data": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    
    return alerta

# Função para gerar e salvar o relatório em tempo real
def generate_real_time_report():
    alertas = []
    
    for _ in range(10):  # Gerar 10 alertas de exemplo
        alertas.append(generate_alert())
        time.sleep(1)  # Atraso de 1 segundo entre alertas
    
    # Gerar relatório em formato JSON
    relatorio_json = json.dumps(alertas, indent=4)
    
    with open('relatorio_temporal.json', 'w') as file:
        file.write(relatorio_json)
    
    print("Relatório de segurança em tempo real gerado: 'relatorio_temporal.json'.")

# Execução do processo
if __name__ == '__main__':
    generate_real_time_report()
