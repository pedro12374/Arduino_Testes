import serial
import time
porta = '/dev/ttyUSB0' #qual a porta USB conectada

ser = serial.Serial(porta, 9600, timeout = 1) #ser recebe os dados vindo da porta, a uma taxa de 9600 bits por segundo

data = open('Data.txt', 'w') #Abre o arquivo 'Data.txt' para escrever nele

#Loop para escrever os dados no arquivo 'Data.txt'
try:
    while True: #Enquanto verdadeiro a variavel txt recebe os dados de cada linha da saida serial do arduino e escreve no arquivo 'Data.txt'
        hora = time.strftime("%H:%M:%S")
        txt = ser.readline()
        data.write(hora + ' ' + txt)
        print(hora + ' ' + txt)
        time.sleep(2)
except KeyboardInterrupt: #Quando ctrl+c e precionado o programa para
    data.close()#Fecha o arquivo 'Data.txt' com os novos dados
    print('FIM')#Encerra tudo, todos os comandos devem vir a cima deste
