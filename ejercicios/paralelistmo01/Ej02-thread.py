import threading
import time


def escribeY():
  for i in range(100):
    print (".", end="",flush=False)
    time.sleep(1)
  return

print ("INICIO")
t = threading.Thread(target=escribeY)
t.start()

for i in range(50):
  print ("-", end="",flush=False)
  time.sleep(2)