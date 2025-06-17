print('FAZENDO A CONEXÃO COM O ARDUÍNO')
print('-'*35)
print()

import serial
from pathlib import Path

# Fazendo a conexão com o Arduíno
inicio = True
while inicio:
    try:
        arduino = serial.Serial('COM3', 9600)
        print('Arduino conectado')
        break
    except:
        fim = input('Deseja continuar novamente? [s/n] ')
        if fim == 'n':
            inicio = False

# Salvando os dados coletados em um arquivo txt
myfile = Path(r'Dados Arduíno.txt')
myfile.touch(exist_ok=True)
f = open(r'Dados Arduíno.txt', 'w')

# Mostrando os dados coletados
while True:
    try:
        msg = str(arduino.readline())
        msg = msg[2:-5] 
        print(msg)
        f.write('\n{msg}\n')
        arduino.flush()
    except:
        print('\nErro de comunicação')
        break
    