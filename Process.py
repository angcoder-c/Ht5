import random

# configuración de numeros aleatorios
random.seed(10)
CPU_SPEED = 3  # instrucciones / u_tiempo

class Process:
    def __init__(self, env, name, ram, cpu, process_times):
        self.env = env
        self.name = name

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

        env.process(self.new())
    
    def new(self):
        # obtener memoria
        yield self.ram.get(self.memory_needed)
        self.env.process(self.ready())
    
    def ready(self):
        # si hay instrucciones, se obtienen los 
        # recursos y se ejecuta la instrucción
        while self.instructions > 0:
            with self.cpu.request() as req:
                yield req
                self.env.process(self.running())
                return
    
    def running(self):
        # ejecutar el nnumero de instrucciones 
        # maximo por unidad de tiempo
        execute_time = CPU_SPEED
        if (self.instructions<CPU_SPEED):
            execute_time=self.instructions

        # 1 u_tiempo
        yield self.env.timeout(1)
        self.instructions -= execute_time

        if self.instructions > 0:
            yield self.env.process(self.ready())
        else:
            yield self.env.process(self.terminated())
    
    def terminated(self):
        # liberar ram
        yield self.ram.put(self.memory_needed)
        self.process_times[self.name]=self.env.now-self.start_time