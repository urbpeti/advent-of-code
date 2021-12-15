import unittest
from unittest import TestCase
from index import Solver

class TestSolver(TestCase):
    def test_task1(self):
        solver = Solver()
        self.assertEqual(solver.solve_task1(['>']), 0)

    def test_task2(self):
        solver = Solver()
        self.assertEqual(solver.solve_task2(['']), 0)


if __name__ == '__main__':
    unittest.main()
