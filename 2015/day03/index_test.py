import unittest
from unittest import TestCase
from index import Solver

class TestSolver(TestCase):
    def test_task1(self):
        solver = Solver()
        self.assertEqual(solver.solve_task1(['>']), 2)
        self.assertEqual(solver.solve_task1(['^>v<']), 4)
        self.assertEqual(solver.solve_task1(['^v^v^v^v^v']), 2)

    def test_task2(self):
        solver = Solver()
        self.assertEqual(solver.solve_task2(['^v']), 3)
        self.assertEqual(solver.solve_task2(['^>v<']), 3)
        self.assertEqual(solver.solve_task2(['^v^v^v^v^v']), 11)


if __name__ == '__main__':
    unittest.main()
