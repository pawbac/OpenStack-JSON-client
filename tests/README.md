
Files:
config.ini - congiration file for the demo scripts
openstackclient.py - module for accessing Openstack API for servers/images/flavors

Requirements

1. install nosetests for python
	apt-get install python-nose

2. create tests folder inside root folder
	ex. openstackclient\trunk\tests

Instructions
	
1. create 2 nosetests scripts for success & failure
	ex. subnet_list_sucess.py
		subnet_list_failure.py

2. append system path of the test scripts
	import sys
	sys.path.append('../..')
	
3. execute nosetests command in the root foolder (ex. trunk)

	# Run all Test Scripts
	$ nosetests -v tests/*.py
	
	# Run all Successfull Test Scripts
	$ nosetests -v tests/*_success.py
	
	# Run specific Test Script
	$ nosetests -v tests/subnet_list_failure.py


-fgt <francis-tonacao.tonacfra@tieto.com>
