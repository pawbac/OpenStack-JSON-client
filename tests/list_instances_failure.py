import sys
sys.path.append('../..')

import time
from openstackclient import CCloud
import unittest

class TestListInstancesMethod(unittest.TestCase):
	def setUp(self):
		self.cc = CCloud()
		self.token = self.cc.get_tokens()

		# Create Three Sample CirrOS Instances


def __name__ == '__main__':
	unittest.main()
