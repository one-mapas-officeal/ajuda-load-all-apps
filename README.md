# System-Android Bridge Monitor

Este projeto monitora o uso de CPU e RAM do seu computador (Linux/Ubuntu) e dispara comandos automáticos para um dispositivo Android conectado via **ADB (Android Debug Bridge)**.

## Funcionalidades
- **Detecção Automática:** Calcula o total de RAM do sistema e define limites de alerta dinamicamente.
- **Monitoramento em Tempo Real:** Verifica CPU e RAM a cada 2 segundos.
- **Automação via ADB:** Permite integrar ações automáticas no Android (como toques, navegação ou controle de hardware) sem intervenção manual.

## Requisitos
- Python 3.x
- `psutil` (instale com `sudo apt install python3-psutil`)
- ADB instalado e configurado no PATH.
- Dispositivo Android com "Depuração USB" ativa.

## Como usar
1. baixe o codigo clicando em 'code' e depois em 'download ZIP'
2. descopilhe a pasta
3. inicie o app com python3 helper.py
4. Conecte o dispositivo via cabo USB.
ALERTE:mais antes siga as outras intruções em outras abas
## Licença
Este projeto é distribuído sob a licença MIT.
