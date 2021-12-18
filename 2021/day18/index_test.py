import unittest
from unittest import TestCase
from index import Solver

class TestSolver(TestCase):
    def test_reduce_number(self):
        solver = Solver()
        self.assertEqual(solver.reduce_number('[[[[[9,8],1],2],3],4]'), '[[[[0,9],2],3],4]')
        self.assertEqual(solver.reduce_number('[7,[6,[5,[4,[3,2]]]]]'), '[7,[6,[5,[7,0]]]]')
        self.assertEqual(solver.reduce_number('[[6,[5,[4,[3,2]]]],1]'), '[[6,[5,[7,0]]],3]')
        self.assertEqual(solver.reduce_number('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'), '[[3,[2,[8,0]]],[9,[5,[7,0]]]]')
        self.assertEqual(solver.reduce_number('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(solver.reduce_number('[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'), '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')
        self.assertEqual(solver.add_numbers(['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]',]), '[[[[5,0],[7,4]],[5,5]],[6,6]]')
        self.assertEqual(solver.magnitude('[9,1]'), 29)
        self.assertEqual(solver.magnitude('[1,9]'), 21)
        self.assertEqual(solver.magnitude('[[1,2],[[3,4],5]]'), 143)
        self.assertEqual(solver.magnitude('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'), 4140)

    def test_task1(self):
        solver = Solver("sample.txt")
        self.assertEqual(solver.solve_task1(), 4140)

    def test_task2(self):
        solver = Solver("sample.txt")
        self.assertEqual(solver.solve_task2(), 3993)
        pass


if __name__ == '__main__':
    unittest.main()
