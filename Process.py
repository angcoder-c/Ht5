import random

CPU_SPEED = 3  # instrucciones / u_tiempo

class Process:
    def __init__(self, env, name, ram, cpu, process_times):
        self.env = env
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.instructions = random.randint(1, 10)
        self.memory_needed = random.randint(1, 10)
        self.process_times = process_times
        self.start_time = env.now
        
        env.process(self.running())
    
    def running(self):
        # Solicitar memoria RAM
        self.state = 'new'
        yield self.ram.get(self.memory_needed)
        self.state = 'ready'
        
        while self.instructions > 0:
            with self.cpu.request() as req:
                yield req  # Esperar turno en el CPU
                self.state = 'running'
                execute_time = min(CPU_SPEED, self.instructions)
                yield self.env.timeout(1)  # Tiempo de procesamiento
                self.instructions -= execute_time
                
                # Simulación de posible espera
                if random.randint(0, 1):
                    self.state = 'waiting'
                    yield self.env.timeout(1)  # Simulación de estado de espera
                    self.state = 'ready'
                else:
                    self.state = 'ready'
        
        # Liberar memoria RAM
        yield self.ram.put(self.memory_needed)
        self.state = 'terminated'
        self.process_times[self.name] = self.env.now - self.start_time
