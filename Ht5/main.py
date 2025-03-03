'''
Hoja de trabajo 5
Fecha 24/02/2025
'''
import random
import matplotlib.pyplot as plt
from sim import simulation

if __name__ == "__main__":
    random.seed(10)
    casos = [25, 50, 100, 150, 200]
    intervalos = [10, 5, 1]
    
    resultados_a = {}
    resultados_b = {}
    
    intervalo_a = 10
    tiempos_promedio_a = []
    desviaciones_a = []
    print(f"\n[Inciso A] Intervalo de llegada: {intervalo_a}")
    for caso in casos:
        promedio, desviacion = simulation(caso, intervalo_a)
        print(f"Procesos: {caso} -> Tiempo promedio: {promedio:.2f}, Desviación estándar: {desviacion:.2f}")
        tiempos_promedio_a.append(promedio)
        desviaciones_a.append(desviacion)
    resultados_a[intervalo_a] = (casos, tiempos_promedio_a, desviaciones_a)

    # Graficar Inciso A
    plt.figure(figsize=(10, 6))
    plt.plot(casos, tiempos_promedio_a, marker='o', linestyle='-', label=f'Intervalo {intervalo_a}')
    plt.xlabel('Número de procesos')
    plt.ylabel('Tiempo promedio en la computadora')
    plt.title('Inciso A: Tiempo promedio vs Número de procesos')
    plt.legend()
    plt.grid()
    plt.show()