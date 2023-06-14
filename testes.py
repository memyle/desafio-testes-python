import subprocess
with open("entradasteste.txt", "r",encoding="utf-8") as test:
    contador = 0
    for linha in test.readlines():
        contador+=1
        print ("\nCenário " + str(contador))
        print ("Comando: " + str(linha))
        subprocess.run(linha, shell=True)