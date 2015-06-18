#!/usr/bin/python
#Demo Script 
#
# Copyright 

from openstackclient import CCloud

cc = CCloud()
token = cc.get_tokens()

## @brief Displays tenants and corresponding details.
# @author Hershe L. Abellana
# @param None
# @return None
def display_tenants():
	print("------TENANT LIST------")
	tenant = cc.get_tenants(token)

	if 'tenants' in tenant:
		# Display tenants and details
		n = 1
		for item in tenant['tenants']:
			print "Tenant %s" % n
			print "ID: %s" % (item['id'])
			print "Name: %s" % (item['name'])
			print "Description: %s" % (item['description'])
			print "Enabled: %s" % (str(item['enabled']))
			print "\n"
			n += 1
	else:
		# Display Error Response
		resp = tenant['error']
		print "Error %s (%s) - %s" % (resp['title'], str(resp['code']), resp['message'])

display_tenants()




