from textwrap import wrap

nums = {
    "օо": 0,
    "օo": 1,
    "օօ": 2,
    "օο": 3,
    "οо": 4,
    "οo": 5,
    "οօ": 6,
    "οο": 7
}

chars = ['о', 'o', 'օ', 'ο']

def parse(path):
    with open(path, 'r', encoding="utf-8") as file:
        prog = file.read()
        prog_clag = ''
        for char in prog:
            if char in chars:
                prog_clag+= char

    cmnds = wrap(prog_clag, 2)
    return cmnds

def execute(cmnds):
    array = [0]
    cmnd = 0
    index = 0
    loop = []
    while cmnd < len(cmnds):

        if cmnds[cmnd] == 'оо':
            index += 1
            if index == len(array):
                array.append(0)

        elif cmnds[cmnd] == 'оo':
            index -= 1
            if index < 0:
                index += 1
                array.insert(0, 0)

        elif cmnds[cmnd] == 'оօ':
            pwr = 0
            n = int('0', base=8)
            while cmnd+pwr+1 < len(cmnds) and cmnds[cmnd+pwr+1] in nums:
                n *= 8
                n += nums[cmnds[cmnd+pwr+1]]
                pwr += 1
            array[index] += n
            cmnd += pwr

        elif cmnds[cmnd] == 'оο':
            pwr = 0
            n = int('0', base=8)
            while cmnd+pwr+1 < len(cmnds) and cmnds[cmnd+pwr+1] in nums:
                n *= 8
                n += nums[cmnds[cmnd+pwr+1]]
                pwr += 1
            array[index] -= n
            cmnd += pwr

        elif cmnds[cmnd] == 'oо':
            print(chr(array[index]), end='')

        elif cmnds[cmnd] == 'oo':
            array[index] = ord(input('\n> '))

        elif cmnds[cmnd] == 'oօ':
            if array[index] != 0:
                loop.append(cmnd)
            else:
                x=1
                while cmnds[cmnd+x] != 'oο':
                    x+=1
                cmnd += x
                
        elif cmnds[cmnd] == 'oο':
            cmnd = loop[-1] - 1
            loop.pop()

        cmnd += 1

def run(path):
    prog = parse(path)
    execute(prog)
    
        
