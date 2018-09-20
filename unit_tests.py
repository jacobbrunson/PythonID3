import unittest

from node import Node

class NodeTest(unittest.TestCase):
	def setUp(self):
		#This is basically the truth table for (A || B) && !C
		examples = [
			{'A': 0, 'B': 0, 'C': 0, 'class': 0},
			{'A': 0, 'B': 0, 'C': 1, 'class': 0},
			{'A': 0, 'B': 1, 'C': 0, 'class': 1},
			{'A': 0, 'B': 1, 'C': 1, 'class': 0},
			{'A': 1, 'B': 0, 'C': 0, 'class': 1},
			{'A': 1, 'B': 0, 'C': 1, 'class': 0},
			{'A': 1, 'B': 1, 'C': 0, 'class': 1},
			{'A': 1, 'B': 1, 'C': 1, 'class': 0},
		]
		self.node = Node(examples)

	def testEntropy(self):
		expected = 0.95443
		self.assertAlmostEqual(self.node.entropy(), expected, places=5)

	def testIG(self):
		(left, right) = self.node.split('A')
		expected = 0.04879
		self.assertAlmostEqual(self.node.informationGain(left, right), expected, places=5)

	def testMajorityClass(self):
		self.assertEqual(self.node.majorityClass(), 0)


if __name__ == '__main__':
    unittest.main()