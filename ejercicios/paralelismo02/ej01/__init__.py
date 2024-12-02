from ejercicios.paralelismo02.ej01.ej01 import MiScraping

hilo = MiScraping("http://localhost/mi_web")
hilo.start()
hilo.join()
links = hilo.get_links()
print(links)