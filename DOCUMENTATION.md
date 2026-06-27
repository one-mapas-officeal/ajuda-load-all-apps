# Explicação Detalhada do Código

Este arquivo detalha o funcionamento do script `helper.py`.

## Estrutura do Script

```python
import psutil      # Biblioteca para monitorar recursos do sistema (CPU/RAM)
import subprocess  # Permite executar comandos do terminal (ADB)
import time        # Utilizado para pausas e intervalos do loop

# --- DETECÇÃO AUTOMÁTICA ---
# Obtém o total de memória RAM instalada no computador
TOTAL_RAM = psutil.virtual_memory().total
# Define o gatilho: se a RAM livre for menor que 20% do total, o alerta dispara
LIMITE_RAM_BYTES = TOTAL_RAM * 0.20
# Define o gatilho: se o uso de CPU for maior que 80%, o alerta dispara
LIMITE_CPU_PORC = 80.0

def enviar_comando_android(comando_shell):
    # Adiciona 'adb shell' ao comando recebido e executa no terminal
    try:
        subprocess.run(["adb", "shell"] + comando_shell.split(), check=True)
    except subprocess.CalledProcessError:
        pass

def monitorar():
    print(f"Monitorando Sistema...")
    
    # Loop infinito que mantém o monitoramento rodando
    while True:
        # Coleta o uso atual da CPU com uma média de intervalo de 1 segundo
        cpu = psutil.cpu_percent(interval=1)
        # Coleta a quantidade de memória RAM disponível em bytes
        ram_livre = psutil.virtual_memory().available
        
        # Verifica se algum dos limites foi atingido
        if ram_livre < LIMITE_RAM_BYTES or cpu > LIMITE_CPU_PORC:
            print(f"ALERTA: CPU {cpu}% | RAM Livre {ram_livre / (1024**3):.2f} GB")
            # Aqui você insere a ação no Android, exemplo:
            # enviar_comando_android("input keyevent 3")
        
        # Pausa de 2 segundos antes da próxima verificação
        time.sleep(2)

if __name__ == "__main__":
    monitorar()
