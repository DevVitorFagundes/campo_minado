import random        # para gerar posições aleatórias
import time          # controle do tempo 
import os            # funções de sistema operacional (cls)
from colorama import Fore, Style

jogo    = []
apostas = []
temp    = "🐯🐯🐢🐢🐟🐟🐪🐪🐇🐇🐸🐸🐞🐞🐖🐖"
figuras = list(temp)            
# print(figuras)

nome = input("Nome do Jogador: ")
pontos = 0
# acerto: +10 pontos
# erro: -5 pontos
hora_inicial = time.time()

def preenche_matriz():
  for i in range(4):
    jogo.append([])
    apostas.append([])
    for _ in range(4):
      num = random.randint(0, len(figuras)-1)
      jogo[i].append(figuras[num])
      apostas[i].append("🟥")
      figuras.pop(num)
      # print(jogo)

def mostra_tabuleiro():
  os.system("cls")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {jogo[i][j]} ", end="")
    print("\n")  

  print("Memorize a posição dos bichos...")
  time.sleep(2)

  print("Contagem Regressiva: ", end="")

  for i in range(10, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
  os.system("cls")

def mostra_apostas():
  os.system("cls")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {apostas[i][j]} ", end="")
    print("\n")  
  
def faz_aposta(num_aposta):
  while True:
    mostra_apostas()
    aposta = input(f"{num_aposta}ª Coordenada (2 números: linha e coluna): ")
    if len(aposta) != 2:
      print("Informe uma dezena como coordenada, por exemplo: 13, 21, 32, 44")
      time.sleep(2)
      continue
    x = int(aposta[0])-1
    y = int(aposta[1])-1
    try:
      if apostas[x][y] == "🟥":
        apostas[x][y] = jogo[x][y]
        break
      else:
        print("Já apostado... escolha outra coordenada")
        time.sleep(2)
    except IndexError:
      print("Posição inválida... repita")
      time.sleep(2)
  return (x, y)    

def verifica_tabuleiro():
  faltam = 0
  for i in range(4):
    for j in range(4):
      if apostas[i][j] == "🟥":
        faltam += 1
  return faltam

preenche_matriz()
mostra_tabuleiro()

while True:
  x1, y1 = faz_aposta(1)
  x2, y2 = faz_aposta(2)

  mostra_apostas()

  if apostas[x1][y1] == apostas[x2][y2]:
    print("Parabéns! Acertou")
    pontos += 10
    if verifica_tabuleiro() == 0:
      print("Que show! Você venceu! Parabéns! 🏆🥇")
      break
    time.sleep(2)
  else:
    print("Bah... Você errou")
    pontos -= 5
    apostas[x1][y1] = "🟥"
    apostas[x2][y2] = "🟥"
    sair = input("Desistir (S/N): ").upper()
    if sair == "S":
      break

hora_final = time.time()
duracao = hora_final-hora_inicial
print(f"{nome} - Você fez um total de {pontos} pontos!")
print(f"Tempo: {duracao:.3f} segundos") 

if os.path.isfile("ranking.txt"):
  with open("ranking.txt", "r") as arq:
    dados = arq.readlines()
else:
  dados = []

jogadores = []
pontuacoes = []
tempos = []

for linha in dados:
  partes = linha.split(";")
  jogadores.append(partes[0])
  pontuacoes.append(int(partes[1]))
  tempos.append(float(partes[2]))

jogadores.append(nome)
pontuacoes.append(pontos)
tempos.append(duracao)

juntas = sorted(zip(pontuacoes, tempos, jogadores), reverse=True)
pontuacoes2, tempos2, jogadores2 = zip(*juntas)

print("\nNº Nome do Jogador...: Pontos Tempo......:")
print("------------------------------------------")

posicao = 0
with open("ranking.txt", "w") as arq:
  for jogador, pontuacao, tempo in zip(jogadores2, pontuacoes2, tempos2):
    arq.write(f"{jogador};{pontuacao};{tempo:.3f}\n")
    posicao += 1
    if jogador == nome:
      print(Fore.RED + f"{posicao:2d} {jogador:20s}  {pontuacao:4d}  {tempo:7.3f} seg")
      print(Style.RESET_ALL, end="")      
    else:
      print(f"{posicao:2d} {jogador:20s}  {pontuacao:4d}  {tempo:7.3f} seg")