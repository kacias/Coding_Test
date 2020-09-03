#유닛 테스트 코드 (메인)

# tests.py
import unittest
import myCalc


class MyCalcTest(unittest.TestCase):

    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 10)

if __name__ == '__main__':
    unittest.main()


