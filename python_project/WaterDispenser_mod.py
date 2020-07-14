# Py CODE onde está chamando o lugar que o objeto esta definido?
class WaterDispenser:
def main():
  maq = MaquinaAgua()
  print(maq.agua() == 0) # mL
  print(maq.copos200() == 0)
  print(maq.copos300() == 0)
  maq.servirCopo200() # não efetua
  print(maq.agua() == 0) # mL
  print(maq.copos200() == 0)
  print(maq.copos300() == 0)
  maq.abastecerAgua() # inicializa 20000mL
  print(maq.agua() == 20000) # mL
  maq.abastecerAgua() # mantém consistente
  print(maq.agua() == 20000) # mL
  maq.servirCopo200() # não efetua, sem copo
  print(maq.agua() == 20000) # mL
  maq.abastecerCopo200() # agora a máquina possui 100 copos de 200
  print(maq.copos200() == 100)
  # correção (A.K.A. PATCH!) =====================================
  maq.servirCopo200()
  maq.servirCopo200()
  maq.servirCopo200()
  maq.servirCopo200()
  maq.servirCopo200() # -1000ml e 5 copos de 200
  print(maq.agua() == 19000)
  print(maq.copos200() == 95)
  print(maq.copos300() == 0)
  maq.abastecerCopo200() # agora a máquina possui 100 copos de 200 novamente
  print(maq.copos200() == 100)
  maq.servirCopo200() # -200ml e 1 copo de 200
  # fim correção =====================================
  print(maq.agua() == 18800)
  print(maq.copos200() == 99)
  print(maq.copos300() == 0)
  maq.abastecerCopo300() # agora a máquina possui 100 copos de 300
  print(maq.copos300() == 100)
  maq.servirCopo300()
  print(maq.agua() == 18500)
  print(maq.copos200() == 99)
  print(maq.copos300() == 99)
  # servir 50 copos de 300 = 15000ml
  for i in range(0,50):
     maq.servirCopo300()
  print(maq.agua() == 3500)
  print(maq.copos200() == 99)
  print(maq.copos300() == 49)
  # servir 17 copos de 200 = 3400ml
  for i in range(0,17):
      maq.servirCopo200()
  print(maq.agua() == 100)
  print(maq.copos200() == 82)
  print(maq.copos300() == 49)
  # não há água para atender o pedido
  maq.servirCopo300()
  print(maq.agua() == 100)
  print(maq.copos200() == 82)
  print(maq.copos300() == 49)
  # não há água para atender o pedido
  maq.servirCopo200()
  print(maq.agua() == 100)
  print(maq.copos200() == 82)
  print(maq.copos300() == 49)
  maq.abastecerAgua() # inicializa 20000mL
  print(maq.agua() == 20000)
  print(maq.copos200() == 82)
  print(maq.copos300() == 49)
  # servir os 49 copos de 300 restantes = 14700ml
  while (maq.copos300() > 0):
      maq.servirCopo300()
  print(maq.agua() == 5300)
  print(maq.copos200() == 82)
  print(maq.copos300() == 0)
  # não há copo para atender o pedido
  maq.servirCopo300()
  print(maq.agua() == 5300)
  print(maq.copos200() == 82)
  print(maq.copos300() == 0)
  maq.servirCopo200() # de 200 ok
  maq.servirCopo200() # de 200 ok
  print(maq.agua() == 4900)
  print(maq.copos200() == 80)
  print(maq.copos300() == 0)
  maq.abastecerCopo300() # 100 copos de 300
  print(maq.agua() == 4900)
  print(maq.copos200() == 80)
  print(maq.copos300() == 100)
  # 3 copos de 300
  maq.servirCopo300() maq.servirCopo300() maq.servirCopo300()
  print(maq.agua() == 4000)
  print(maq.copos200() == 80)
  print(maq.copos300() == 97)

