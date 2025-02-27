import random

# configuración de numeros aleatorios
random.seed(10)
CPU_SPEED = 3  # instrucciones / u_tiempo

class Process:
    def __init__(self, env, name, ram, cpu, process_times):
        self.env = env
        self.name = name
        self.state = 'now'

        # cola
        self.ram = ram

        # cpu, 1 por defecto
        self.cpu = cpu

        # cantidad de instrucciones del proceso
        self.instructions = random.randint(1, 10)

        # memoria que requiere el proceso
        self.memory_needed = random.randint(1, 10)
        self.process_times = process_times
        self.start_time = env.now

        env.process(self.running())
    
    def running(self):
        # obtener memoria
        self.state = 'new'
        yield self.ram.get(self.memory_needed)
                
        self.state = 'ready'
        with self.cpu.request() as req:
            yield req
        

        # ejecutar el nnumero de instrucciones 
        # maximo por unidad de tiempo
        execute_time = CPU_SPEED
        if (self.instructions<CPU_SPEED):
            execute_time=self.instructions

        while self.instructions > 0:
            # 1 u_tiempo
            self.state = 'running'
            yield self.env.timeout(1)
            self.instructions -= execute_time

            if random.randint(0, 1):
                self.state = 'waitting'
                yield self.env.timeout(1)
                self.state = 'ready'
            else:
                self.state = 'ready'

        # liberar ram
        yield self.ram.put(self.memory_needed)
        self.state = 'terminated'
        self.process_times[self.name]=self.env.now-self.start_time