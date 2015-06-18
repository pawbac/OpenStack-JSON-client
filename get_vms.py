#!/usr/bin/python

from openstackclient import CCloud

cc = CCloud()

def list_vms(token):
    print "------VMs LIST------"
    resp = cc.list_instances(token)

    if isinstance(resp, str): # Error message
        print resp
    elif resp['servers']: # Return instances
        n = 1
        for server in resp['servers']:
            print "\nInstance %s" % n
            print "Status: %s" % (server['status'])
            print "Instance ID: %s" % (server['id'])
            print "Tenant ID: %s" % (server['tenant_id'])
            print "Name: %s" % (server['name'])
            print "Task: %s" % (server['OS-EXT-STS:task_state'])
            print "VM State: %s" % (server['OS-EXT-STS:vm_state'])
            n += 1
    else:
        print "No instances launched"

    return resp
