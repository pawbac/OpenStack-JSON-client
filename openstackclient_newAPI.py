## @package openstackclient
# @author Dino Madarang
#
# A simple Openstack REST Client
#
# This is a simple openstack rest client for getting tokens, managing a servers,
# retrieving tenants and many more features.
#

import ConfigParser
import httplib2
# try:
    # import simplejson as json
# except ImportError:
    # import json
import json

class CCloud(object):

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('config.ini')

    def get_tokens(self):
        h = httplib2.Http()

        resp, content = h.request(self.config.get('test', 'tokensUrlV3'),
                                  "POST", body='{"auth": {"identity": {"methods": ["password"],"password": {"user": {"id":"' +
                                  self.config.get('test', 'userID') + '","password": "' +
                                  self.config.get('test', 'tenantPassword') + '"}}}}}',
                                  headers={'content-type':'application/json'})

        #data = json.loads(content)
        return content

    def list_instances(self, token):
        request_url = self.config.get('test', "computeApiV21") + self.config.get('test', "tenantId")
        h = httplib2.Http()

        resp, content = h.request(request_url,
                                  "GET", headers={'X-Auth-Token':token})
        print content
        # Returns intacnces or error description
        if resp['status'] == '200' or resp['status'] == '203':
            content = json.loads(content)
            return content
        else:
            return content

    def get_server_id(self, token, name):
        request_url = self.config.get('test', "computeApi") + \
                        self.config.get('test', "tenantId") + "/servers?" + name
        h = httplib2.Http()

        resp, content = h.request(request_url, "GET",
                                  headers={'content-type':'application/json', 'X-Auth-Token':token})

        data = json.loads(content)
        return data["servers"][0]["id"]

    def generate_key(self, ten_id, key_name, token):
        h = httplib2.Http()

        resp, content = h.request(self.config.get('test', 'keysUrl'),
                                  "POST", body='{"keypair":{"name":"' + key_name + '","tenant_id":"' + self.config.get('test', "tenantId") + '"}}',
                                  headers={'content-type':'application/json', 'X-Auth-Token':token})

        data = json.loads(content)
        return data

    def create_instance(self, flavor, image, nic, secgr, name, token):
        request_url = self.config.get('test', "computeApi") + self.config.get('test', "tenantId") + '/servers'
        h = httplib2.Http()

        resp, content = h.request(request_url,
                                  "POST", body='{"server":{"name":"' + name +
                                  '","imageRef":"' + image +
                                  '","flavorRef":"' + flavor +
                                  # '","key_name":"' + key +
                                  '","networks":[{"uuid":"' + nic + 
                                  '"}],"security_groups":[{"name":"' + secgr + '"}]}}',
                                  headers={'content-type':'application/json', 'X-Auth-Token':token})

        data = json.loads(content)
        return data

    def delete_instance(self, server_id, token):
        request_url = self.config.get('test', "computeApi") + self.config.get('test', "tenantId") + "/servers/" + server_id
        h = httplib2.Http()

        resp, content = h.request(request_url, "DELETE", headers={'content-type':'application/json', 'X-Auth-Token':token})

	return content
