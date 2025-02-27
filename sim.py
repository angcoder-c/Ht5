import simpy
import random
import Process

def simulation(procesos, intervalo):
    env = simpy.Environment()
    ram = simpy.Container(env, init=100, capacity=100)
    cpu = simpy.Resource(env, capacity=1)
    process_times = {}
    
    for i in range(procesos):
        # nuevo proceso
        Process.Process(env, f'proceso {i}', ram, cpu, process_times)

        # procesos en intervalos de x
        send_interval = random.expovariate(1 / intervalo)
        env.timeout(send_interval)

    env.run()
    return (process_times, sum(process_times.values()))