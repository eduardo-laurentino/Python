import serial

arduino = serial.Serial("/dev/ttyACM0", 9600)
while True:
    linha = str(arduino.readline())
    linha_teste = linha[2:-15]
    print(linha_teste, "°C")
arduino.close()                     