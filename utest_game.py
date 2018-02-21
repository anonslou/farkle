import unittest
import game
import multiset as ms


class GameTest(unittest.TestCase):
    
    def test_roll(self):
        self.assertEqual(len(game.roll(-1)), 0)
        for dice_counter in range(0,7):
            self.assertEqual(len(game.roll(dice_counter)), dice_counter)

    def test_score_all(self):
        cases = {'111111': (8000, ''),
                 '234662': (0, '662234'),
                 '222221': (900, ''), 
                 '444235': (450, '32'),
                 '111222': (1200, ''), 
                 '115234': (250, '234'), 
                 '111554': (1100, '4'), 
                 '152346': (150, '2346')}
        for score in cases.keys():
            mset = ms.Multiset(score)
            self.assertEqual(game.score_all(mset), (cases[score][0], ms.Multiset(cases[score][1])))

if __name__ == '__main__':
   unittest.main()
