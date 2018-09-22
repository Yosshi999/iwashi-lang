import re
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("python %s filename" % sys.argv[0])
        exit(-1)

    ops = []
    labels = dict()
    f = open(sys.argv[1], "r")
    for i, line in enumerate(f):
        if re.match(r"だれかがハサミで", line):
            ops.append(["GETC"])
        elif re.match(r"タイムラインをちょんぎった", line):
            ops.append(["PUTC"])
        elif re.match(r"そして", line):
            ops.append(["GETN"])
        elif re.match(r"あしたときのうがつながった", line):
            ops.append(["PUTN"])
        elif re.match(r"あしたのことはしっている", line):
            ops.append(["INC"])
        elif re.match(r"^(.+)がつちからはえてくるんだ", line):
            la = re.match(r"^(.+)がつちからはえてくるんだ", line).group(1)
            ops.append(["JGZ", la])
        elif re.match(r"^(.+)にあながあく", line):
            la = re.match(r"^(.+)にあながあく", line).group(1)
            ops.append(["NOP"])
            labels[la] = i
        elif re.match(r"すのこがきえるんだ", line):
            ops.append(["DEC"])
        elif re.match(r"きのうのきおくはきえたけど", line):
            ops.append(["ZERO"])
        elif re.match(r"きえたってこともよくわからないんだ", line):
            ops.append(["EXIT"])
        elif re.match(r"そらのうえから(.+)がたつ", line):
            la = re.match(r"そらのうえから(.+)がたつ", line).group(1)
            ops.append(["JZ", la])
        elif re.match(r"めがみえなくなってきた", line):
            ops.append(["NEG"])
        elif re.match(r"はなはかれず", line):
            ops.append(["ADD"])
        elif re.match(r"とりはとばずねむる", line):
            ops.append(["SUB"])
        elif re.match(r"かぜはとまりつめたく", line):
            ops.append(["MUL"])
        elif re.match(r"つきはみちもかけもせずまわる", line):
            ops.append(["DIV"])
        elif re.match(r"(\d+)ねんまえかのことでした", line):
            result = re.match(r"(\d+)ねんまえかのことでした", line)
            n = int(result.group(1))
            if n < 0 or n > 2018:
                raise NameError('そんな時代は無い at line: %d' % i)
            ops.append(["FOCUS", n])
        elif line == '\n':
            continue
        else:
            raise NameError('そんな命令は無い at line: %d' % i)

    for op in ops:
        if op[0] == 'JZ' or op[0] == 'JGZ':
            op[1] = labels[op[1]]
    #for op in ops:
    #    print(op)
    memory = [0 for i in range(3000)]
    rip = 0
    mem_i = 0
    while True:
        op = ops[rip]
        opcode = op[0]
        if opcode == 'GETC':
            c = sys.stdin.read(1)
            if c == '':
                # fail to read
                memory[mem_i] = -1
            else:
                memory[mem_i] = ord(c)
        elif opcode == 'PUTC':
            print(chr(memory[mem_i]), end='', flush=True)
        elif opcode == 'GETN':
            s = ""
            while True:
                c = sys.stdin.read(1)
                if c == '\n' or c == '':
                    break
                if c == '\r':
                    sys.stdin.read(1)
                    break
                s += c
            memory[mem_i] = int(s)
        elif opcode == 'PUTN':
            print(memory[mem_i], end='', flush=True)
        elif opcode == 'INC':
            memory[mem_i] += 1
        elif opcode == 'JGZ':
            if memory[mem_i] > 0:
                rip = op[1]
        elif opcode == 'NOP':
            pass
        elif opcode == 'DEC':
            memory[mem_i] -= 1
        elif opcode == 'ZERO':
            memory[mem_i] = 0
        elif opcode == 'EXIT':
            exit(0)
        elif opcode == 'JZ':
            if memory[mem_i] == 0:
                rip = op[1]
        elif opcode == 'NEG':
            memory[mem_i] *= -1
        elif opcode == 'ADD':
            memory[mem_i] = memory[mem_i+1] + memory[mem_i+2]
        elif opcode == 'SUB':
            memory[mem_i] = memory[mem_i+1] - memory[mem_i+2]
        elif opcode == 'MUL':
            memory[mem_i] = memory[mem_i+1] * memory[mem_i+2]
        elif opcode == 'DIV':
            memory[mem_i] = memory[mem_i+1] // memory[mem_i+2]
            memory[mem_i+1] = memory[mem_i+1] % memory[mem_i+2]
        elif opcode == 'FOCUS':
            mem_i = op[1]
        else:
            raise NameError('undefined opcode %s' % opcode)
        rip += 1
        if len(ops) <= rip:
            exit(0)




