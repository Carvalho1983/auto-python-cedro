import requests
import timeit
import time

def get_request(endpoint):    
    URL = endpoint   
    PARAMS = ""  
    inicio = time.time()
    r  = requests.get(url = URL, params = PARAMS)
    fim = time.time()
    tempo = fim - inicio
    return tempo

time = get_request("http://10.1.9.163:8080/categorias/1")
print time 