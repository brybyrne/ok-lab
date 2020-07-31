import yaml
from jinja2 import Template
import yaml
from pprint import pprint

'''
This script reads in a yaml file to to generate CLI to remove host entries for an IOS terminal server. Output is CLI for
cut and paste.
'''

# Read in configuration file
print ("Reading in Configuraiton File")
with open("../device_details/rhosts.yaml") as f:
    rhosts_details = yaml.safe_load(f.read())
    pprint(rhosts_details)

# Read in jinja template
with open("../templates/rm_rhosts.j2") as f:
    rhosts_template = Template(f.read())

#Render the template
rhosts_config = rhosts_template.render(hosts=rhosts_details["host"])

print(rhosts_config)
