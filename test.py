#!/usr/bin/python

import time

from openstackclient import CCloud
from get_vms import display_vms

cc = CCloud()
token = cc.get_tokens()

def test():
	name = "sample"
	flavor = "1" # m1.tiny
	image = "3a9b5851-45fb-4e02-b9bc-994717ac8af1" # cirros-0.3.4-x86_64-uec
	nic = "4f9fb47f-737b-4b3d-aa39-a1c71725cf53"
	secgr = "default"

	#cc.create_instance(flavor, image, nic, secgr, name, token)
	#cc.create_instance(flavor, image, nic, secgr, "sample2", token)

	#sample_id = cc.get_server_id(token, name)
	#print "InstanceID found"
	#time.sleep(300)
	#cc.delete_instance(sample_id, token)

	#time.sleep(300)
	display_vms(token)

test()




