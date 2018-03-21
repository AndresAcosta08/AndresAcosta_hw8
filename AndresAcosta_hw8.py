import numpy as np
import matplotlib.pyplot as plt

#La funcion genera y retorna N numeros aleatorios siguiendo la distribucion discreta de probabilidad P.

def sample_1(N):
	numeros = np.random.random_sample(N)
	return numeros

#Imprime el resultado de la funcion 1, con N como parametro.
#print sample_1(5)

#La funcion genera y retorna N numeros aleatorios siguiendo la distribucion probabilidad exponencial con Beta= 0.5.
def sample_2(escala, N):
	escala=0.5
	numeros2 = np.random.exponential(escala,N)
	return numeros2

#Imprime el resultado de la funcion 2, con N como parametro.
#print sample_2(0.5,5)

def get_mean(sampling_fun,N,M):
	promedios=[]
	for i in range(N):
		prom=sampling_fun(M)
		promedios.append(prom)

	return promedios

print get_mean(sample_1,5,10000)





