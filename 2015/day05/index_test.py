import unittest
from unittest import TestCase
from index import Solver

class TestSolver(TestCase):
    def test_task1(self):
        solver = Solver()
        self.assertEqual(solver.solve_task1(['ugknbfddgicrmopn']), 1)
        self.assertEqual(solver.solve_task1(['aaa']), 1)
        self.assertEqual(solver.solve_task1(['jchzalrnumimnmhp']), 0)
        self.assertEqual(solver.solve_task1(['haegwjzuvuyypxyu']), 0)
        self.assertEqual(solver.solve_task1(['dvszwmarrgswjxmb']), 0)
        self.assertEqual(solver.solve_task1(['aaa', 'ugknbfddgicrmopn', 'jchzalrnumimnmhp']), 2)

    def test_task2(self):
        solver = Solver()
        self.assertEqual(solver.solve_task2(['qjhvhtzxzqqjkmpb']), 1)
        self.assertEqual(solver.solve_task2(['xxyxx']), 1)
        self.assertEqual(solver.solve_task2(['uurcxstgmygtbstg']), 0)
        self.assertEqual(solver.solve_task2(['ieodomkazucvgmuy']), 0)


if __name__ == '__main__':
    unittest.main()
