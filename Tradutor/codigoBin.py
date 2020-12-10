arquivo = str(input())

with open(arquivo) as f:
    lines = f.readlines()
    lines = [i for j in [str(x[:-1]).split() for x in lines if x[0] != '#' and x != ''] for i in j]

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val


string = []
for i in range(len(lines)):
    entrada = lines[i]
    if entrada == '1111.1111.1111.1111':
        break
    entrada = entrada.replace(" ","")
    entrada = entrada.replace(".","")
    # 00001001 001 001 00

    imm = entrada[:8]
    rb = entrada[8:11]
    ra = entrada[11:14]
    op = entrada[14:]
    imm_2 = twos_comp(int(imm,2),len(imm))
    if op == '00':
        string.append(f'R{int(ra,2)}+=R{int(ra,2)} + R{int(rb,2)} + {imm}')
    elif op == '01':
        string.append(f'R{int(ra,2)}-=R{int(ra,2)} - R{int(rb,2)} - {imm}')
    elif op == '10':
        string.append(f'jleu R{int(ra,2)}<=R{int(rb,2)}, pc+={imm_2}')
    else:
        string.append(f'jles R{int(ra,2)}<=R{int(rb,2)}, pc+={imm_2}')

for i in string:
    print(i)
