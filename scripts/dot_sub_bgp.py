from ncclient import manager
from jinja2 import Template
import yaml

'''
This script will use NETCONF to configure a Layer 3 Sub-interface and advertise via BGP
'''

# Read in Device Details
with open("../device_details/dot_sub_bgp.yaml") as f:
    device_details = yaml.safe_load(f.read())

# Read in templates
with open("../templates/dot1q_sub.j2") as f:
    dot1q_sub_temp = Template(f.read())

with open("../templates/bgp_network_statement.j2") as f:
    bgp_net_temp = Template(f.read())

# Render variables into template
for d in device_details["hosts"]:

    with open("../configs/dot1q_sub.cfg", "w") as f:
        dot1q_sub_config = dot1q_sub_temp.render(ports=d["interfaces"])
        f.write(dot1q_sub_config)

    with open("../configs/bgp_net.cfg", "w") as f:
        bgp_net_config = bgp_net_temp.render(asn=d["asn"],
                                             prefix=d["interfaces"])
        f.write(bgp_net_config)

for d in device_details["hosts"]:

    with manager.connect(host=d["ip"],
                         username=d["username"],
                         password=d["password"],
                         port=d["port"],
                         allow_agent=False,
                         look_for_keys=False,
                         hostkey_verify=False) as m:

        dot1q_sub_resp = m.edit_config(dot1q_sub_config, target='running')

        bgp_net_resp = m.edit_config(bgp_net_config, target='running')


        
