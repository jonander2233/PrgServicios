import threading
def Saludo():
    print ("hola,soy el hilo\n")

t = threading.Thread(target=Saludo)

t.start()
print("Hola soy el hilo principal")