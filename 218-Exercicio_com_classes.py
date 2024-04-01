# Exercicio com classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Motor (nome)
# 3 - Crie uma classe Fabricante (nome)
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante 
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricantes na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None


    def declarando_motor(self, motor):
        self.motor = motor


    def declarando_fabricante(self, fabricante):
        self.fabricante = fabricante


    def imprime_informacoes(self):
        try:
            if self.motor is None:
                print(f'O carro {self.nome} deve ter um motor declarado.')
            elif self.fabricante is None:
                print(f'O carro {self.nome} deve ter um fabricante declarado.')
            else:
                print(f'Carro: {self.nome}, Fabricante: {self.fabricante.nome}, Motor: {self.motor.nome}')
        except Exception as e:
            print(e)

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


mustang = Carro('Mustang')
camaro = Carro('Camaro')
corolla = Carro('Corolla')

ford = Fabricante('Ford')
chevrolet = Fabricante('Chevrolet')
toyota = Fabricante('Toyota')

v6 = Motor('V6')
v8 = Motor('V8')
i4 = Motor('i4')

mustang.declarando_motor(v6)
mustang.declarando_fabricante(ford)
mustang.imprime_informacoes()

camaro.imprime_informacoes()