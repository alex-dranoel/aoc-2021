from itertools import combinations
from collections import Counter
ll = [l.strip().split(' | ')[1].split() for l in open('input.txt')]
dd = [l.strip().split(' | ')[0].split() for l in open('input.txt')]
a_ll = [l.strip().replace(' | ', ' ').split() for l in open('input.txt')]

print('N lines:', len(a_ll))

acc=0
for w in ll:
    for l in w:
        if len(l) == 2 or len(l) == 3 or len(l) == 4 or len(l) == 7:
            acc+=1

print(acc)

print('----------')
def get_mapping(w):
    m = {}
    two = set([l for l in w if len(l) == 2][0])
    three = set([l for l in w if len(l) == 3][0])
    four = set([l for l in w if len(l) == 4][0])

    # here there are three possible digits: '6', '9' and '0'
    six = [list(l) for l in w if len(l) == 6]

    # top segment 'a' is the one remaining when doing 7 - 1 (three - two)
    a = three - two
    # bottom segment 'g' is what's left from '9' after removing '4' and '7'.
    # segment 'e' would still be there for '6' and '0', so filtering on len(s) == 1
    g = [s for s in [set(l) - four - three for l in six] if len(s) == 1][0]
    # bottom-left segment 'e' is what's left from '6' or '0' after removing '4', '7' and the bottom segment 'g'
    e = [s for s in [set(l) - four - three - g for l in six] if len(s) == 1][0]
    # top-left segment 'b' is what's left from '0' after removing '7', bottom ('g') and bottom-left ('e')
    # segment 'd' would still be there for the '6' and '9', so filtering on len(s) == 1
    b = [s for s in [set(l) - three - g - e for l in six] if len(s) == 1][0]
    # center segment 'd' is what's left from '6' or '9' after removing '7', bottom ('g'), bottom-left ('e') and top-left ('b')
    d = [s for s in [set(l) - three - g - e - b for l in six] if len(s) == 1][0]
    # bottom-right segment 'f' is what's left from '6' after removing bottom ('g'), bottom-left ('e'), top-left ('b'), center ('d'), and top ('a')
    # segment 'c' would still be there for the '0' and '9', so filtering on len(s) == 1
    f = [s for s in [set(l) - g - e - b - d - a for l in six] if len(s) == 1][0]

    # find the missing segment 'c'
    c = set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) - a - b - d - e - f - g
    
    # just convert to a normal mapping dictionnary
    m[a.pop()] = 'a'
    m[b.pop()] = 'b'
    m[c.pop()] = 'c'
    m[d.pop()] = 'd'
    m[e.pop()] = 'e'
    m[f.pop()] = 'f'
    m[g.pop()] = 'g'
    return m

# build a map for seven segment display
seven_seg = {
    'cf' : '1',
    'acdeg' : '2',
    'acdfg' : '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
    'abcefg': '0'
}

acc = 0
for i,w in enumerate(a_ll):
    m = get_mapping(w)
    answ = ''
    for l in ll[i]:
        new_l = ''
        for c in l:
            new_l += m[c]
        l = ''.join(sorted(list(new_l)))
        answ += seven_seg[l]

    print(int(answ))
    acc+=int(answ)

print('Final:', acc)

