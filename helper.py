import psutil
import subprocess
import time

# --- CONFIGURAÇÕES ---
TOTAL_RAM = psutil.virtual_memory().total
LIMITE_RAM_BYTES = TOTAL_RAM * 0.20
LIMITE_CPU_PORC = 80.0

def comando_adb(comando):
    subprocess.run(["adb", "shell"] + comando.split(), capture_output=True)

def processar_tarefa_no_celular():
    print("[PC] Iniciando ciclo: Despertar -> Executar -> Finalizar")
    
    # 1. Despertar celular (Liga a tela)
    comando_adb("input keyevent 26") 
    time.sleep(1)
    
    # 2. Desbloquear (se necessário, deslizar para cima)
    comando_adb("input swipe 500 1500 500 500")
    time.sleep(1)
    
    # 3. Aqui você abre seu app ou executa a tarefa
    # Exemplo: Abrir um app específico pelo nome do pacote
    # comando_adb("monkey -p com.exemplo.seuapp 1")
    
    print("[PC] Executando tarefas no celular...")
    time.sleep(10) # Tempo de processamento no celular
    
    # 4. Fechar app (ou voltar para home)
    comando_adb("input keyevent 3")
    time.sleep(1)
    
    # 5. Desligar a tela (Tela preta)
    comando_adb("input keyevent 26")
    print("[PC] Celular em modo de descanso.")

def monitorar():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram_livre = psutil.virtual_memory().available
        
        if ram_livre < LIMITE_RAM_BYTES or cpu > LIMITE_CPU_PORC:
            print(f"ALERTA: CPU {cpu}% | RAM {ram_livre / (1024**3):.2f} GB")
            processar_tarefa_no_celular()
            
        time.sleep(2)

if __name__ == "__main__":
    monitorar()
