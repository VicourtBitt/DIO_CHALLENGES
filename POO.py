class Veiculo:
    def __init__(self, tipo, nome, qtd_rodas, tipo_de_motor):
        self.modelo = tipo
        self.nome = nome
        self.qtd_rodas = qtd_rodas
        self.tipo_de_motor = tipo_de_motor

    def ligar_motor(self):
        print(f"{"A Motocicleta" if self.tipo == "Moto" else "O Carro" if self.tipo == "Carro" else "Caminhão"}\
              está dando a partida.")
        
    def __str__(self):
        return f"{self.__class__.__name__, self.tipo}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"