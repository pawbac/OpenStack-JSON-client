#!/usr/bin/python

from openstackclient import CCloud

cc = CCloud()

def list_vms(token):
    print "------VMs LIST------\n"
    resp = cc.list_instances(token)

    if isinstance(resp, str): # Error message
        print resp
    elif resp['servers']: # Return instances
        n = 1
        for server in resp['servers']:
            print "Instance %s" % n
            print "Status: %s" % (server['status'])
            print "Instance ID: %s" % (server['id'])
            print "Tenant ID: %s" % (server['tenant_id'])
            print "Name: %s" % (server['name'])
            print "Task: %s" % (server['OS-EXT-STS:task_state'])
            print "VM State: %s\n" % (server['OS-EXT-STS:vm_state'])
            n += 1
    else:
        print "No instances launched\n"

    return resp

if __name__ == "__main__":
    token = cc.get_tokens()
    list_vms(token)
