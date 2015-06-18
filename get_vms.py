#!/usr/bin/python

from openstackclient import CCloud

cc = CCloud()

def display_vms(token):
	print("------VMs LIST------")
	vms = cc.get_vm_list(token)

	if len(vms['servers']) in vms:
		n = 1
		for server in vms['servers']:
			print "Instance %s" % n
			print "Status: %s" % (server['status'])
			print "Instance ID: %s" % (server['id'])
			print "Tenant ID: %s" % (server['tenant_id'])
			print "Name: %s" % (server['name'])
			print "Task: %s" % (server['OS-EXT-STS:task_state'])
			print "VM State: %s" % (server['OS-EXT-STS:vm_state'])
			print "Power State: %s" % (server['OS-EXT-STS:power_state'])
			print "\n"
			n += 1
	else:
		print "No instances launched"

	return len(vms['servers'])
	
#token = cc.get_tokens()
#display_vms(token)



