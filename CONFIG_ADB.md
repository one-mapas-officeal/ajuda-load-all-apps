# Configurando o ADB no Linux (Ubuntu/Debian)

O ADB é o protocolo de comunicação necessário para o script enviar comandos ao seu dispositivo.

1. **Instalação:**
   No terminal, execute o comando abaixo para instalar as ferramentas de plataforma:
   ```bash
   sudo apt update
   sudo apt install android-tools-adb android-tools-fastboot
  
2. **verificação:**
   execute:
   ```bash
   adb devices
**info:**
   Se a instalação estiver correta, você verá o número de série do seu dispositivo seguido da palavra device.

3. **Solução de problemas comuns:**

    **Permissão negada:** Tente reiniciar o servidor ADB com adb kill-server e depois adb start-server.

    **Dispositivo não listado:** Verifique se o cabo é de boa qualidade (alguns cabos servem apenas para carga, não para dados).

    **Regras de UDEV:** Se o dispositivo não aparecer, pode ser necessário adicionar regras de permissão no Linux (frequentemente não é necessário em distros modernas).
