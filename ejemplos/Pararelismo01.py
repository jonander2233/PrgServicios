import threading

def escribeY():
  for i in range(1000):
    print ("y", end="",flush=True)
  return

print ("INICIO")
t = threading.Thread(target=escribeY)
t.start()

for i in range(1000):
  print ("X", end="",flush=True)
