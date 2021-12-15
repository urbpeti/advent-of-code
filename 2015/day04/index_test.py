import unittest
from unittest import TestCase
from index import Solver

class TestSolver(TestCase):
    def test_task1(self):
        solver = Solver()
        self.assertEqual(solver.solve_task1(['abcdef']), 609043)
        self.assertEqual(solver.solve_task1(['pqrstuv']), 1048970)


if __name__ == '__main__':
    unittest.main()
