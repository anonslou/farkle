#!/usr/bin/env python
import random as rnd
import multiset as ms

def roll(dice_count=6):
    diceset = ''
    for i in range(dice_count):
        diceset += str(rnd.randint(1,6))
    return ms.Multiset(diceset)

def score_single(diceset):
    if len(diceset) <= 0:
        return (0, diceset)
    score = diceset['1']*100
    score += diceset['5']*50
    diceset.discard('1')
    diceset.discard('5')
    return (score, diceset)

def score_sets(d):
    if len(d) < 3:
        return (0, d)
    s = 0
    dd = d.copy()
    for i in d.items():
        if i[1] == 3:
            s += int(i[0])*100
            if i[0] == '1':
                s *= 10
            dd.discard(i[0])
    return (s, dd)

def score_uniq(d):
    if len(d) < 4:
        return (0, d)
    for i in d.items():
        for j in range(6,3,-1):
            if i[1] == j:
                s = int(i[0])*100 * pow(2, j-3)
                if i[0] == '1':
                    s *= 10
                return(s, d.difference(i[0]*j))
    return (0, d)

def score_all(d):
    sumall, d = score_uniq(d)
    s, d = score_sets(d)
    sumall += s
    s, d = score_single(d)
    sumall += s
    return (sumall, d)

def game():
    counter = 100000
    for j in range(6,0,-1):
        score = 0
        zero = 0
        for i in range(counter):
            d = roll(j)
            s, d = score_all(d)
            score += s
            if s == 0:
                zero += 1
        print(j, end='\t')
        print('avg: ' + str(score/counter), end='\t')
        print('fail: ' + str(zero*100/counter))

def game2():
    counter = 10000
    success = 0
    avg = 0
    fail = 0
    for i in range(counter):
        ss = 0
        d = roll(6)
        s, d = score_all(d)
        if s == 50 or s == 100:
            ss = s
            d = roll(5)
            s, d = score_all(d)
            if s > 0:
                avg += ss + s
                success += 1
            else:
                fail += 1
    print(fail*100/success)
    print(avg/success)

def game_test():
    d = roll()
    print(d)
    s, d = score_all(d)
    print(s, d)

if __name__ == "__main__":
    game_test()

