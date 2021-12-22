from collections import defaultdict

p1_pos = 3
p2_pos = 4
pos = {1:p1_pos, 2:p2_pos}
score = {1:0, 2:0}

def roll(n, start):
    i = start
    out = [None]*3
    
    for j in range(n):
        out[j] = i
        i+=1
        if i == 101:
            i = 1
    
    return out, i

n_roll = 0
start = 1
while True:

    p, start = roll(3, start)
    n_roll += 3
    tot = sum(p)
    pos[1] += tot
    while pos[1] > 10:
        pos[1] -= 10

    score[1] += pos[1]

    if score[1] >= 1000:
        print(score[2]*n_roll)
        break


    p, start = roll(3, start)
    n_roll += 3

    tot = sum(p)
    pos[2] += tot
    while pos[2] > 10:
        pos[2] -= 10

    score[2] += pos[2]
    if score[2] >= 1000:
        print(score[1]*n_roll)
        break

    print(n_roll)


single_player_outcomes = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

p1_wins = 0
p1_wins_ = 0
p2_wins = 0
tot_score_and_pos = defaultdict(int)
tot_score_and_pos[((0, p1_pos), (0, p2_pos))] += 1

while len(tot_score_and_pos) > 0:
    tot_score_and_pos_new = defaultdict(int)
    for kk, vv in tot_score_and_pos.items():
        for k1, v1 in single_player_outcomes.items():

            p1 = kk[0][1] + k1
            p1 -= int(p1>10) * 10
            s1 = kk[0][0] + p1
            if s1 >= 21:
                p1_wins += v1*vv
                continue

            for k2, v2 in single_player_outcomes.items():

                p2 = kk[1][1] + k2
                p2 -= int(p2 > 10) * 10
                s2 = kk[1][0] + p2
                if s2 >= 21:
                    p2_wins += v1*v2*vv
                    continue

                tot_score_and_pos_new[((s1,p1), (s2,p2))] += v1*v2*vv

    tot_score_and_pos = tot_score_and_pos_new


print(p1_wins)
print(p2_wins)

