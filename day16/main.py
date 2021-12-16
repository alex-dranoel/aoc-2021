from functools import reduce
import operator

l = open('input.txt').readline().strip()
h_size = len(l) * 4
l = (bin(int(l, 16))[2:]).zfill(h_size)

version = 0
v_size = 3
t_size = 3
l_size = 5
op_t_size = 1
op_0_size = 15
op_1_size = 11


def read_literal(data):
    offset = 0
    nbr = ''
    sub_nbr = '1'
    while sub_nbr[0] != '0':
        sub_nbr = ''.join(data[offset:offset+l_size])
        offset += l_size
        nbr += sub_nbr[1:]

    return offset, int(nbr, 2)


def read_op_0(data):
    v = 0
    offset = 0
    tot_l = int(''.join(data[offset:offset+op_0_size]), 2)
    offset += op_0_size
    tot_read_bits = 0
    nbrs = []
    while tot_read_bits < tot_l:
        read_bits, read_v, nbrs_list = read_next_packet(data[offset:])
        tot_read_bits += read_bits
        offset += read_bits
        v += read_v
        nbrs.extend(nbrs_list)
    
    return offset, v, nbrs


def read_op_1(data):
    v = 0
    offset = 0
    n_sub = int(''.join(data[offset:offset+op_1_size]), 2)
    offset += op_1_size
    nbrs = []
    for _ in range(n_sub):
        read_bits, read_v, nbrs_list = read_next_packet(data[offset:])
        offset += read_bits
        v += read_v
        nbrs.extend(nbrs_list)

    return offset, v, nbrs


def read_next_packet(data):
    offset = 0
    v = int(''.join(data[offset:offset+v_size]), 2)
    offset += v_size
    t = int(''.join(data[offset:offset+t_size]), 2)
    offset += t_size

    nbrs = []
    if t == 4:
        read_bits, nbr = read_literal(data[offset:])
        offset += read_bits
        nbrs.append(nbr)

    else:
        op_t = int(''.join(data[offset:offset+op_t_size]), 2)
        offset += op_t_size

        if op_t == 0:
            read_bits, tot_v, nbrs_list = read_op_0(data[offset:])
            offset += read_bits
            v += tot_v


        elif op_t == 1:
            read_bits, tot_v, nbrs_list = read_op_1(data[offset:])
            offset += read_bits
            v += tot_v

        if t == 0:
            nbrs.append(sum(nbrs_list))
        elif t == 1:
            nbrs.append(reduce(operator.mul, nbrs_list, 1))
        elif t == 2:
            nbrs.append(min(nbrs_list))
        elif t == 3:
            nbrs.append(max(nbrs_list))
        elif t == 5:
            nbrs.append(1 if nbrs_list[0] > nbrs_list[1] else 0)
        elif t == 6:
            nbrs.append(1 if nbrs_list[0] < nbrs_list[1] else 0)
        elif t == 7:
            nbrs.append(1 if nbrs_list[0] == nbrs_list[1] else 0)

    return offset, v, nbrs

answers = read_next_packet(l)
print('Part 1', answers[1])
print('Part 2', answers[2][0])
