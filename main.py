'''
Hoja de trabajo 5
Fecha 24/02/2025
'''
import random

from sim import simulation

if __name__ == "__main__":
    random.seed(10)
    casos = [25, 50, 100, 150, 200]
    intervalos = [10, 5, 1]
    
    for intervalo in intervalos:
        print(f"\nIntervalo de llegada: {intervalo}")
        for caso in casos:
            print(simulation(caso, intervalo))
            promedio, desviacion = simulation(caso, intervalo)
            print(f"Procesos: {caso} -> Tiempo promedio: {promedio:.2f}, Desviación estándar: {desviacion:.2f}")
