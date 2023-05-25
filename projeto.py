from time import sleep
tempo_em_segundos = 10

print("A senha deve conter 6 digitos")

while True:
    cad_senha = int(input("Insira a senha do seu celular:"))

    if cad_senha > 999999:
        print("A senha só pode conter 6 digitos!!")

    elif cad_senha < 99999:
        print("A senha deve conter 6 digitos")

    else :         
        break
print("A senha foi cadastrada")
print("Em caso de errar sua senha você tera 3 tentativas")
tentativa = 1

for i in range(0,3,tentativa):
    senha = int(input("Insira sua senha:"))

    if senha != cad_senha:
        print(f"Senha Incorreta\n Essa foi sua {tentativa}º tentativa")
        sleep(3.0)
        tentativa+=1
    else:
        print("Bem vindo!")
        break

if tentativa > 3: 
    print("celular bloqueado por excesso de tentativas !")                                                         