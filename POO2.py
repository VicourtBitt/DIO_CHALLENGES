class Bicicletas:
    def __init__(self, modelo=str, cor=str, ano=int, valor=float, movement= False):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.movement = movement
    
    def _buzinar(self):
        print(f"A bibicleta {self.modelo} buzinou.")
    
    def _andar(self):
        if self.movement:
            print(f"A bicicleta {self.modelo} já está em movimento.")
        else:
            self.movement = True
            print(f"{self.modelo} começando a se mexer")

    def _parar(self):
        if not self.movement:
            print(f"A bicicleta {self.modelo} já está parada. ")
        else:
            print(f"{self.modelo} já está parando.")

    def _citar_info(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicletas(modelo="Cross X3", cor="Vermelho/Branco", ano=2013, valor=4399.99)
print(b1._citar_info())
print('\n')
b1._parar()
b1._andar()
b1._buzinar()
b1._parar()
 