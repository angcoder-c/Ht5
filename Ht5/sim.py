import simpy
import random
import Process
import statistics

from Process import Process

def simulation(procesos, intervalo):
    env = simpy.Environment()
    ram = simpy.Container(env, init=100, capacity=100)
    cpu = simpy.Resource(env, capacity=1)
    process_times = {}
    
    def generate_processes():
        for i in range(procesos):
            yield env.timeout(random.expovariate(1 / intervalo))
            Process(env, f'Proceso {i}', ram, cpu, process_times)
    
    env.process(generate_processes())
    env.run()
    
    tiempos = list(process_times.values())
    promedio = statistics.mean(tiempos) if tiempos else 0
    desviacion = statistics.stdev(tiempos) if len(tiempos) > 1 else 0
    return promedio, desviacion