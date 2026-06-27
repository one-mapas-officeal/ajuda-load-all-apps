import psutil
import subprocess
import time

# --- DETECÇÃO AUTOMÁTICA ---
# Define limites baseados em porcentagem do total (Ex: 20% da RAM livre dispara o alerta)
TOTAL_RAM = psutil.virtual_memory().total
LIMITE_RAM_BYTES = TOTAL_RAM * 0.20  # Dispara se menos de 20% da RAM estiver livre
LIMITE_CPU_PORC = 80.0

def enviar_comando_android(comando_shell):
    try:
        subprocess.run(["adb", "shell"] + comando_shell.split(), check=True)
    except subprocess.CalledProcessError:
        pass

def monitorar():
    print(f"Monitorando Sistema...")
    print(f"Total RAM detectada: {TOTAL_RAM / (1024**3):.2f} GB")
    
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram_livre = psutil.virtual_memory().available
        
        if ram_livre < LIMITE_RAM_BYTES or cpu > LIMITE_CPU_PORC:
            print(f"ALERTA: CPU {cpu}% | RAM Livre {ram_livre / (1024**3):.2f} GB")
            # Exemplo de ação:
            # enviar_comando_android("input keyevent 3") 
        
        time.sleep(2)

if __name__ == "__main__":
    monitorar()
