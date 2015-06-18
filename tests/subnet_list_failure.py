import sys
sys.path.append('../..')
 
import time
from openstackclient import CCloud
import unittest

class TddInSubnetMgmt(unittest.TestCase):
	
	def setUp(self):
		self.cc = CCloud()
		self.token = self.cc.get_tokens()
		
		# Create Sample Network1 & Network2 w/o Subnet
		resp1 = self.cc.create_network(self.token, "sample_network1", "false")
		resp2 = self.cc.create_network(self.token, "sample_network2", "false")
		
		# Get Network1 & Network2 ID of created sample networks
		self.networks = self.cc.list_networks(self.token)
		for net in self.networks['networks']:
			if net['name'] == "sample_network1":
				self.network_id1 = net['id']
			elif net['name'] == "sample_network2":
				self.network_id2 = net['id']
		
		self.cidr1 = "10.0.10.0/24"
		self.name1 = "sample_subnet1"
		self.ip_version1 = "4"
		
		self.cidr2 = "10.0.20.0/24"
		self.name2 = "sample_subnet2"
		self.ip_version2 = "4"
		
		# Create Sample Subnet
		resp1 = self.cc.create_subnet(self.token, self.name1, self.cidr1, self.network_id1, self.ip_version1)
		resp2 = self.cc.create_subnet(self.token, self.name2, self.cidr2, self.network_id2, self.ip_version2)
		
	def tearDown(self):
		# Delete Created Sample Networks
		resp1 = self.cc.delete_networks(self.token, self.network_id1)
		resp2 = self.cc.delete_networks(self.token, self.network_id2)
		
		self.cc = None
		self.token = None
		self.networks = None
		self.cidr1 = None
		self.name1 = None
		self.ip_version1 = None
		self.cidr2 = None
		self.name2 = None
		self.ip_version2 = None
		
	def test_subnet_list_failure(self):
		# Set Invalid Token
		resp = self.cc.list_subnets('123456')
		# Expected Error / 401 - Unauthorized
		self.assertTrue(resp, 401)
			
if __name__ == '__main__':
    unittest.main()
