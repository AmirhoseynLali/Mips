import os

while True:
    path = input('ادرس دقیق فایل را وارد کنید :')  # 'C:\CodeBlocks\karsi.txt'   test    "C:\CodeBlocks\karsi.txt"
    if path[0] == '"' and path[-1] == '"':
        path = path.replace('"', ' ')
        path = path.strip()
        break


def fix_memory(case, case2, case3):  # کیس 1 خود حافظه است و کیس دو مفدار عددی است که قرار به حافظه داده شه و کیس سه دستور
    # پیدا کردن مقدار حافظه یا دستور عوض کردن مقدار ان است
    if case3 == 'find':
        prov = False
        save = int()
        for i2 in memory_R:
            if case == i2:
                prov = True
                print(i2)
                save = memory_R[i2]
                break
        if not prov:
            print('memory cant be found ERROR')
            exit()
        elif prov:
            return save
    elif case3 == 'update':
        if case.find('array') != -1:
            case = case.replace('array', " ")
            case = case.strip()
            for i3 in memory_R:
                if case.find(i3) != -1:
                    memory_R[i3] = {}
                    break
        else:
            for i3 in memory_R:
                if case.find(i3) != -1:

                    memory_R[i3] = case2
                    break


def set_array(value):
    value = value.split(',')
    for i_1 in memory_R:
        if i_1.find(str(value[0])) != -1:

            if type(memory_R[i_1]) == dict:
                memory_R[i_1].update({str(value[1]): int(value[2])})


try:
    with open(os.path.join(path), encoding='utf8') as f:
        book = f.readlines()
        f.close()

except FileNotFoundError:
    print('فایل پیدا نشد دوباره تلاش کنید')  #  ***************تا به اینجا فایل رو باز کردیم و اماده است*************************

back_point = {}  # نقاط بازگشتی
memory_R = {'$s0': 0, '$s1': 0, '$s2': 0, '$s3': 0, '$zero': 0, '$t0': 0, '$t1': 0, '$t2': 0}
len_book = 0
first_page = 0


for i in book:  # ساخت نقاط بازگشتی
    if str(i).find('end_set') != -1:
        first_page = (len_book + 1)
    if first_page == 0:
        test = str(i)
        if test.find('array') != -1:
            fix_memory(test, 0, 'update')
        if test.find('=') != -1:
            test = test.split('=')
            fix_memory(test[0], int(test[1]), 'update')
        elif test.find(',') != -1:
            set_array(test)

    if str(i).find(':') != -1:
        test = i.find(':')
        test = i[:test]
        back_point.update({test: len_book})
    len_book += 1

# print(memory_R)
# print(len_book, '    and    ', first_page)

memory_e = 0
memory_m1 = 0
memory_m2 = 0



