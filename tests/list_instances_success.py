import sys
sys.path.append('../..')

import time
from openstackclient import CCloud
import unittest

class TestListInstancesMethod(unittest.TestCase):
	def setUp(self):
		self.cc = CCloud()
		self.token = self.cc.get_tokens()

		# Preset values
		flavor = "42" # m1.tiny
		image = "3a9b5851-45fb-4e02-b9bc-994717ac8af1" # cirros-0.3.4-x86_64-uec
		nic = "4f9fb47f-737b-4b3d-aa39-a1c71725cf53" # private
		secgr = "default"

		# Create Three CirrOS instances
		cc.create_instance(flavor, image, nic, secgr, "sample1", token) #1
		cc.create_instance(flavor, image, nic, secgr, "sample2", token) #2
		cc.create_instance(flavor, image, nic, secgr, "sample3", token) #3

	def tearDown(self):
		# Get Instances' IDs
		sample_id_1 = cc.get_server_id(token, "sample1") #1
		sample_id_2 = cc.get_server_id(token, "sample2") #2
		sample_id_3 = cc.get_server_id(token, "sample3") #2

		# Delete Created Sample Instances
		cc.delete_instance(sample_id_1, token) #1
		cc.delete_instance(sample_id_2, token) #2
		cc.delete_instance(sample_id_3, token) #3
		
	def test_vms_list(self):


def __name__ == '__main__':
	unittest.main()

