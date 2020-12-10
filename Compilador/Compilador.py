arquivo = open("CodigoBin.drs", "w")

cabecalho = """#------------------------------------------------------------
#- Deeds (Digital Electronics Education and Design Suite)
#- Rom Contents Saved on (10/12/2020, 09:08:13)
#-      by Deeds (Digital Circuit Simulator)(Deeds-DcS)
#-      Ver. 2.30.041 (March 3, 2020)
#- Copyright (c) 2002-2020 University of Genoa, Italy
#-      Web Site:  https://www.digitalelectronicsdeeds.com
#------------------------------------------------------------
#R ROM256x16, id 0006
#- Deeds Rom Source Format (*.drs)

#A 0000h
#B

"""
nums='1111.1111.1111.1111 1111.1111.1111.1111 \n'*127

lines = []

print("""
Utilização:
            addi Ra Rb Imm
            subi Ra Rb Imm 
            jleu Ra Rb Imm
            jles Ra Rb Imm 
            
            Obs: não é case sensitive, use numeros para indicar os registradores
            indo de 0 a 7 e digite em decimal.
            Digite dê enter em uma linha vazia para finalizar o código.
            
            Arquivo gerado: CodigoBin.drs""")

while True:
    entrada = input()
    if entrada == '':
        arquivo.write(cabecalho)
        nums = nums.split()
        for i in range(len(lines)):
            nums[i]=lines[i]
        nums = [f"{i} {j}\n" for i, j in list(zip(nums, nums[1:]))[::2]]
        arquivo.writelines(nums)
        arquivo.close()
        break
    e = entrada.split()
    if e[0].lower() == 'addi':
        string = f"{int(e[3]):08b}"
        string += f"{int(e[2]):03b}"
        string += f"{int(e[1]):03b}"
        string += f"00"
        string = string[:4] + '.' + string[4:8] + '.' + string[8:12] + '.' + string[12:]
        lines.append(string)
    if e[0].lower() == 'subi':
        string = f"{int(e[3]):08b}"
        string += f"{int(e[2]):03b}"
        string += f"{int(e[1]):03b}"
        string += f"01"
        string = string[:4] + '.' + string[4:8] + '.' + string[8:12] + '.' + string[12:]
        lines.append(string)
    if e[0].lower() == 'jleu':
        string = f"{int(e[3]):08b}"
        string += f"{int(e[2]):03b}"
        string += f"{int(e[1]):03b}"
        string += f"10"
        string = string[:4] + '.' + string[4:8] + '.' + string[8:12] + '.' + string[12:]
        lines.append(string)
    if e[0].lower() == 'jles':
        string = f"{int(e[3]):08b}"
        string += f"{int(e[2]):03b}"
        string += f"{int(e[1]):03b}"
        string += f"11"
        string = string[:4] + '.' + string[4:8] + '.' + string[8:12] + '.' + string[12:]
        lines.append(string)
