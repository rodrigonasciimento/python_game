import random as rd

# Personagem: classe mãe
# Héroi: controlado pelo usuário
# Inimigo adversário do usuário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def atacar(self, alvo):
        dano = rd.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.__habilidade}\n"

    def ataque_especial(self, alvo):
        dano = rd.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial e causou {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.__tipo}"

class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self):
        self.heroi = Heroi(nome="Batman", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Coringa", vida=100, nivel=4, tipo="Doido")
    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando Batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens: ")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar....")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida. Escolha Novamente!")

            if self.inimigo.get_vida() > 0:
                #Inimigo ataca heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Parabéns, você venceu a batalha!")
        else:
            print("Você foi derrotado!")

#Criando instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()