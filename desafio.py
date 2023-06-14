import sys
import os

def create_file():
    with open("arquivo.txt", "w") as file:
        file.write("[Os números abaixo serao multiplicados pelo valor repassado via parâmetro -d:]\n")
        for i in range(10):
            file.write(str(i) + "\n")
    print("Arquivo criado com sucesso!")

def clear_file():
    if os.path.exists("arquivo.txt"):
        os.remove("arquivo.txt")
        print("Arquivo removido com sucesso!")
    else:
        print("O arquivo não existe.")

def update_file(parametro):
    with open("arquivo.txt", "w") as file:
        file.seek(0)
        file.write("[Os números abaixo serao multiplicados pelo valor repassado via parâmetro -d:]\n")
        for i in range (10):
            resultado = i * int(parametro)
            file.write(str(i) + ' x ' + str(parametro) + ' = ' + str(resultado) + "\n")
    print("Arquivo atualizado com sucesso!")       
 
def update_text(parametro):
    with open("arquivo.txt", "r" ) as file:
        lines = file.readlines()
        lines[0] = parametro + '\n'
    with open("arquivo.txt", "w" ) as file:
        file.seek(0)
        file.writelines(lines)
        print("Texto atualizado com sucesso!")
        
def main():
    if len(sys.argv) < 2:
        print("Uso: desafio.py [opção] [parâmetro]")
        return
    option = sys.argv[1]
    if option == "-l":
        create_file()
    elif option == "-d":
        if len(sys.argv) < 3:
            print("Você precisa fornecer um parâmetro para a opção -d.")
            return
        if len(sys.argv) > 3:
            print("Uso: desafio.py [opção] [parâmetro]")
            return
        update_file(sys.argv[2])
    elif option == "-t":
        if len(sys.argv) > 3:
            print("Texto precisa estar entre aspas para ser alterado.")
            return
        if len(sys.argv) < 3:
            print("Você precisa fornecer um parâmetro para a opção -t.")
            return
        update_text(sys.argv[2])
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()