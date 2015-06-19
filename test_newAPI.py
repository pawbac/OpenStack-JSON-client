#!/usr/bin/python

from openstackclient_newAPI import CCloud
from get_vms import list_vms

cc = CCloud()
token = cc.get_tokens()

def test():
    flavor = "42" # m1.nano
    image = "3a9b5851-45fb-4e02-b9bc-994717ac8af1" # cirros-0.3.4-x86_64-uec
    nic = "4f9fb47f-737b-4b3d-aa39-a1c71725cf53"
    secgr = "default"

    #cc.create_instance(flavor, image, nic, secgr, "sample1", token)
    #cc.create_instance(flavor, image, nic, secgr, "sample2", token)
    #cc.create_instance(flavor, image, nic, secgr, "sample3", token)

    #sample_id = cc.get_server_id(token, "sample1")
    #cc.delete_instance(sample_id, token)

    #list_vms(token)

test()
