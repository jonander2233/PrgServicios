import threading

# mét-odo al que se va a aosciar el hilo
def SaludoHilo2():
  print ('soy el hilo 2\n')
  t3.start()

def SaludoHilo3():
  print ('hola, soy el hilo 3\n')

# creamos un hilo asociado a una función
t3 = threading.Thread(target=SaludoHilo3)
t2 = threading.Thread(target=SaludoHilo2)
#
t2.start()
print ("hola, soy el hilo 1 y primero \n") #impresión en el hilo principal