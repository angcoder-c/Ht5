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
    
    # Inciso A: Intervalo de llegada = 10
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
    
    # Inciso B: Intervalos de 5 y 1
    for intervalo in [5, 1]:
        tiempos_promedio_b = []
        desviaciones_b = []
        print(f"\n[Inciso B] Intervalo de llegada: {intervalo}")
        for caso in casos:
            promedio, desviacion = simulation(caso, intervalo)
            print(f"Procesos: {caso} -> Tiempo promedio: {promedio:.2f}, Desviación estándar: {desviacion:.2f}")
            tiempos_promedio_b.append(promedio)
            desviaciones_b.append(desviacion)
        resultados_b[intervalo] = (casos, tiempos_promedio_b, desviaciones_b)
        
        # Graficas inciso b
        plt.figure(figsize=(10, 6))
        plt.plot(casos, tiempos_promedio_b, marker='o', linestyle='-', label=f'Intervalo {intervalo}')
        plt.xlabel('Número de procesos')
        plt.ylabel('Tiempo promedio en la computadora')
        plt.title(f'Inciso B: Tiempo promedio vs Número de procesos (Intervalo {intervalo})')
        plt.legend()
        plt.grid()
        plt.show()
