class Veiculo:
    def __init__(self, nro_rodas= int, motor= float, modelo= str):
        self.nro_rodas = nro_rodas
        self.motor = motor
        self.modelo = modelo

    def dando_partida(self):
        motor = self.motor
        print(f"Motor {float(motor)} está ligando")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"


class DeCarga(Veiculo):
    def __init__(self, qtd_carga= int, carga_livre= 0, **kw):
        super().__init__(**kw)
        self.qtd_carga = qtd_carga
        self.carga_livre = carga_livre

    def iniciando_carregamento(self):
        qtd_carga = self.qtd_carga

        while True:
            try:
                a_colocar = int(input(f"Quanto você deseja carregar? Se lembre, o limite é {qtd_carga}kg's: "))

                if (a_colocar > qtd_carga):
                    raise ValueError
                
            except (ValueError, TypeError):
                print("Insira um valor válido, dentro do limite de carregamento.")
                continue 

            print(f"Veiculo carregado com {a_colocar}kg's")
            self.carga_livre = (qtd_carga - a_colocar)
            return self.carga_livre


class Leve(Veiculo):
    def __init__(self, tipo= str, **kw):
        super().__init__(**kw)
        self.tipo = tipo

    def ganhando_velocidade(self):
        Leve.dando_partida()
        print(f"{self.tipo} está ganhando velocidade")


class Carro(DeCarga):
    ...

class Caminhao(DeCarga):
    ...


class Motocicleta(DeCarga, Leve):
    ...

wolks = Caminhao(nro_rodas= 8, motor= 2.6, modelo="Volvo Scania G3", qtd_carga= 6000)
wolks.iniciando_carregamento()
print(wolks)

bis = Motocicleta(nro_rodas= 2, motor= 0.150, modelo="HGA G3", qtd_carga= 60, tipo= "Bis")
bis.iniciando_carregamento()
print(bis)