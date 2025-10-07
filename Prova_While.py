salario = float(input("Digite seu salario: "))
meses = int(input("Digite quantos meses voce trabalhou: "))
ferias = ""
while meses < 12:
  ferias = (salario/12) * meses
  print(f"Ferias proporcionais de {ferias:.2f}")
  break