def add(line):
    line = line.replace('add', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    c = fix_memory(c, 0, 'find')
    value = int(b) + int(c)
    fix_memory(a, value, 'update')


def addi(line):
    line = line.replace('addi', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    value = int(b) + int(c)
    fix_memory(a, value, 'update')


def sub(line):
    line = line.replace('sub', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    c = fix_memory(c, 0, 'find')
    value = int(b) - int(c)
    fix_memory(a, value, 'update')


def lw(line):
    line = line.replace('lw', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    b = b.replace('(', ',')
    b = b.split(',')
    c = str(b[0])
    b = b[1]
    b = b.replace(")", " ")
    b = b.strip()
    value = memory_R[b][c]
    print(value)
    fix_memory(a, value, 'update')


def sw(line):
    line = line.replace('sw', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    a = fix_memory(a, 0, 'find')
    b = line[1]
    b = b.replace('(', ',')
    b = b.split(',')
    c = str(b[0])
    b = b[1]
    b = b.replace(")", " ")
    b = b.strip()
    memory_R[b][c] = a


def sll(line):
    line = line.replace('sll', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    value = int(b) * (int(c) * 2)
    fix_memory(a, value, 'update')


def srl(line):
    line = line.replace('srl', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    value = int(b) / (int(c) * 2)
    fix_memory(a, int(value), 'update')


def slt(line):
    line = line.replace('slt', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    c = fix_memory(c, 0, 'find')
    value = 0
    if int(b) < int(c):
        value = 1
    fix_memory(a, value, 'update')


def slti(line):
    line = line.replace('slti', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    value = 0
    if int(b) < int(c):
        value = 1
    fix_memory(a, value, 'update')


def num_to_binary(num):
    r = 1
    c = 0
    print('the binary of ', num)
    while int(num) != 0:
        c += int(num % 2) * r
        r *= 10
        num = int(num / 2)
    print('is ', c)
    c = fix_binary(c)
    return c


def binary_to_num(binary):
    n = len(binary)
    n -= 1
    n2 = n
    answer = 0
    print('the number of ', binary)
    while n > -1:
        if binary[n] == '1':
            answer += (2 ** (n2 - n))
        n -= 1
    print('is ', answer)
    return answer


def fix_binary(binary):
    binary = str(binary)
    n = 7
    n -= len(binary)
    answer = str()
    while n > -1:
        answer += '0'
        n -= 1
    if (len(answer) + len(binary)) == 8:
        answer += binary
    else:
        if len(binary) > 8:
            answer = str()
            tt = len(binary)
            tt -= 8
            for j in range(0, 8):
                answer += binary[tt]
                tt += 1
        else:
            answer = binary
    print('fixed binary is ', answer)
    return answer
# qw = num_to_binary(16)
# qw = fix_binary(qw)
# qw = '11111111'
# qw = binary_to_num(qw)


def and_f(line):
    line = line.replace('and', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    b = num_to_binary(int(b))
    c = fix_memory(c, 0, 'find')
    c = num_to_binary(int(c))
    print('b is ', b)
    print('c is ', c)
    ss = str()
    for i2 in range(0, 8):
        if b[i2] != c[i2]:
            ss += '0'
        else:
            ss += b[i2]
    print('final is ', ss)
    value = binary_to_num(ss)
    print('value is ', value)
    fix_memory(a, value, 'update')


def or_f(line):
    line = line.replace('or', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    b = num_to_binary(int(b))
    c = fix_memory(c, 0, 'find')
    c = num_to_binary(int(c))
    print('b is ', b)
    print('c is ', c)
    ss = str()
    for i2 in range(0, 8):
        if b[i2] == '0' and c[i2] == '0':
            ss += '0'
        else:
            ss += '1'
    print('final is ', ss)
    value = binary_to_num(ss)
    print('value is ', value)
    fix_memory(a, value, 'update')


def andi(line):
    line = line.replace('andi', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = line[2]
    b = fix_memory(b, 0, 'find')
    b = num_to_binary(int(b))
    c = num_to_binary(int(c))
    print('b is ', b)
    print('c is ', c)
    ss = str()
    for i2 in range(0, 8):
        if b[i2] != c[i2]:
            ss += '0'
        else:
            ss += b[i2]
    print('final is ', ss)
    value = binary_to_num(ss)
    print('value is ', value)
    fix_memory(a, value, 'update')


def nori(line):
    line = line.replace('nori', " ")
    line = line.strip()
    line = line.split(',')
    a = line[0]
    b = line[1]
    c = int(line[2])
    print(line)
    print(c)
    b = fix_memory(b, 0, 'find')
    b = num_to_binary(int(b))
    c = num_to_binary(c)
    print('b is ', b)
    print('c is ', c)
    ss = str()
    for i2 in range(0, 8):
        if b[i2] == '0' and c[i2] == '0':
            ss += '1'
        else:
            ss += '0'
    print('final is ', ss)
    value = binary_to_num(ss)
    print('value is ', value)
    fix_memory(a, value, 'update')

def brain(page):
    if page.find('addi') != -1:
        addi(page)
        return True
    elif page.find('add') != -1:
        add(page)
        return True
    elif page.find('sub') != -1:
        sub(page)
        return True
    elif page.find('lw') != -1:
        lw(page)
        return True
    elif page.find('sw') != -1:
        sw(page)
        return True
    elif page.find('sll') != -1:
        sll(page)
        return True
    elif page.find('srl') != -1:
        srl(page)
        return True
    elif page.find('andi') != -1:
        andi(page)
        return True
    elif page.find('and') != -1:
        and_f(page)
        return True
    elif page.find('nori') != -1:
        nori(page)
        return True
    elif page.find('or') != -1:
        or_f(page)
        return True
    elif page.find('slti') != -1:
        slti(page)
        return True
    elif page.find('slt') != -1:
        slt(page)
        return True
    else:
        return False
# def read_book(start_point):
#     while start_point < len_book :
#         my_request = brain(book[start_point])


def jump(page):
    print(page)
    if page[0] == 'j' and page[1] == " ":
        print('i found jump command')
        page = page.replace('j', " ")
        page = page.strip()
        for point in back_point:
            print(point, '   ', page)
            if point.find(page) != -1:
                print('i found point very well ', back_point[point])
                page = back_point[point]
                return page
    elif page.find('beq') != -1:
        page = page.replace('beq', " ")
        page = page.strip()
        page = page.split(',')
        a = fix_memory(page[0], 0, 'find')
        b = fix_memory(page[1], 0, 'find')
        c = page[2]
        c = c.strip()
        if int(a) == int(b):
            for point in back_point:
                print(point, '   ', c)
                if point.find(c) != -1:
                    print('i found beq point very well ', back_point[point])
                    page = back_point[point]
                    return page
        else:
            return -1
    elif page.find('bne') != -1:
        page = page.replace('bne', " ")
        page = page.strip()
        page = page.split(',')
        a = fix_memory(page[0], 0, 'find')
        b = fix_memory(page[1], 0, 'find')
        c = page[2]
        if int(a) != int(b):
            c = c.strip()
            for point in back_point:
                print(point, '   ', c)
                if point.find(c) != -1:
                    print('i found beq point very well ', back_point[point])
                    page = back_point[point]
                    return page
        else:
            return -1

    else:
        return -1


def reader(start, end, f2):
    page = start
    while page < end:
        if f2 >= 300:
            print('out of f < 300 line limited')
            break
        f2 += 1
        print(f2, ' _ ', page, 'end = ', end, '  and start = ', start)
        new = str(book[page])
        new = new.strip()
        if new.find(':') == -1 and len(new) > 1:
            founded = brain(new)
            if not founded:
                go = jump(new)
                if go >= 0:
                    reader(int(go), end, f2)
                    break
        page += 1


reader(first_page, len_book, 0)
print('\n\n', memory_R)
