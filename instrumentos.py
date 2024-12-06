class Instrumentos:
    def __init__(self, violino, viola, cello):
        self._violino = violino
        self._viola = viola
        self._cello = cello
        
    def set_violino(self, violino):
        self._violino = print("Violino")
    def set_viola(self, viola):
        self._viola = print("Viola")
    def set_cello(self, cello):
        self._cello = print("Cello")
        
    def get_violino(self):
        return self._violino
    def get_viola(self):
        return self._viola
    def get_cello(self):
        return self._cello
        
    def mostrar(self):
        print(f"{self.get_violino()} {self.get_viola()} {self.get_cello()}")
    
'''
TESTE    
i = Instrumentos("Violino", "Viola", "Cello")
i.mostrar()
'''
        