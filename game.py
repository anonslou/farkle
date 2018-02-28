#!/usr/bin/env python
import random as rnd
import multiset as ms


def roll(dice_count=6):
    diceset = ''
    for i in range(dice_count):
        diceset += str(rnd.randint(1, 6))
    return ms.Multiset(diceset)


def score_single(diceset):
    diceset = diceset.copy()
    if len(diceset) <= 0:
        return (0, diceset)
    score = diceset['1']*100
    score += diceset['5']*50
    diceset.discard('1')
    diceset.discard('5')
    return score, diceset


def score_sets(d):
    if len(d) < 3:
        return (0, d.copy())
    s = 0
    dd = d.copy()
    for i in d.items():
        if i[1] == 3:
            s += int(i[0])*100
            if i[0] == '1':
                s *= 10
            dd.discard(i[0])
    return s, dd


def score_uniq(d):
    d = d.copy()
    if len(d) < 4:
        return (0, d)
    for i in d.items():
        for j in range(6, 3, -1):
            if i[1] == j:
                s = int(i[0])*100 * pow(2, j-3)
                if i[0] == '1':
                    s *= 10
                return(s, d.difference(i[0]*j))
    return 0, d


def score_all(d):
    d = d.copy()
    sumall, d = score_uniq(d)
    s, d = score_sets(d)
    sumall += s
    s, d = score_single(d)
    sumall += s
    return sumall, d


def game():
    counter = 100000
    for j in range(6, 0, -1):
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


def game_test():
    d = roll()
    print(d)
    s, d = score_all(d)
    print(s, d)


def game_full():
    dice = roll()
    print(dice)
    score, d = score_all(dice)
    print('score: ' + str(score))
    if score == 0:
        print('round score: 0')
        return 0

    while True:
        s = 0
        case = input()
        if case == 'stop':
            score += s
            break
        elif case == 'fix':
            print('enter dices: ', end='')
            inp = input()
            bad_select = False  # TODO rewrite all input checks with exceptions
            for i in inp:
                if i not in dice.difference(d):
                    bad_select = True
                    break
            if bad_select:
                print('bad input, after "fix" you must enter dice with value!')
                continue
            fix = ms.Multiset(inp)
            dice.difference_update(fix)
            s = score_all(fix)[0]
            print('fixed: ' + str(fix))
            if len(dice) == 0:
                dice = roll()
            else:
                dice = roll(len(dice))
            print(dice)
            s, d = score_all(dice)
            if s == 0:
                score = 0
                print('fire!')
                break
            else:
                print('score: ' + str(s))
                score += s
        else:
            print('bad input, use: "fix" or "stop" command')
    print('round score: ' + str(score))
    return score

if __name__ == '__main__':
    game_full()
