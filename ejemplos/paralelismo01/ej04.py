import threading
import time
import random

def tareaUno():
  global Done
  time.sleep (random.random())
  if not Done:

    print("Tarea realizada")
    time.sleep(0.12)
    Done = True
  else :
    print ("tarea NO REALIZADA")
    time.sleep(0.05)
  return

Done = False

hilos = list()
for i in range(50):
  t = threading.Thread(target=tareaUno)
  hilos.append(t)
  t.start()
tareaUno()
time.sleep(1)