import requests
import json
# import PrettyPrinter


vmanage_ip = 'sandboxsdwan.cisco.com'
mount_point = 'j_security_check'
device_list_url = 'device'

login_url = "https://%s:8443/dataservice/%s" % (vmanage_ip, mount_point)
device_list_url = "https://%s:8443/dataservice/%s" % (vmanage_ip, device_list_url)

login_credentials = {'j_username': 'devnetuser', 'j_password': 'Cisco123!'}

session = requests.session()  # instantiate the requests session
response = session.post(url=login_url, data=login_credentials, verify=False)

if b'<html>' in response.content:
    print('Login Failed')
else:
    print('Login Success')

# note the returned response at this point is "type byte"
# b'{"header":{"generatedOn":1592489531988,"viewKeys":{"uniqueKey":["system-ip"]....
response = session.get(url=device_list_url, verify=False)
response = json.loads(response.content)

for device in response['data']:
    print(device['host-name'],device['local-system-ip'], device['uuid'])

