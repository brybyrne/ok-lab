from ncclient import manager
from jinja2 import Template
import yaml

'''
This script will use NETCONF to configure a Layer 3 Interface and advertise via BGP
'''

# Read in Device Details
with open("../device_details/l3_int_bgp.yml") as f:
    device_details = yaml.safe_load(f.read())

# Read in templates
with open("../templates/l3_interface.j2") as f:
    l3_int_temp = Template(f.read())

with open("../templates/bgp_network_statement.j2") as f:
    bgp_net_temp = Template(f.read())

# Render variables into template
for d in device_details["hosts"]:

    with open("../configs/l3_int.cfg", "w") as f:
        l3_int_config = l3_int_temp.render(l3_ports=d["l3_interface"])
        f.write(l3_int_config)

    with open("../configs/bgp_net.cfg", "w") as f:
        bgp_net_config = bgp_net_temp.render(asn=d["asn"],
        prefix=d["l3_interface"])
        f.write(bgp_net_config)

for d in device_details["hosts"]:

    with manager.connect(host=d["ip"],
                         username=d["username"],
                         password=d["password"],
                         port=d["port"],
                         allow_agent=False,
                         look_for_keys=False,
                         hostkey_verify=False) as m:

        l3_int_resp = m.edit_config(l3_int_config, target='running')

        bgp_net_resp = m.edit_config(bgp_net_config, target='running')
