from ncclient import manager
from jinja2 import Template
import yaml

'''
This script is designed to create an IOS-XE DHCP server along with the associated VLANs, SVIs, and access port configs.
'''

# Read in Device Details
with open("../device_details/dhcp_details.yml") as f:
    device_details = yaml.safe_load(f.read())

# Read in templates
with open("../templates/vlan.j2") as f:
    vlan_temp = Template(f.read())

with open("../templates/l2_interface.j2") as f:
    l2_int_temp = Template(f.read())

with open("../templates/l3_interface.j2") as f:
    l3_int_temp = Template(f.read())

with open("../templates/dhcp.j2") as f:
    dhcp_temp = Template(f.read())

# Render variables into template
for d in device_details["host"]:
    with open("../configs/wan_vlan_config.cfg", "w") as f:
        vlan_config = vlan_temp.render(vlans=d["vlans"])
        f.write(vlan_config)

    with open("../configs/wan_l2_int_config.cfg", "w") as f:
         l2_int_config = l2_int_temp.render(l2_ports=d["l2_interface"])
         f.write(l2_int_config)

    with open("../configs/wan_l3_int_config.cfg", "w") as f:
        l3_int_config = l3_int_temp.render(l3_ports=d["l3_interface"])
        f.write(l3_int_config)

    with open("../configs/wan_dhcp_config.cfg", "w") as f:
        dhcp_config = dhcp_temp.render(dhcp=d["dhcp"])
        f.write(dhcp_config)

for d in device_details["host"]:

    with manager.connect(host=d["ip"],
                         username=d["username"],
                         password=d["password"],
                         port=d["port"],
                         allow_agent=False,
                         look_for_keys=False,
                         hostkey_verify=False) as m:

        vlan_resp = m.edit_config(vlan_config, target= 'running')

        l2_int_resp=m.edit_config(l2_int_config, target='running')

        l3_int_resp=m.edit_config(l3_int_config, target='running')

        dhcp_resp=m.edit_config(dhcp_config, target='running')
