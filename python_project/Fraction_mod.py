class Fraction:
  def main():
    # Caminho Feliz
f1 = Fracao(1, 5)
print(f1.numerador) # 1
print(f1.numerador == 1)
print(f1.denominador) # 5
print(f1.denominador == 5)
f2 =  Fracao(1, 5)
print(f2.numerador == 1)
print(f2.denominador == 5)
f2.mais(2, 5) # +2/5
print(f2.numerador == 3)
print(f2.denominador == 5)
f2.mais(f1.numerador, f2.denominador)
print(f2.numerador == 4)
print(f2.denominador == 5)
f3 =  Fracao(3, 7)
print(f3.numerador == 3)
print(f3.denominador == 7)
f3.mais(f2.numerador, f2.denominador)
print(f3.numerador == 43)
print(f3.denominador == 35)
# Começando com as alternativas
f4 =  Fracao(6) # denominador padrão 1
print(f4.numerador == 6)
print(f4.denominador == 1)
f5 =  Fracao() # numerador padrão 0
print(f5.numerador == 0)
print(f5.denominador == 1)
# Fração inválida
# denominador 0 deve lançar IllegalArgumentException
#f6 =  Fracao(2, 0) # deve quebrar aqui
#print(f6.denominador == 0) # não deve chegar aqui
# comente as linhas após fazer quebrar
# Operações não suportadas
# não lidaremos com frações negativas
# deve lançar UnsupportedOperationException
#f7 =  Fracao(2, -5)
#f8 =  Fracao(-2, 5)
#f9 =  Fracao(-2, -5)
# comente as linhas após fazer quebrar
# desafio: especificar e implementar as outras operações (opcional)

