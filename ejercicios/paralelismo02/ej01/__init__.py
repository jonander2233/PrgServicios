from ejercicios.paralelismo02.ej01.ej01 import MiScraping

hilo = MiScraping("http://localhost:8000/portada.html")
hilo.start()
hilo.join()
links = hilo.get_links()
print(links)