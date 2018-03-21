import numpy as np
import matplotlib.pyplot as plt

#La funcion genera y retorna N numeros aleatorios siguiendo la distribucion discreta de probabilidad P.

def sample_1(N):
	numeros = np.random.random_sample(N)
	
#Retorna el resultado de la funcion 1, con N como parametro.
	return numeros


#La funcion genera y retorna N numeros aleatorios siguiendo la distribucion probabilidad exponencial con Beta= 0.5.
def sample_2(escala, N):
	escala=0.5
	numeros2 = np.random.exponential(escala,N)
	
#Retorna el resultado de la funcion 2, con Escala y N como parametro.
	return numeros2



#La funcion genera y retorna M promedios Sn dada la función de sampleo.
def get_mean(sampling_fun,N,M):
	promedios=[]
	for i in range(N):
		prom=sampling_fun(M)
		promedios.append(prom)

#Retorna el resultado de la funcion 3, con una funcion, N y M como parametros.
	return promedios





